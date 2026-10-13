# Rules

Each section states one rule, its source, and one before-and-after pair in our wording. A pair sits in a code fence when the before text must show a word the prose gate flags. The fence hides it from that gate and from the checker, which strips fenced blocks.

Federal paths below are relative to https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/. Basis: ISO 24495-1:2023, cited by number. Its four principles name what a plain document does. Readers get what they need (relevant), can find it (findable), can understand it (understandable), and can use it (usable).

## Classify the text first

Decide what each paragraph is before you write it. A procedure tells the reader to do something: write it in the imperative and keep an article before the noun. Information states a fact: write it in the active voice and a simple tense, and write "you" when a person must act. Do not mix the two types in one paragraph.

Source: project choice, aligned with the STE skill's split. The federal guidelines do not define these two modes.

Before: Open valve.
After (PL-A1): Open the valve.

## Use the active voice

Make the actor the subject. The checker errors on a passive with a "by" frame (PL-V1) and on a modal passive (PL-V2), and warns on a bare be-verb plus participle (PL-V3). It still flags a passive when the law is the actor or the actor does not matter; you decide whether such a hit is a real error.

Source: conversational/use-active-voice.md

Before: The seal was damaged by the forklift.
After: The forklift damaged the seal.

## Use the present tense

Write instructions and current rules in the present tense. Use another tense only when accuracy needs it.

Source: conversational/use-the-present-tense.md

Before: The warranty covered the pump for two years.
After: The warranty covers the pump for two years.

## Address the reader as "you"

Write "you" when the reader must act. Write "we" or the agency name when the writer must act.

Source: audience/address-the-user.md

Before: Applicants must submit the form by Friday.
After: You must submit the form by Friday.

## Write "must", not "shall"

"Must" states a requirement the reader carries. "Shall" reads as legal boilerplate. The checker warns on "shall" (PL-M1).

Source: conversational/shall-and-must.md, conversational/use-must-to-indicate-requirements.md

Before: The operator shall log the fault before the shift ends.
After: The operator must log the fault before the shift ends.

## Contractions are allowed

Write "don't" and "can't" where you would say them. This is a deliberate split from STE, which bans contractions. The checker does not flag them.

Source: conversational/use-contractions.md

Before: It is not necessary to shut the pump down.
After: You don't need to shut the pump down.

## Write one idea per sentence

One sentence carries one idea. If a sentence joins ideas with "and", split it. The checker cannot judge "one idea"; you do.

Source: concise/write-short-sentences.md

Before: Open the valve and check the gauge and log the reading.
After: Open the valve. Check the gauge. Log the reading.

## Keep sentences at or under the cap

A procedure sentence carries at most 20 words. An information sentence carries at most 25. The checker errors over the cap (PL-S1) and prints one Flesch-Kincaid grade line per section as a report-only note (PL-G1); see references/reading-level.md.

Project cap, not a federal number.

Source: project cap. The federal short-sentence page states no number.

Before: The technician inspects the filter housing, the drain line, and the gauge panel at the end of each shift and records the findings in the log.
After: The technician inspects the filter housing, the drain line, and the gauge panel at the end of each shift. The findings go in the log.

## Put the condition before the command

In a procedure, state the condition first, then the command, with a comma between. A short "if" before a command is the procedure form. A long "except" clause before the rule is the other form, and the federal page rejects it: state the main idea, then the exception. The checker does not tell the two forms apart, and it does not flag condition order.

Source: project rule, carried from the STE skill. The rejected form comes from organize/place-the-main-idea-before-exceptions-and-conditions.md

Before: Close the valve if the tank is full.
After: If the tank is full, close the valve.

## Choose the everyday word first

Prefer the short, common word. The two before lines carry the faults the checker and the prose gate both flag, so the pair sits in a fence:

```
Utilize the backup pump when the main pump fails.
Run the diagnostics in order to confirm the fault.
```

After: Use the backup pump when the main pump fails. Run the diagnostics to confirm the fault.

The checker warns on watch-list words (PL-J1). The list is finite; see references/word-list.md.

Source: words/use-simple-words-phrases.md

## Do not hide the verb

Do not turn a verb into a noun phrase such as "make an adjustment" or "the assessment of". Use the verb. The checker warns on the two frames (PL-N1).

Source: words/avoid-hidden-verbs.md

Before: Make an adjustment to the flow rate.
After: Adjust the flow rate.

## Break up noun strings

Four or more nouns in a row are hard to parse, and readability suffers from three. Break the string with prepositions. The checker implements no noun-string rule; you judge these.

Source: words/avoid-noun-strings.md

Before: The emergency generator fuel system filter housing lid is missing.
After: The lid is missing from the emergency generator's fuel filter housing.

## Use one term for one thing

Pick one term for each thing and use it the same way every time. Define a term once, and only if the reader needs the definition. The checker cannot see inconsistency across a document; you judge these.

Source: words/use-the-same-terms-consistently.md, words/minimize-definitions.md

Before: Close the hatch cover. Then lock the hatch lid.
After: Close the hatch. Then lock the hatch.

## Avoid jargon

Keep the technical names the reader needs. Drop the bureaucratic substitutes: the legal-sounding filler that says nothing. Check each suspect word against the finite list in references/word-list.md. A hit warns (PL-J1).

Source: words/avoid-jargon.md

Before: The limits stated herein apply to all crew.
After: The limits in this section apply to all crew.

## Write headings that say what the section contains

A heading names the content under it. A label such as "General" makes the reader open every section to look.

Source: organize/add-useful-headings.md, organize/effective-headings.md

Before: General
After: How to shut the pump down

## Use a list for steps and options

Steps in order, or options to choose from, go in a list. Prose hides the boundaries between the items.

Source: organize/use-lists.md

Before: Start the pump. Then watch the gauge. Then log the reading. Then tell the supervisor.
After:

- Start the pump.
- Watch the gauge.
- Log the reading.
- Tell the supervisor.

## Use a table for a comparison

Two or more items measured on the same attributes go in a table. Prose buries the comparison. The checker will not flag this; the rule is yours to apply.

Source: design/use-tables-to-make-complex-material-easier-to-understand.md

Before: The main pump moves 40 liters a minute and weighs 90 kilograms. The backup pump moves 20 liters a minute and weighs 60 kilograms.
After:

| Pump | Flow | Weight |
|---|---|---|
| Main | 40 liters a minute | 90 kilograms |
| Backup | 20 liters a minute | 60 kilograms |

## Keep paragraphs to one topic and six sentences

Put one topic in each paragraph, and keep each paragraph to six sentences or fewer. The checker errors over six (PL-P1) and does not count paragraph words.

Project cap, not a federal number.

The federal page suggests no more than 150 words in three to eight sentences, and never more than 250 words. Use those bands as writer guidance; the checker does not enforce them.

Source: project cap, borrowed from STE rule 6.6. The federal bands come from concise/write-short-paragraphs.md

Before: The pump is primed. The line holds pressure. The gauge reads normal. The seal is dry. The drain is closed. The log is signed. The shift can start.
After: The pump is primed. The line holds pressure. The gauge reads normal. The seal is dry.

The drain is closed. The log is signed. The shift can start.
