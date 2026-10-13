# Reading level

The checker prints one Flesch-Kincaid grade line per markdown section. The grade is a report line. It is never an error and never a warning, and it does not affect the exit code. Version 1.0 gates on nothing here.

## Formulas

- Reading Ease = 206.835 - 1.015 x ASL - 84.6 x ASW
- Grade Level = 0.39 x ASL + 11.8 x ASW - 15.59

ASL is words per sentence. ASW is syllables per word.

Sources: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests and the Navy derivation report https://apps.dtic.mil/sti/pdfs/ADA006655.pdf (Kincaid, Fishburne, Rogers, and Chissom, 1975).

## Syllable heuristic

`scripts/plain_check.py` estimates syllables without a dictionary:

- Count vowel groups (`[aeiouy]+`) in the lowercased word.
- Subtract one for a silent trailing `e` when the word does not end in `le`.
- Floor the count at one syllable per word.
- No exception dictionary.

## Limits

The heuristic can be off by about one syllable on irregular words, which moves a grade by a fraction. The grade is an estimate, not a certification, and it says nothing about whether the reader can use the text. Read it as a number to look at, not a gate to pass.

Audience-tuned grade targets are a 1.1 candidate, deferred by PLAN.md.
