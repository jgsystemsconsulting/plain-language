---
name: plain-language
description: Writes and rewrites text in plain language and checks it with scripts/plain_check.py. Use when the user asks for plain language, a plain rewrite, or a check against the Federal Plain Language Guidelines.
license: MIT
source-specification: Federal Plain Language Guidelines (plainlanguage.gov, via the GSA GitHub archive) and ISO 24495-1:2023 Part 1, cited by number
---

# Plain Language

This skill writes and rewrites text in plain language.
The source is the US Federal Plain Language Guidelines.
They are a work of the US government, so they are in the public domain.
The standard ISO 24495-1:2023 is cited by number only.
This skill tracks Part 1 of that standard only.
This skill is not a PLAIN document and not an ISO document.
It does not certify compliance with either source.
See NOTICE.md for attribution.

Federal pages are cited by path.
The base address is https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/.
Each path in this file is relative to that address.

## Scope

Apply plain language to: documentation, policy text, instructions, and reports.

Do not apply it to:

- Poetry, fiction, and marketing copy
- Code, identifiers, commands, and file paths
- Quoted material.

If the user asks for a different style, the user wins.

## Step 1: Classify the text

Before you write, classify each paragraph:

- **Procedure** tells the reader to do something. Write it in the imperative, and keep an article before the noun. Cap: 20 words per sentence.
- **Information** tells the reader a fact. Write it in active voice and a simple tense. Write "you" when a person must act. Cap: 25 words per sentence.

If the user does not name a type, use information.
Do not mix the two types in one paragraph.

Project cap, not a federal number.

## Step 2: Obey the verb rules

- Use the active voice (`conversational/use-active-voice.md`).
- Use the present tense (`conversational/use-the-present-tense.md`).
- Address the reader as "you" or "we" (`audience/address-the-user.md`).
- Write "must", not "shall" (`conversational/shall-and-must.md`).
- Contractions are allowed (`conversational/use-contractions.md`).

The checker still flags a passive when the law is the actor.
You decide whether such a hit is a real error.

## Step 3: Obey the sentence rules

- Write one idea per sentence (`concise/write-short-sentences.md`).
- Keep each sentence at or under the cap: 20 words in a procedure, 25 words in information.
- Put the condition before the command, and put a comma after the condition. "If the light comes on, stop the engine."

Project cap, not a federal number.

The federal page `organize/place-the-main-idea-before-exceptions-and-conditions.md` rejects a long "except" clause before the rule.
A short "if" before a command is a different form.
The checker does not tell them apart.

## Step 4: Obey the word rules

- Choose the everyday word first (`words/use-simple-words-phrases.md`).
- Do not hide a verb in a noun (`words/avoid-hidden-verbs.md`). Write "decide", not "make a decision".
- Break a noun string of four or more words (`words/avoid-noun-strings.md`). You judge these hits. The checker implements no noun-string rule.
- Use one term for one thing, and use it the same way every time (`words/use-the-same-terms-consistently.md`, `words/minimize-definitions.md`). You judge these hits too.
- Avoid jargon (`words/avoid-jargon.md`). Check each suspect word against the finite list in `references/word-list.md`.

## Step 5: Structure the text

- Write headings that say what the section contains (`organize/add-useful-headings.md`).
- Use a list for steps and options (`organize/use-lists.md`).
- Use a table for a comparison (`design/use-tables-to-make-complex-material-easier-to-understand.md`).
- Put one topic in each paragraph, and keep each paragraph to six sentences or fewer.

Project cap, not a federal number.

The federal guidance suggests a paragraph of up to 150 words and a section of up to 250 words.
Use those numbers as writer guidance.
The checker does not count words in a paragraph.

## Step 6: Check your text

After you write, check your text. Do these steps:

1. If you can run scripts, run the checker. The output prints an ERROR line for each error, a WARNING line for each warning, and a final Result line.

```
python scripts/plain_check.py --mode procedure <file>
python scripts/plain_check.py --mode information <file>
```

2. If you cannot run scripts, do a manual scan. Look for a semicolon that joins two ideas, a "be" verb plus a participle, "shall", hidden verbs, sentences over the cap, paragraphs over six sentences, and watch-list words.
3. Fix each error. Read each warning, then fix it or say why it stays.
4. Run the check again. Stop when there are no errors.

The tool has limits:

```
The check tool cannot find all the errors.
The tool cannot know if a word means what the reader needs.
You must also compare your words with references/word-list.md.
```

## Step 7: Work with other checks

Plain language owns structure, voice, and vocabulary.
The avoid-ai-writing skill owns AI tells: em dashes, Tier-1 vocabulary, and hollow intensifiers.
When both skills name the same word, either fix is fine.
Do not merge the two checkers.
Durable prose in a repository must also pass `python ~/.zcode/scripts/prose_check.py`.

## Reference files

- `references/rules.md`: the full rule set, with a before-and-after pair for each rule.
- `references/word-list.md`: simple-first substitutions and the jargon watch list.
- `references/reading-level.md`: the reading-level formulas and their limits.
- `examples/before-after.md`: worked examples of text before and after a rewrite.

## Basis

A document is plain when readers get what they need (relevant), can find it (findable), can understand it (understandable), and can use it (usable).
That sentence paraphrases the four principles of ISO 24495-1:2023.
The wording follows the public IPLF paraphrase, not the ISO text.
The federal guidelines name the same goals as find, understand, and use.
