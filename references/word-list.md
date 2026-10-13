# Word list

This is not a closed dictionary. A word absent from the list is not approved. Absence means the checker said nothing.

The checker warns on the single-word rows marked `checker`. Multi-word rows are for the writer. The script copies the checker rows into `WATCH` in `scripts/plain_check.py`. Update both together.

## Simple-first substitutions

| Don't say | Say | Source |
|---|---|---|
| utilize | use | overlap, checker |
| commence | start | overlap, checker |
| initiate | start | overlap, checker |
| prior | before | overlap, checker |
| obtain | get | overlap, checker |
| additional | more | overlap, checker |
| in order to | to | overlap |
| shall | must | overlap |

`shall` stays in this table for the agent. The checker fires PL-M1, not PL-J1, so the source cell is `overlap` with no `checker` mark.

### Federal dirty dozen

| Don't say | Say | Source |
|---|---|---|
| addressees | you | federal, checker |
| assist | help | federal, checker |
| assistance | help | federal, checker |
| commence | start | federal, checker |
| implement | carry out | federal, checker |
| in accordance with | by, following, per, under | federal |
| in order that | for, so | federal |
| in the amount of | for | federal |
| in the event of | if | federal |
| it is | (omit) | federal |
| promulgate | issue | federal, checker |
| this activity, command | us, we | federal |
| utilize | use | federal, checker |
| utilization | use | federal |

Say-cell values on checker-marked rows match the `WATCH` value exactly (the checker prints that word). Rows without a checker mark keep the federal preferred wording for the writer. `commence` and `utilize` appear in both tables. That is intended: one row records the overlap source, one records the federal source. The checker has each word once.

## Jargon watch list

| Don't say | Say | Source |
|---|---|---|
| herein | omit | project, checker |
| heretofore | omit | project, checker |
| aforementioned | omit | project, checker |
| whereby | omit | project, checker |
| therein | omit | project, checker |
| notwithstanding | omit | project, checker |
| whilst | omit | project, checker |

These seven are project choices, not a federal list.
