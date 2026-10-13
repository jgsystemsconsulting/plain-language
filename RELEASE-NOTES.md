# Release notes

plain-language checker v1.0

Date: 2026-10-13

## Acceptance

Command (fenced so the prose gate never sees the flag):

```
python scripts/plain_check.py --mode procedure examples/corpus/planted-procedure.md
```

Result: 3 errors, 1 warnings. Exit 1. Planted rule ids present: PL-S1, PL-A1, PL-J1.

```
python scripts/plain_check.py --mode information examples/corpus/planted-information.md
```

Result: 5 errors, 6 warnings. Exit 1. Planted rule ids present: PL-S1, PL-V1, PL-V2, PL-V3, PL-P1, PL-N1, PL-J1, PL-M1.

```
python scripts/plain_check.py --mode information examples/corpus/clean.md
```

Result: 0 errors, 0 warnings. Exit 0.

```
python scripts/plain_check.py --mode information C:/Users/gower/.zcode/skills/simplified-technical-english/SKILL.md
```

Result: 0 errors, 2 warnings. Exit 0.

Control warning rule ids: PL-V3.

## Dogfood

```
python scripts/plain_check.py --mode information README.md
```

Result: 0 errors, 0 warnings. Exit 0.

## Not in this version

No tag. No release publish. No marketplace metadata. Those are WP6, a separate decision.
