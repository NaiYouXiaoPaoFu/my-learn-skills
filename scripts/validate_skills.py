#!/usr/bin/env python3
"""Validate local learning skills for structure and workflow guardrails."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".agents" / "skills"
REQUIRED_SECTIONS = ["IRON LAW", "## 职责", "## 工作流", "## 输出格式", "## 反模式"]
MAX_SKILL_LINES = 120
MIN_DESCRIPTION_CHARS = 40


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, ["unterminated YAML frontmatter"]
    raw = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    extra = sorted(set(data) - {"name", "description"})
    if extra:
        errors.append(f"unexpected frontmatter keys: {', '.join(extra)}")
    return data, errors


def validate_skill(path: Path) -> list[str]:
    text = read(path)
    rel = path.relative_to(ROOT)
    errors: list[str] = []

    frontmatter, fm_errors = parse_frontmatter(text)
    errors.extend(f"{rel}: {err}" for err in fm_errors)

    name = frontmatter.get("name", "")
    desc = frontmatter.get("description", "")
    folder = path.parent.name
    if name != folder:
        errors.append(f"{rel}: frontmatter name '{name}' does not match folder '{folder}'")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        errors.append(f"{rel}: invalid skill name '{name}'")
    if len(desc) < MIN_DESCRIPTION_CHARS:
        errors.append(f"{rel}: description too short")

    lines = text.splitlines()
    if len(lines) > MAX_SKILL_LINES:
        errors.append(f"{rel}: too long ({len(lines)} lines > {MAX_SKILL_LINES})")

    for marker in REQUIRED_SECTIONS:
        if marker not in text:
            errors.append(f"{rel}: missing required marker '{marker}'")

    forbidden = ["TO" + "DO", "[TO" + "DO", "Structuring This " + "Skill", "place" + "holder"]
    for marker in forbidden:
        if marker in text:
            errors.append(f"{rel}: contains template marker '{marker}'")

    if "Skill Chain" in text and "Stop Condition" not in text:
        errors.append(f"{rel}: mentions Skill Chain without Stop Condition")

    return errors


def main() -> int:
    errors: list[str] = []
    if not SKILLS_DIR.exists():
        print(f"missing skills directory: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_files = sorted(p / "SKILL.md" for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != "references")
    if not skill_files:
        print("no skills found", file=sys.stderr)
        return 1

    for skill_file in skill_files:
        if not skill_file.exists():
            errors.append(f"{skill_file.relative_to(ROOT)}: missing SKILL.md")
            continue
        errors.extend(validate_skill(skill_file))

    required_refs = [
        "composition-recipes.md",
        "issue-pr-workflow.md",
        "learning-system-gate.md",
        "checkpoint-catalog.md",
        "documentation-layering.md",
        "interview-checkpoint-style.md",
        "repo-integration-workflow.md",
    ]
    for ref in required_refs:
        if not (SKILLS_DIR / "references" / ref).exists():
            errors.append(f".agents/skills/references/{ref}: missing required reference")

    if not (ROOT / "AGENTS.md").exists():
        errors.append("AGENTS.md: missing repository agent rules")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
