#!/usr/bin/env python3
"""Create a non-destructive agent-harness baseline in a project repository."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


PLACEHOLDERS = (
    "PROJECT_NAME",
    "INSTALL_COMMAND",
    "BUILD_COMMAND",
    "LINT_COMMAND",
    "TYPECHECK_COMMAND",
    "TEST_COMMAND",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize layered AGENTS.md, change docs, and local workflow skills."
    )
    parser.add_argument("target", type=Path, help="Repository root to initialize")
    parser.add_argument("--project-name", help="Project name used in generated prose")
    parser.add_argument(
        "--dry-run", action="store_true", help="Report actions without writing files"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing destinations after backing them up under .agents/harness-backups/",
    )
    return parser.parse_args()


def git_root(target: Path) -> Path | None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=target,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip()).resolve()


def package_commands(target: Path) -> tuple[str | None, dict[str, str]]:
    package_json = target / "package.json"
    if not package_json.is_file():
        return None, {}
    try:
        package = json.loads(package_json.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        raise SystemExit(f"Cannot read {package_json}: {error}") from error

    scripts = package.get("scripts") if isinstance(package.get("scripts"), dict) else {}
    if (target / "pnpm-lock.yaml").exists():
        runner, install = "pnpm", "pnpm install"
    elif (target / "yarn.lock").exists():
        runner, install = "yarn", "yarn install"
    elif (target / "bun.lock").exists() or (target / "bun.lockb").exists():
        runner, install = "bun", "bun install"
    else:
        runner = "npm"
        install = "npm ci" if (target / "package-lock.json").exists() else "npm install"

    def command(*names: str) -> str | None:
        for name in names:
            if name in scripts:
                if runner == "yarn":
                    return f"yarn {name}"
                return f"{runner} run {name}"
        return None

    return package.get("name") if isinstance(package.get("name"), str) else None, {
        "INSTALL_COMMAND": install,
        "BUILD_COMMAND": command("build"),
        "LINT_COMMAND": command("lint", "check"),
        "TYPECHECK_COMMAND": command("typecheck", "type-check", "check:types"),
        "TEST_COMMAND": command("test", "test:unit"),
    }


def infer_values(target: Path, explicit_name: str | None) -> dict[str, str]:
    package_name, commands = package_commands(target)
    values: dict[str, str | None] = {
        "PROJECT_NAME": explicit_name or package_name or target.name,
        "INSTALL_COMMAND": commands.get("INSTALL_COMMAND"),
        "BUILD_COMMAND": commands.get("BUILD_COMMAND"),
        "LINT_COMMAND": commands.get("LINT_COMMAND"),
        "TYPECHECK_COMMAND": commands.get("TYPECHECK_COMMAND"),
        "TEST_COMMAND": commands.get("TEST_COMMAND"),
    }

    pyproject = target / "pyproject.toml"
    if pyproject.is_file() and not commands:
        text = pyproject.read_text(encoding="utf-8")
        values.update(
            {
                "INSTALL_COMMAND": "uv sync" if (target / "uv.lock").exists() else "python -m pip install -e '.[dev]'",
                "BUILD_COMMAND": "python -m build" if "[build-system]" in text else None,
                "LINT_COMMAND": "python -m ruff check ." if "ruff" in text else None,
                "TYPECHECK_COMMAND": "python -m mypy ." if "mypy" in text else None,
                "TEST_COMMAND": "python -m pytest" if "pytest" in text or (target / "tests").exists() else None,
            }
        )
    elif (target / "Cargo.toml").is_file() and not commands:
        values.update(
            {
                "INSTALL_COMMAND": "cargo fetch",
                "BUILD_COMMAND": "cargo build",
                "LINT_COMMAND": "cargo clippy --all-targets --all-features -- -D warnings",
                "TYPECHECK_COMMAND": "cargo check",
                "TEST_COMMAND": "cargo test",
            }
        )
    elif (target / "go.mod").is_file() and not commands:
        values.update(
            {
                "INSTALL_COMMAND": "go mod download",
                "BUILD_COMMAND": "go build ./...",
                "LINT_COMMAND": "go vet ./...",
                "TYPECHECK_COMMAND": "# Type checking is covered by go build and go test",
                "TEST_COMMAND": "go test ./...",
            }
        )

    for key in PLACEHOLDERS:
        if not values.get(key):
            label = key.removesuffix("_COMMAND").lower().replace("_", " ")
            values[key] = f"# TODO: define {label} command"
    return {key: str(value) for key, value in values.items()}


def render(source: Path, values: dict[str, str]) -> str:
    content = source.read_text(encoding="utf-8")
    for key, value in values.items():
        content = content.replace("{{" + key + "}}", value)
    return content


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        raise SystemExit(f"Target directory does not exist: {target}")

    resolved_git_root = git_root(target)
    if resolved_git_root is not None and resolved_git_root != target:
        raise SystemExit(
            f"Target is inside Git repository {resolved_git_root}; rerun against the actual repository root."
        )

    source_root = Path(__file__).resolve().parent.parent / "assets" / "project-harness"
    if not source_root.is_dir():
        raise SystemExit(f"Template directory is missing: {source_root}")

    values = infer_values(target, args.project_name)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = target / ".agents" / "harness-backups" / timestamp
    created = skipped = replaced = 0

    for source in sorted(path for path in source_root.rglob("*") if path.is_file()):
        relative = source.relative_to(source_root)
        destination = target / relative
        if destination.exists() and not args.overwrite:
            print(f"SKIP    {relative}")
            skipped += 1
            continue

        action = "CREATE"
        if destination.exists():
            backup = backup_root / relative
            print(f"BACKUP  {relative} -> {backup.relative_to(target)}")
            if not args.dry_run:
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination, backup)
            action = "REPLACE"

        print(f"{action:<7} {relative}")
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render(source, values), encoding="utf-8")
        if action == "CREATE":
            created += 1
        else:
            replaced += 1

    mode = "dry-run" if args.dry_run else "written"
    print(f"SUMMARY {mode}: created={created} replaced={replaced} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
