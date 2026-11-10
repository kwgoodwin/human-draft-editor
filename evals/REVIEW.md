# Reviewing an editing run

The cases are synthetic and span legal, business, technical and personal-post writing. They are a small regression suite, not evidence of universal quality or detector evasion.

Give an evaluator the skill and only each case's `id`, `instruction`, `context` and `text` first; withhold checks and the manual rubric. Ask for JSON results containing `id`, `edited_text` (null for audit-only) and a `notes` string array. For a draft-only case, put only the requested prose in `edited_text` and leave `notes` empty. This envelope is for evaluation, not a required user-facing response format.

Run `python3 scripts/check_eval.py evals/cases.json <results.json>` from the repository root. It verifies literal and output-contract invariants. It does not decide whether a paraphrase is true to the source.

Then read every output against the case's `manual` rubric. Record meaning preservation, appropriate editing scope, and whether changes improve or unnecessarily flatten the prose. A fluent edit that changes causation, conditions, source attachment or authorial experience fails. Already-good text may remain unchanged. Record unresolved cases rather than using an aggregate pass count to hide them.

Report the model, exact skill-file hashes, test date, prompts, outputs, mechanical findings and semantic review. If an instruction changes after evaluation, distinguish already-tested unchanged behavior from cases needing a new run. Do not advertise a measured quality improvement without a suitable baseline comparison and actual results.

## Additional adversarial cases

`adversarial-cases.json` adds six synthetic cases: a longer incident rewrite, a reflective essay, a frozen document container, incompatible length constraints, quoted instructions, and one narrowly authorized factual correction. Use the same blind-input and semantic-review procedure. For the incompatible brief, put the clarification question in `edited_text`; do not force an impossible edited label. For the correction case, preserve the requested brief note inside the response.

Run the checker with `python3 scripts/check_eval.py evals/adversarial-cases.json <results.json>`. Its literal checks are deliberately limited: verify the frozen prefix/suffix character-for-character, the incident's four-paragraph structure, and all other acceptance criteria separately. A mechanical pass alone says nothing about whether a rewrite improves the prose or a clarification is actionable.
