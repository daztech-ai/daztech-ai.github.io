#!/usr/bin/env python3
"""Scan ledgers/ directory and generate ledger_manifest.json + all_ledgers.json.

Run this every time new paper trade JSON files are added to ledgers/.
The track-record.html dashboard reads ledger_manifest.json to discover files.

Usage:
  python3 build_ledger_manifest.py                     # generate both files
  python3 build_ledger_manifest.py --manifest-only     # only ledger_manifest.json
  python3 build_ledger_manifest.py --merge-only        # only all_ledgers.json
"""

import json
import os
import sys
from pathlib import Path

LEDGERS_DIR = Path(__file__).resolve().parent if '__file__' in dir() else Path('/home/daz/daztech-betting-engine/output/ledgers')


def find_ledger_files(ledgers_dir: Path) -> list[str]:
    """Return sorted list of .json filenames (excluding manifest/merged files)."""
    exclude = {'ledger_manifest.json', 'all_ledgers.json'}
    files = sorted(
        f.name for f in ledgers_dir.glob('*.json')
        if f.name not in exclude and not f.name.startswith('.')
    )
    return files


def normalize_picks(raw_picks: list, source_file: str) -> list[dict]:
    """Ensure all picks have the standard fields for the dashboard."""
    out = []
    for p in raw_picks:
        item = dict(p)
        if '_source' not in item:
            item['_source'] = source_file
        out.append(item)
    return out


def generate_manifest(ledgers_dir: Path) -> list[str]:
    files = find_ledger_files(ledgers_dir)
    manifest_path = ledgers_dir / 'ledger_manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(files, f, indent=2)
    print(f'  ledger_manifest.json → {len(files)} files indexed')
    return files


def generate_merged(ledgers_dir: Path, files: list[str]):
    all_picks = []
    for fname in files:
        fpath = ledgers_dir / fname
        try:
            with open(fpath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f'  WARNING: Skipping {fname}: {e}')
            continue
        picks = data if isinstance(data, list) else [data]
        all_picks.extend(normalize_picks(picks, fname))
        print(f'  {fname}: {len(picks)} picks')

    merged_path = ledgers_dir / 'all_ledgers.json'
    with open(merged_path, 'w') as f:
        json.dump(all_picks, f)
    print(f'  all_ledgers.json → {len(all_picks)} total picks merged')


def main():
    ledgers_dir = LEDGERS_DIR
    if not ledgers_dir.exists():
        print(f'ERROR: ledgers/ directory not found at {ledgers_dir}')
        sys.exit(1)

    args = set(sys.argv[1:])
    manifest_only = '--manifest-only' in args
    merge_only = '--merge-only' in args
    do_both = not manifest_only and not merge_only

    print(f'Scanning {ledgers_dir}/')
    files = find_ledger_files(ledgers_dir)

    if do_both or manifest_only:
        generate_manifest(ledgers_dir)

    if do_both or merge_only:
        if not files:
            print('  No ledger JSON files found.')
            return
        generate_merged(ledgers_dir, files)

    print('Done.')


if __name__ == '__main__':
    main()
