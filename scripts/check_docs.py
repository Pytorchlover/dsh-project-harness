#!/usr/bin/env python3
"""Check local Markdown link destinations. Not a semantic freshness checker.

Default scope: tracked root Markdown, docs/, .agents/notes/ and .agents/plans/.
Explicit files/directories include untracked Markdown. Code blocks, external URLs,
fragment-only links and template documents are skipped. Anchors are not checked.
"""
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+["\'][^\n]*?["\'])?\s*\)')
REFERENCE = re.compile(r'^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)', re.M)


def destinations(text: str):
    # Match ordinary inline links and reference definitions, not code examples.
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append('')
        elif fence is None:
            lines.append(line)
    text = re.sub(r'<!--.*?-->', '', '\n'.join(lines), flags=re.S)
    text = re.sub(r'(`+).*?\1', '', text)
    for pattern in (LINK, REFERENCE):
        for match in pattern.finditer(text):
            yield match.group(1).strip('<>')


def check(repo: Path, files: list[Path]) -> tuple[int, list[str]]:
    checked, errors = 0, []
    for path in files:
        try:
            text = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{path}: {exc}')
            continue
        for target in destinations(text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            # A leading slash denotes the repository root, not the host root.
            decoded = unquote(url.path)
            destination = (repo / decoded.lstrip('/')) if decoded.startswith('/') else path.parent / decoded
            checked += 1
            if not destination.exists():
                errors.append(f'{path.relative_to(repo)}: missing {target}')
    return checked, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    parser.add_argument('paths', nargs='*', help='Repository-relative Markdown files/directories')
    args = parser.parse_args()
    repo = args.repo.resolve()
    files = set()
    if args.paths:
        for value in args.paths:
            path = (repo / value).resolve()
            if not path.is_relative_to(repo) or not path.exists():
                parser.error(f'Path must exist inside repository: {value}')
            files.update(path.rglob('*.md') if path.is_dir() else [path])
    else:
        result = subprocess.run(['git', 'ls-files', '-z'], cwd=repo, capture_output=True, check=True)
        for value in result.stdout.decode().split('\0'):
            p = Path(value)
            if value and p.suffix.lower() == '.md' and (len(p.parts) == 1 or value.startswith(('docs/', '.agents/notes/', '.agents/plans/'))):
                files.add(repo / p)
    files = sorted(p for p in files if p.suffix.lower() == '.md' and 'template' not in p.name.lower())
    count, errors = check(repo, files)
    for error in errors:
        print(error)
    print(f'Doc links: {len(files)} files, {count} local destinations, {len(errors)} errors. Anchors and prose accuracy not checked.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
