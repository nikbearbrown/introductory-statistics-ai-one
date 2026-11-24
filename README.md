# Introductory Statistics (AI Plus One)

**Compact first draft.** Five chapters, worked calculations, short practice sets and a capstone for first college statistics readers. Basic algebra, fractions and table reading are enough. This is not a finished textbook, an expert-reviewed edition, or a replacement for an existing book.

Follow a result from its question through its denominators, measurements and assumptions. An estimate can be arithmetically right and still unusable for the decision. The recurring examples use invented bus-arrival records; they are not observations or recommendations about a real transit system.

## Learning outcomes

After working through this draft, readers should be able to:

- Identify what a dataset can represent and summarize it with appropriate denominators, displays, and measures.
- Explain what sampling variation and assumptions mean for an inference.
- Distinguish an observed relationship from a causal claim and defend a conclusion with checked evidence.

## Chapters

1. [Ask what the data can represent](chapters/01-representation.md)
2. [Summarize without hiding variation](chapters/02-description.md)
3. [Use sampling variation](chapters/03-sampling-variation.md)
4. [Estimate and test with uncertainty](chapters/04-inference.md)
5. [Model relationships carefully](chapters/05-relationships.md)
6. [Unaided capstone and worksheet](practice/capstone.md)

Write down a first attempt before consulting an assistant. An optional critique uses only synthetic data, one proposed calculation or claim, and an independent check. The book does not require an AI account, a programming language or a live data feed. Use paper or a spreadsheet for the work; optional Python 3.10+ checks use only its standard library.

```sh
python3 -B -m lab.check_examples
python3 -B -m unittest discover -s tests -v
```

The code recalculates small printed examples, including distribution counts and exact randomization probabilities. It does not validate real sampling frames, estimate a treatment effect from an observational spreadsheet, or replace the learner's capstone. A fuller edition could add continuous probability models, categorical inference, ANOVA and additional regression diagnostics without pretending those topics are already taught in depth here.
