#!/usr/bin/env python3
"""Check literal/format invariants in an editing run. Semantic review is separate."""
import argparse
import json
from pathlib import Path


def evaluate(cases, results):
    rows = results.get('results', results) if isinstance(results, dict) else results
    if not isinstance(rows, list):
        raise ValueError('results must be a list or an object containing a results list')
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != {c['id'] for c in cases}:
        raise ValueError('result IDs must match all case IDs exactly once')
    by_id = {r['id']: r for r in rows}
    report = []
    for case in cases:
        result = by_id[case['id']]
        text, notes = result.get('edited_text'), result.get('notes', [])
        checks, failures = case.get('checks', {}), []
        if not isinstance(notes, list) or not all(isinstance(n, str) for n in notes):
            raise ValueError(f'{case["id"]}: notes must be a string list')
        if checks.get('audit_only'):
            if text is not None:
                failures.append('audit-only returned edited prose')
            if not notes:
                failures.append('audit-only omitted findings')
        elif not isinstance(text, str):
            failures.append('missing edited_text string')
        else:
            if checks.get('unchanged') and text != case['text']:
                failures.append('already-good draft changed')
            failures.extend(f'lost protected literal: {s}' for s in checks.get('preserve_literals', []) if s not in text)
            failures.extend(f'introduced forbidden content: {s}' for s in checks.get('forbid_literals', []) if s in text)
        if checks.get('notes_required') and not notes:
            failures.append('factual concern not flagged')
        if checks.get('notes_empty') and notes:
            failures.append('draft-only contract included commentary')
        report.append({'id': case['id'], 'mechanical_pass': not failures, 'failures': failures})
    return {'cases': len(report), 'mechanical_passed': sum(r['mechanical_pass'] for r in report),
            'results': report, 'limitation': 'Literal/format checks do not prove meaning preservation or style quality. Inspect every case against its semantic rubric.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cases', type=Path)
    parser.add_argument('results', type=Path)
    args = parser.parse_args()
    report = evaluate(json.loads(args.cases.read_text()), json.loads(args.results.read_text()))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report['mechanical_passed'] == report['cases'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
