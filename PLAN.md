# Plan: plain-language skill, version 1.0

Goal: an installable agent skill that writes and rewrites text in plain language, anchored to named standards, with a mechanical checker. The reference implementation for the architecture is our simplified-technical-english skill: SKILL.md with distilled rules, reference files with the full guidance, worked examples, and a checker script that closes a write-check-fix loop. A style skill without a checker is a prompt, not a standard, so the checker is work package one.

## Sources and legal basis

- US Federal Plain Language Guidelines (plainlanguage.gov): work of the US government, public domain. This project may quote, summarize, and adapt it freely, with a courtesy attribution in NOTICE.md.
- ISO 24495-1:2023, Plain language, Part 1: Governing principles and elements: paywalled and copyrighted by ISO. The skill cites the standard by number and paraphrases its four governing principles (relevant, findable, understandable, usable). It never reproduces normative text.
- Flesch Reading Ease and Flesch-Kincaid Grade Level: published formulas from 1970s research, freely implementable.
- If EQUATOR checklists or other third-party material ever join the references, each gets its own NOTICE.md entry before it lands.

## Non-goals for version 1.0

- No reproduction of ISO text, and no claim of ISO certification or endorsement.
- No audience-tuned reading-level targets (a 1.1 candidate once the base checker is proven).
- No marketplace publishing. That is a separate decision after the acceptance criteria below pass.

## Layout

Mirrors simplified-technical-english:

```
SKILL.md                  distilled rules and procedure, about 120 lines
references/rules.md       full rule set, each rule with a before-and-after pair
references/word-list.md   simple-first substitutions and a jargon watch list
references/reading-level.md   formulas and target scores
scripts/plain_check.py    the checker
examples/before-after.md  six to eight worked pairs
LICENSE, NOTICE.md, README.md, PLAN.md
```

## Work packages

### WP1: checker first

Call the checker as `plain_check.py` with a mode argument of procedure or information and a file path; it exits non-zero on errors. Checks: sentences over the length cap (20 words procedural, 25 informational), passive-voice constructions, paragraphs over six sentences, nominalizations against a substitutions list, jargon watch-list hits, missing articles in imperative procedures, and a Flesch-Kincaid grade estimate reported per section. Warnings are informational; errors block.

Acceptance: the checker catches every planted violation in a test corpus of at least ten paragraphs, and reports zero errors on docs/RESEARCH-CASE-V2.md from the inference-rig repository as the known-clean control.

### WP2: SKILL.md

Scope section (apply to documentation, policy text, instructions, and reports; not to poetry, marketing, code, or quoted material), text classification into procedure and information, verb rules (active voice, simple tenses, direct address as "you"), sentence rules (one idea per sentence, length caps, condition before command with a comma), word rules (everyday word first, no nominalizations, define a term once and use it consistently), structure rules (headings that describe, lists for steps and options, tables for comparisons), and the check step that names the script. Target: a competent agent can apply the skill from SKILL.md alone; the references carry the depth.

### WP3: references

rules.md states each rule with one before-and-after pair. word-list.md carries a simple-first substitutions table (it reuses the STE substitutions where the two standards agree, since plain language and STE overlap heavily on wordiness) plus a jargon watch list for legal, policy, and bureaucratic registers. reading-level.md documents the formulas, the grade targets per register, and the honest limits of readability scores.

### WP4: examples

before-after.md with six to eight pairs: a policy paragraph, an instruction set, a technical description, a legal-adjacent warning, a table-heavy section, and one deliberate failure case showing where plain language is the wrong tool.

### WP5: install and verification

Install to ~/.zcode/skills, ~/.agents/skills, and ~/.claude/skills, following the simplified-technical-english pattern. Run the acceptance corpus and the clean control, run the checker on this repository's own README as a dogfood pass, and record results in the release notes.

### WP6: release and publish (separate decision)

Tag v1.0, add release-repo-standard artifacts if releasing, then decide whether to publish on the skill marketplace under the jgsystemsconsulting account.

## Milestones

- M1: repository scaffold and this plan (the initial commit).
- M2: checker passes the acceptance corpus and the clean control.
- M3: SKILL.md, references, and examples complete.
- M4: installed in all three locations, checker green, dogfood pass recorded, v1.0 tagged.

## Risks and mitigations

- Plain language has no closed dictionary the way ASD-STE100 has its 869 approved words, so the checker under-detects vocabulary problems by design. SKILL.md carries the same honest clause the STE skill uses: the tool cannot find all errors, and the writer must still compare the words against the guidance.
- ISO 24495 has announced further parts (legal communication among them), and guidance may shift. The skill states its Issue basis and versions against it.
- Overlap with the avoid-ai-writing skill and prose_check.py in the local environment. SKILL.md states the precedence: plain-language governs structure and vocabulary; avoid-ai-writing governs AI tells; both may run on the same file.
