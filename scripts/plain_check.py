#!/usr/bin/env python3
"""plain_check.py - check text against plain-language writing rules.

Uses only the Python standard library.

Usage:
    python3 plain_check.py --mode procedure|information FILE...
    cat draft.txt | python3 plain_check.py --mode information
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- constants

LIMITS = {"procedure": 20, "information": 25}

BE = r"am|is|are|was|were|be|been|being"
IRREGULAR = frozenset({
    "made", "known", "shown", "given", "taken", "written", "built",
    "kept", "held", "left", "found", "done", "seen", "paid", "said",
})
PARTICIPLE = r"(?:\w+(?:ed|en)|" + "|".join(sorted(IRREGULAR)) + ")"

PASSIVE_BY = re.compile(
    rf"\b(?:{BE})\s+(?:\w+\s+){{0,2}}{PARTICIPLE}\s+by\b",
    re.IGNORECASE,
)
MODAL_PASSIVE = re.compile(
    rf"\b(?:can|will|must|could|would|should|may|might|shall)\s+"
    rf"(?:not\s+)?be\s+{PARTICIPLE}\b",
    re.IGNORECASE,
)
BARE_PASSIVE = re.compile(
    rf"\b(?:{BE})\s+{PARTICIPLE}\b",
    re.IGNORECASE,
)
NOMINAL = re.compile(
    r"\b(?:make|give|have|take|reach|conduct|perform|undertake)\s+"
    r"(?:a|an|the)\s+\w+(?:tion|sion|ment|ance|ence)\b"
    r"|"
    r"\bthe\s+\w+(?:tion|sion|ment|ance|ence)\s+of\b",
    re.IGNORECASE,
)
IMPERATIVE_VERBS = frozenset({
    "set", "open", "close", "remove", "install", "check", "make", "use",
    "write", "read", "stop", "start", "turn", "press", "select", "enter",
    "save", "send", "add", "delete",
})
DETERMINERS = frozenset({
    "the", "a", "an", "your", "this", "each", "all",
})

# Keep WATCH in sync with references/word-list.md. Update both together.
# Single tokens only. Multi-word dirty-dozen rows live in the reference
# table for the agent. They are not checker tokens in v1.0.
# "in order to" is multi-word; reference lists it, checker does not.
WATCH = {
    "utilize": "use",
    "commence": "start",
    "initiate": "start",
    "prior": "before",
    "obtain": "get",
    "additional": "more",
    "addressees": "you",
    "assist": "help",
    "assistance": "help",
    "implement": "carry out",
    "promulgate": "issue",
    "herein": None,
    "heretofore": None,
    "aforementioned": None,
    "whereby": None,
    "therein": None,
    "notwithstanding": None,
    "whilst": None,
}

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
WORDISH = re.compile(r"[A-Za-z0-9'&/’-]+")
LIST_MARKER = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
HEADING_LINE = re.compile(r"^#{1,6}\s+\S")


# ---------------------------------------------------------------- helpers

def strip_markdown(text):
    """Remove parts of the text that the plain-language rules do not control."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", " CODE ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", " URL ", text)
    text = re.sub(r"^>.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r'"[^"\n]*"', " QUOTED ", text)
    return text


def count_words(sentence):
    """Count words; parenthetical groups and hyphenated groups are one word each."""
    s = re.sub(r"\([^)]*\)", " PAREN ", sentence)
    s = re.sub(r"\*\*|\*|__|_|#+", " ", s)
    return len(WORDISH.findall(s))


def iter_sentences(block):
    """Split a block on . ! ? followed by whitespace. No colon or semicolon split."""
    for part in SENT_SPLIT.split(block):
        part = part.strip()
        if part and WORDISH.search(part):
            yield part


def syllables(word):
    """Estimate syllable count for Flesch-Kincaid."""
    w = word.lower()
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith("le") and n >= 2:
        n -= 1
    return max(1, n)


def word_tokens(text):
    """Return WORDISH tokens from text after the same stripping as count_words."""
    s = re.sub(r"\([^)]*\)", " PAREN ", text)
    s = re.sub(r"\*\*|\*|__|_|#+", " ", s)
    return WORDISH.findall(s)


# ---------------------------------------------------------------- checks

class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.grades = []

    def error(self, loc, rule, msg):
        self.errors.append((loc, rule, msg))

    def warn(self, loc, rule, msg):
        self.warnings.append((loc, rule, msg))


def check_sentence(sent, mode, report, loc):
    limit = LIMITS[mode]
    n = count_words(sent)
    head = sent if len(sent) <= 60 else sent[:57] + "..."
    if n > limit:
        report.error(loc, "PL-S1", f'sentence has {n} words (max {limit}): "{head}"')

    m_by = PASSIVE_BY.search(sent)
    if m_by:
        report.error(
            loc, "PL-V1",
            f'passive voice "{m_by.group(0)}": make the actor the subject',
        )

    m_modal = MODAL_PASSIVE.search(sent)
    if m_modal:
        report.error(
            loc, "PL-V2",
            f'passive voice "{m_modal.group(0)}": make the actor the subject',
        )

    m_bare = BARE_PASSIVE.search(sent)
    if m_bare and not m_modal:
        # PL-V3 only when PL-V2 did not already take the modal frame.
        # A by-frame may still also match bare and emit both PL-V1 and PL-V3.
        report.warn(
            loc, "PL-V3",
            f'passive voice "{m_bare.group(0)}": make the actor the subject',
        )

    if mode == "procedure":
        tokens = word_tokens(sent)
        if tokens:
            first = tokens[0].lower()
            if first in IMPERATIVE_VERBS and len(tokens) >= 2:
                second = tokens[1].lower()
                if second not in DETERMINERS:
                    report.error(
                        loc, "PL-A1",
                        f'imperative "{tokens[0]} {tokens[1]}" has no article. '
                        f'Put "the" or "a" before the noun.',
                    )

    m_nom = NOMINAL.search(sent)
    if m_nom:
        report.warn(
            loc, "PL-N1",
            f'nominalization "{m_nom.group(0)}": use a verb, not a hidden verb',
        )

    for word in word_tokens(sent):
        lw = word.lower()
        if lw in WATCH:
            plain = WATCH[lw]
            if plain is None:
                report.warn(
                    loc, "PL-J1",
                    f'jargon "{word}": consider a plainer word.',
                )
            else:
                report.warn(
                    loc, "PL-J1",
                    f'jargon "{word}": write "{plain}".',
                )
        elif lw == "shall":
            report.warn(loc, "PL-M1", '"shall": write "must".')


def check_text(text, mode, report, name):
    text = strip_markdown(text)
    paragraphs = re.split(r"\n\s*\n", text)
    for i, par in enumerate(paragraphs):
        par = par.strip()
        if not par or not WORDISH.search(par):
            continue
        first = par.lstrip()[:1]
        if first in ("#", "|"):
            continue
        lines = par.splitlines()
        items = []
        prose = []
        for line in lines:
            if LIST_MARKER.match(line):
                items.append(line)
            else:
                prose.append(line)
        for line in items:
            item = LIST_MARKER.sub("", line, count=1)
            for s in iter_sentences(item):
                check_sentence(s, mode, report, f"{name}:list")
        if prose:
            block = "\n".join(prose)
            sents = list(iter_sentences(block))
            loc = f"{name}:par{i + 1}"
            if len(sents) > 6:
                report.error(
                    loc, "PL-P1",
                    f"paragraph has {len(sents)} sentences (max 6).",
                )
            for s in sents:
                check_sentence(s, mode, report, loc)

    # Grade pass: sections on markdown headings. Grades never affect exit.
    emit_grades(text, report, name)


def emit_grades(text, report, name):
    lines = text.splitlines()
    sections = []  # (title, body_lines)
    current_title = None
    current_body = []
    saw_heading = False

    def flush():
        nonlocal current_title, current_body
        if current_title is None and not any(WORDISH.search(l) for l in current_body):
            current_body = []
            return
        title = current_title if current_title is not None else None
        sections.append((title, current_body))
        current_body = []

    for line in lines:
        if HEADING_LINE.match(line):
            flush()
            saw_heading = True
            current_title = re.sub(r"^#{1,6}\s+", "", line).strip()
            current_body = []
        else:
            current_body.append(line)
    flush()

    if not sections:
        return

    # Assign default titles for top matter / whole file.
    if not saw_heading:
        # single section, whole file
        title, body = sections[0]
        _grade_section(name, "(file)", body, report)
        return

    for title, body in sections:
        if title is None:
            if not any(WORDISH.search(l) for l in body):
                continue
            _grade_section(name, "(top)", body, report)
        else:
            _grade_section(name, title, body, report)


def _grade_section(name, title, body_lines, report):
    # Strip list markers so numbered markers are not phantom sentences.
    cleaned = []
    for line in body_lines:
        if LIST_MARKER.match(line):
            cleaned.append(LIST_MARKER.sub("", line, count=1))
        else:
            cleaned.append(line)
    block = "\n".join(cleaned)
    sents = list(iter_sentences(block))
    n_sents = len(sents)
    if n_sents < 2:
        report.grades.append(
            f"GRADE   {name}:# {title}  n/a (too few sentences)"
        )
        return
    words = []
    for s in sents:
        words.extend(word_tokens(s))
    n_words = len(words)
    if n_words == 0:
        report.grades.append(
            f"GRADE   {name}:# {title}  n/a (too few sentences)"
        )
        return
    n_syl = sum(syllables(w) for w in words)
    asw = n_syl / n_words
    grade = 0.39 * (n_words / n_sents) + 11.8 * asw - 15.59
    report.grades.append(
        f"GRADE   {name}:# {title}  FKGL {grade:.1f} "
        f"({n_sents} sentences, {asw:.1f} syllables/word est.)"
    )


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(
        description="Check text against plain-language writing rules."
    )
    ap.add_argument(
        "files", nargs="*", help="files to check (default: stdin)"
    )
    ap.add_argument(
        "--mode",
        choices=["procedure", "information"],
        required=True,
        help="text type: procedure or information",
    )
    args = ap.parse_args()

    report = Report()
    if args.files:
        for f in args.files:
            try:
                text = Path(f).read_text(encoding="utf-8")
            except OSError as e:
                report.error(f"{f}:read", "PL-IO", str(e))
                continue
            check_text(text, args.mode, report, f)
    else:
        check_text(sys.stdin.read(), args.mode, report, "stdin")

    for loc, rule, msg in report.errors:
        print(f"ERROR   {loc} [rule {rule}] {msg}")
    for loc, rule, msg in report.warnings:
        print(f"WARNING {loc} [rule {rule}] {msg}")
    for line in report.grades:
        print(line)

    print(f"\nResult: {len(report.errors)} errors, {len(report.warnings)} warnings.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
