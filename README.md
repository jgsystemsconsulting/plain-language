# plain-language

A skill that writes and rewrites text in plain language. It follows the same layout as our Simplified Technical English skill: rules in SKILL.md, reference files, worked examples, and a mechanical checker. The basis is the US Federal Plain Language Guidelines and ISO 24495-1:2023. This project cites and paraphrases that standard. It does not reproduce it.

Status: shipped. Version 1.0, dated 2026-10-13; [RELEASE-NOTES.md](RELEASE-NOTES.md) records the acceptance results and how the checker was verified. [PLAN.md](PLAN.md) keeps the original work plan. To apply the skill, start with [SKILL.md](SKILL.md), which holds the distilled rules and the write-check-fix procedure.

## Layout

| Path | Contents |
|---|---|
| SKILL.md | Distilled rules and the write-check-fix procedure |
| references/rules.md | Full rule set with before-and-after examples |
| references/word-list.md | Simple-first word guidance and a jargon watch list |
| references/reading-level.md | Readability formulas, report-only grade, honest limits |
| scripts/plain_check.py | Mechanical checker, non-zero exit on errors |
| examples/before-after.md | Worked examples across policy, technical, and legal-adjacent text |

## Related project

[simplified-technical-english](https://github.com/jgsystemsconsulting/simplified-technical-english) is the sibling skill for ASD-STE100. It proves the architecture: a style skill holds up only when a checker closes the loop.

## License

MIT for the text of the skill and its scripts. See [NOTICE.md](NOTICE.md) for the sources this project builds on and the terms that apply to them.
