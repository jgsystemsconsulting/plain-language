# Before and After: Worked Examples

This file shows before-and-after pairs for the plain-language rules. Each pair names the rules it illustrates. The before text carries the faults on purpose, so the checker flags some of it. That result is normal here: this file is writer training, not an acceptance fixture. Pair 6 shows when plain language is the wrong tool.

## 1. Policy paragraph: passive voice, "shall", and a hidden verb

**Before:**

The review board shall make a determination on each appeal. The final decision was recorded by the clerk.

**After:**

The review board must decide each appeal. The clerk recorded the final decision.

Rules: PL-V1 (passive with a "by" frame), PL-M1 (write "must", not "shall"), PL-N1 (do not hide the verb). The rewrite makes the board and the clerk the actors, replaces "shall" with "must", and turns "make a determination" into "decide".

## 2. Instruction set: missing article, long sentence, condition order

**Before:**

Open valve.
Monitor the drain line, the filter housing, and the gauge panel, and record each reading in the shift log before you close the panel, and then report the result to the supervisor on duty.
Shut the intake if the tank level reads high.

**After:**

Open the valve.
If the tank level reads high, shut the intake.
Watch the drain line and the gauge panel.
Record each reading in the shift log, then report to the supervisor on duty.

Rules: PL-A1 (missing article, applied in procedure mode), PL-S1 (20-word procedure cap), and the condition-before-command rule. The checker does not flag condition order. The long instruction also breaks the 25-word information cap, and this file runs in information mode.

## 3. Technical description: noun string, hidden verb, long sentence

**Before:**

The main warehouse loading dock door sensor panel went dark. The completion of the repair depends on a parts shipment. The technician who inspected the panel on Tuesday reported that the wiring harness connector inside the housing showed corrosion damage across three of its contact points.

**After:**

The panel is dark at the loading dock of the main warehouse. The repair waits on a parts shipment. The technician found corroded contacts in the wiring connector on Tuesday. Three contacts show damage.

Rules: the noun-string rule (break a run of four or more nouns), PL-N1 (hidden verb), and PL-S1 (sentence cap). The opening noun string runs seven words. The checker implements no noun-string rule, so that hit is agent-judged. The hidden verb and the 26-word sentence are checker hits.

## 4. Legal-adjacent warning: the exception before the rule

**Before:**

Except during a declared emergency, except when the fire marshal grants a written waiver, and except for pumps on the retired list, the operator shall keep the backup pump fueled at all times.

**After:**

The operator must keep the backup pump fueled at all times. Three exceptions apply: a declared emergency, a written waiver from the fire marshal, and pumps on the retired list.

Rules: PL-M1 ("shall" becomes "must") and the federal page organize/place-the-main-idea-before-exceptions-and-conditions.md, which puts the main idea before exceptions. This is the long exception form, not the short "if" procedure form from pair 2. The checker cannot tell the two forms apart. It flags the sentence length and the "shall", and you judge the order.

## 5. Comparison section: prose to table

**Before:**

The standard van moves 8 cubic meters of cargo and holds 900 kilograms of payload. The long van moves 11 cubic meters of cargo and holds 1,100 kilograms of payload. Both vans need a service every 20,000 kilometers.

**After:**

| Attribute | Standard van | Long van |
|---|---|---|
| Cargo | 8 cubic meters | 11 cubic meters |
| Payload | 900 kilograms | 1,100 kilograms |
| Service | every 20,000 kilometers | every 20,000 kilometers |

Rules: the table rule (use a table for a comparison of two items on the same attributes). The checker will not flag this pair. The pair exists so you see the structure rule. Prose buries the comparison, and the table lines the attributes up.

## 6. Failure case: quoted statute

**Before (quoted material):**

> The grantee shall thereafter maintain, in perpetuity, such records as the Secretary may from time to time prescribe, and shall, upon the demand of any officer authorized by the Secretary, make the same available for inspection during ordinary business hours.

**After:**

Do not rewrite this. Plain language is the wrong tool for quoted statute text. The wording carries a fixed legal meaning, and a rewrite can change that meaning.

The wrong move looks like this: "Keep the records the Secretary asks for, and show them when an officer asks during normal work hours."

That version reads easier, but it narrows who may demand the records and it drops the perpetuity duty. This is the wrong move.

Rules: the scope rule (quoted material stays as written). The quote sits in a block quote, and the checker strips block quotes, so the quote produces no hit.

## 7. Jargon: one watch-list word

**Before (in a fence, for a reason):**

```
Utilize the backup lamp when the main lamp fails.
```

**After:**

Use the backup lamp when the main lamp fails.

Rules: PL-J1 (watch-list word). references/word-list.md maps the flagged word to "use". The before line sits in a fence. The prose gate flags that word outside fences. The checker strips fences, so the pair stays invisible to both tools, and the commentary still names the rule.

## 8. Paragraph cap: seven sentences in one paragraph

**Before:**

The gate is shut. The lamp is on. The log is full. The crew is ready. The road is clear. The load is light. The shift is over.

**After:**

The gate is shut. The lamp is on. The log is full. The crew is ready.

The road is clear. The load is light. The shift is over.

Rules: PL-P1 (paragraph cap: six sentences). Project cap, not a federal number. The checker errors at seven. The first after paragraph holds the site state, and the second holds the go signal.
