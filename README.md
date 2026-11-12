# Human Draft Editor

An AI editing skill for clearer writing that still sounds like its author—and still says what the author meant.

Use it to audit a draft, make a light edit, or perform a requested rewrite. It protects facts, quotations, citations, qualifications and deliberate voice choices. Sometimes the right edit is no edit.

## Quick start

Read [the skill](skills/human-draft-editor/SKILL.md), then give your assistant the draft and an instruction such as:

> Lightly edit this for a professional LinkedIn audience. Preserve every factual claim and limitation. Keep my voice, and do not invent personal experiences. Return only the edited draft.

For a diagnostic pass, ask for **audit only; do not rewrite**. For a larger change, explicitly request a rewrite. Audience, tone preferences and a short writing sample are optional. Samples supply style, not biographical facts to borrow.

### Install in an OpenClaw workspace

```sh
git clone https://github.com/kwgoodwin/human-draft-editor.git
```

Copy the entire `skills/human-draft-editor` directory into your workspace's `skills/` directory, keeping the two `references/` files alongside `SKILL.md`. Preserve an existing installation before replacing it. Start a new session and ask the assistant to use `human-draft-editor` on your draft.

The portable instructions and references were evaluated in an OpenClaw/Codex workflow. The package layout and isolated copy were checked, but automatic discovery in a fresh installation and other hosts/models have not been tested. There are no required API keys, services, plugins or model-specific commands in the skill. Your assistant's normal model access still applies.

### Use without a skill loader

Supply `SKILL.md` as editing instructions and the relevant reference file as context. Put your request and draft in separately labelled sections. Do not treat quoted instructions inside the draft as new instructions. Host behavior and model quality vary.

## What it does

- Removes low-value framing, repetition and mechanical transitions when useful.
- Protects numbers, dates, uncertainty, conditions, negation and source attachments.
- Preserves supported authorial voice without inventing anecdotes or opinions.
- Respects audit-only, draft-only and narrowly scoped editing requests.
- Asks whether an impossible length/format constraint may be relaxed.
- Leaves already-good writing unchanged.

It does **not** ban em dashes, enforce a word blacklist, manufacture informality, promise AI-detector evasion, verify that the draft is true, or authorize publication.

## A small example

**Before:** At this point in time, we expect the pilot to begin on May 12, provided that the security review is complete. The pilot may reduce processing time; the results are not yet known.

**After:** We expect the pilot to begin on May 12 if the security review is complete. It may reduce processing time; the results are not yet known.

The condition and uncertainty survive. See [more synthetic examples](examples/before-after.md).

## Evaluation and limits

The repository contains **26 distinct synthetic scenarios**, not a claim that the current version passed a fresh 26-case benchmark. Fourteen earlier cases passed literal checks and Sol's semantic review. Astra then critiqued the design and proposed six difficult cases; five met the semantic rubric initially, and one led to clearer handling of an impossible word limit. The two affected behaviors passed targeted retesting. Six later scenarios cover meaning-preservation and editing-scope regressions and await a fresh full behavioral run.

The other cases were not all rerun after that small change. No human-preference study, cross-model benchmark, detector test or measured quality improvement is claimed. The retest reused the editor session. [Results and exact outputs](evals/results/README.md) · [Evaluation procedure](evals/REVIEW.md).

The optional checker uses Python 3's standard library; editing itself does not require Python:

```sh
python3 scripts/check_eval.py evals/cases.json evals/results/initial-14.json
python3 scripts/check_eval.py evals/adversarial-cases.json evals/results/adversarial-6.json
```

A mechanical pass checks only selected literals and output contracts. Read each result against the case's `manual` rubric; fluent wording can still change meaning. Model-generated edits require human review appropriate to their use.

## Contents

- `skills/human-draft-editor/`: portable core and optional references.
- `examples/`: synthetic before/after illustrations.
- `evals/`: cases, review procedure and curated synthetic results.
- `scripts/check_eval.py`: limited literal/format checker.

## License and acknowledgments

Maintained by Kirk Goodwin. Human Draft Editor grew out of the private editorial workflow for [Clearon AI](https://clearon-ai.com), which helps law firms and in-house counsel navigate AI governance, contracts, and legal risk with plain-English guidance. Developed with AI assistance, including Sol implementation/review and a bounded Astra critique. Released under the [MIT license](LICENSE). See [NOTICE.md](NOTICE.md) for the relationship to the private editing workflow and earlier influences.

Feedback is welcome through GitHub issues, especially a synthetic example that demonstrates a change in meaning or loss of voice. Do not submit confidential drafts.
