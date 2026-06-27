#!/usr/bin/env python3
"""Install JStack commands, skill, and MCP server into Codex."""

from __future__ import annotations

import argparse
import datetime as dt
import platform
import shutil
from pathlib import Path


PROMPTS = ("j-stack-dev.md", "jstack-subagents.md", "jstack-full-team.md")


def copytree_replace(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))


def archive_existing(path: Path, archive_root: Path) -> Path | None:
    if not path.exists():
        return None
    archive_root.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    target = archive_root / f"{path.name}-{stamp}"
    shutil.move(str(path), str(target))
    return target


def remove_existing_stack_blocks(config: str) -> str:
    lines = config.splitlines()
    output: list[str] = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if stripped in {"[mcp_servers.gstack]", "[mcp_servers.jstack]"}:
            skip = True
            continue
        if skip and stripped.startswith("[") and stripped not in {"[mcp_servers.gstack.env]", "[mcp_servers.jstack.env]"}:
            skip = False
        if skip:
            continue
        output.append(line)
    return "\n".join(output).rstrip() + "\n"


def mcp_block(install_dir: Path) -> str:
    is_windows = platform.system().lower().startswith("win")
    command = "python" if is_windows else "python3"
    gstack_root = Path.home() / ".gstack" / "repos" / "gstack"
    if is_windows:
        path = f"{gstack_root / 'bin'};C:/Windows/System32;C:/Windows;C:/Windows/System32/WindowsPowerShell/v1.0"
    else:
        path = f"{gstack_root / 'bin'}:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    server = (install_dir / "jstack_mcp_server.py").as_posix()
    return f"""
[mcp_servers.jstack]
command = "{command}"
args = ["{server}"]
startup_timeout_sec = 30.0
tool_timeout_sec = 300.0

[mcp_servers.jstack.env]
GSTACK_ROOT = "{gstack_root.as_posix()}"
PATH = "{path}"
""".strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--codex-home", default=str(Path.home() / ".codex"))
    args = parser.parse_args()

    repo_root = Path(args.repo_root).expanduser().resolve()
    codex_home = Path(args.codex_home).expanduser().resolve()
    if not repo_root.exists():
        raise SystemExit(f"Repo root not found: {repo_root}")

    prompts_dir = codex_home / "prompts"
    skills_root = codex_home / "skills"
    skill_dir = skills_root / "jstack-dev"
    mcp_root = codex_home / "mcp"
    mcp_dir = mcp_root / "jstack"
    config_path = codex_home / "config.toml"

    prompts_dir.mkdir(parents=True, exist_ok=True)
    skills_root.mkdir(parents=True, exist_ok=True)
    mcp_root.mkdir(parents=True, exist_ok=True)

    archived_prompt = archive_existing(prompts_dir / "gstack-dev.md", codex_home / "prompts-disabled")
    archived_skill = archive_existing(skills_root / "gstack-dev", codex_home / "skills-disabled")

    for prompt in PROMPTS:
        shutil.copy2(repo_root / "prompts" / prompt, prompts_dir / prompt)
    copytree_replace(repo_root / "skills" / "jstack-dev", skill_dir)
    copytree_replace(repo_root / "mcp" / "jstack", mcp_dir)

    if not config_path.exists():
        config_path.write_text("", encoding="utf-8")
    original = config_path.read_text(encoding="utf-8")
    backup = config_path.with_suffix(".toml.jstack-backup")
    backup.write_text(original, encoding="utf-8")
    updated = remove_existing_stack_blocks(original)
    updated = updated.rstrip() + "\n\n" + mcp_block(mcp_dir) + "\n"
    config_path.write_text(updated, encoding="utf-8")

    print("Installed JStack prompts:")
    for prompt in PROMPTS:
        print(f"  - {prompts_dir / prompt}")
    print(f"Installed jstack-dev skill to {skill_dir}")
    print(f"Installed JStack MCP to {mcp_dir}")
    print(f"Updated Codex config: {config_path}")
    print(f"Backup written: {backup}")
    if archived_prompt:
        print(f"Archived old /gstack-dev prompt: {archived_prompt}")
    if archived_skill:
        print(f"Archived old gstack-dev skill: {archived_skill}")
    print("Restart Codex or open a new thread for command and MCP changes to load.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
