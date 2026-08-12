#!/usr/bin/env python3
"""Analyze and safely integrate this learning-skill kit into another repository."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".agents" / "skills"
INTEGRATION_REPORT = Path("docs") / "learning-skill-integration-plan.md"

CORE_FILES = [
    (ROOT / "scripts" / "validate_skills.py", Path("scripts") / "validate_skills.py"),
]
OPTIONAL_DIRS = [
    (ROOT / "docs" / "templates", Path("docs") / "templates"),
    (ROOT / "docs" / "research", Path("docs") / "research"),
]
AGENT_RULES_BLOCK = """<!-- learning-skills:start -->

## Learning Skills Integration

- Learning, teaching, review, issue/PR intake, and project-deep-dive tasks should route through `.agents/skills/learn-orchestrator` unless a narrower existing project skill is explicitly better.
- Pasted issue/PR/review content should be treated as internal precise context via `issue-pr-intake`; do not restate full issue/PR bodies to the user.
- Teaching must not assume unverified prior knowledge; use `concept-teacher` before `learning-checkpoint` when prerequisites are unclear.
- Checkpoints may use interview-style follow-ups, but stop after at most two follow-up rounds and return to teaching if the user is stuck.
- Learning notes should record the project scene, knowledge point, user gap, correction, mastery state, and concrete external links actually used.

<!-- learning-skills:end -->
"""

CJK_KEYWORDS = {
    "学习", "教学", "检验", "追问", "面试", "上下文", "issue", "pr", "review",
    "架构", "设计", "代码", "链路", "回写", "文档", "资料", "来源", "概念",
    "项目", "拆解", "规则", "编排", "同步", "集成", "合并",
    "审核", "纠偏", "改法", "问题", "原因", "风险", "验证", "边界",
}

CATEGORY_KEYWORDS = {
    "teaching": {"mentor", "teacher", "concept-teacher", "教学", "引导", "概念教学"},
    "review": {"review", "review-coach", "blog-review", "代码审核", "审核"},
    "checkpoint": {"checkpoint", "blog-checkpoint", "learning-checkpoint", "讲后检验", "理解确认"},
    "issue-intake": {"issue-pr-intake", "pasted issue", "pr link", "review comments", "粘贴 issue", "精准上下文"},
    "context": {"learn-context", "上下文装载", "collect context", "prepare learning context"},
    "architecture": {"architecture-lens", "architecture", "架构", "分层边界"},
    "trace": {"code-path-tracer", "trace", "tracer", "执行链路", "链路追踪"},
    "note": {"learning-note-writer", "学习笔记", "学习结论", "回写", "阶段总结"},
    "source": {"source-researcher", "来源链接", "官方资料", "查证"},
    "orchestration": {"learn-orchestrator", "orchestrator", "学习流程路由", "编排"},
    "integration": {"repo-skill-integrator", "sync_to_repo", "同步", "集成合并"},
}

PRIMARY_CATEGORY_BY_NAME = {
    "blog-mentor": "teaching",
    "concept-teacher": "teaching",
    "blog-review": "review",
    "review-coach": "review",
    "gh-pr-comments": "review",
    "blog-checkpoint": "checkpoint",
    "learning-checkpoint": "checkpoint",
    "issue-pr-intake": "issue-intake",
    "learn-context": "context",
    "architecture-lens": "architecture",
    "code-path-tracer": "trace",
    "learning-note-writer": "note",
    "source-researcher": "source",
    "learn-orchestrator": "orchestration",
    "project-deep-dive": "deep-dive",
    "repo-skill-integrator": "integration",
    "openspec-propose": "openspec",
    "openspec-apply-change": "openspec",
    "openspec-archive-change": "openspec",
    "openspec-explore": "openspec",
}

GENERIC_TOKENS = {
    "use", "when", "user", "asks", "actions", "skill", "skills", "repo", "repository",
    "project", "target", "source", "workflow", "description", "with", "from", "this", "that",
    "用于", "项目", "用户", "任务", "规则", "当前", "需要", "使用", "输出", "读取",
}

KEY_SECTIONS = ["IRON LAW", "## 职责", "## 工作流", "## 输出格式", "## 反模式"]


@dataclass(frozen=True)
class SkillMeta:
    name: str
    path: Path
    description: str
    tokens: frozenset[str]
    categories: frozenset[str]
    primary_category: str
    key_content: str
    purpose_excerpt: str
    workflow_excerpt: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan a repo and safely integrate missing learning skills without overwriting local rules."
    )
    parser.add_argument("target_repo", help="Path to the repository that should receive or merge learning skills.")
    parser.add_argument("--apply", action="store_true", help="Copy missing items and write an integration report.")
    parser.add_argument("--include-research", action="store_true", help="Also copy docs/research if absent.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="ignore")


def parse_frontmatter(path: Path) -> tuple[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        return path.parent.name, ""
    end = text.find("\n---\n", 4)
    if end == -1:
        return path.parent.name, ""
    name = path.parent.name
    description = ""
    for line in text[4:end].splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("description:"):
            description = line.split(":", 1)[1].strip().strip('"')
    return name, description


def extract_section(text: str, marker: str) -> str:
    if marker == "IRON LAW":
        match = re.search(r"^IRON LAW:\s*(.+)$", text, flags=re.MULTILINE)
        return match.group(1).strip() if match else ""
    start = text.find(marker)
    if start == -1:
        return ""
    start = text.find("\n", start)
    if start == -1:
        return ""
    next_heading = re.search(r"\n## ", text[start + 1 :])
    end = start + 1 + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def compact(text: str, limit: int = 180) -> str:
    line = re.sub(r"\s+", " ", text).strip()
    if len(line) <= limit:
        return line
    return line[: limit - 3].rstrip() + "..."


def key_content_from_skill(text: str, description: str) -> str:
    sections = [description]
    for marker in KEY_SECTIONS:
        value = extract_section(text, marker)
        if value:
            sections.append(value)
    return "\n".join(sections)


def tokenize(text: str) -> frozenset[str]:
    raw = set(re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", text.lower()))
    parts: set[str] = set()
    for token in raw:
        parts.add(token)
        parts.update(part for part in re.split(r"[-_]", token) if len(part) > 2)
    for keyword in CJK_KEYWORDS:
        if keyword.lower() in text.lower():
            parts.add(keyword.lower())
    return frozenset(part for part in parts if part not in GENERIC_TOKENS)


def categorize(text: str) -> frozenset[str]:
    text_lower = text.lower()
    categories: set[str] = set()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword.lower() in text_lower for keyword in keywords):
            categories.add(category)
    return frozenset(categories)


def primary_category(name: str, categories: frozenset[str]) -> str:
    if name in PRIMARY_CATEGORY_BY_NAME:
        return PRIMARY_CATEGORY_BY_NAME[name]
    if len(categories) == 1:
        return next(iter(categories))
    return ""


def load_skills(root: Path) -> list[SkillMeta]:
    skills_root = root / ".agents" / "skills"
    if not skills_root.exists():
        return []
    skills: list[SkillMeta] = []
    for directory in sorted(p for p in skills_root.iterdir() if p.is_dir() and p.name != "references"):
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            continue
        name, description = parse_frontmatter(skill_file)
        file_text = read_text(skill_file)
        content = key_content_from_skill(file_text, description)
        categories = categorize(f"{name} {content}")
        skills.append(
            SkillMeta(
                name=name,
                path=directory,
                description=description,
                tokens=tokenize(content),
                categories=categories,
                primary_category=primary_category(name, categories),
                key_content=content,
                purpose_excerpt=compact(extract_section(file_text, "## 职责") or description),
                workflow_excerpt=compact(extract_section(file_text, "## 工作流")),
            )
        )
    return skills


def similarity(a: SkillMeta, b: SkillMeta) -> float:
    if not a.tokens or not b.tokens:
        return 0.0
    intersection = len(a.tokens & b.tokens)
    union = len(a.tokens | b.tokens)
    return intersection / union if union else 0.0


def shared_terms(a: SkillMeta, b: SkillMeta, limit: int = 8) -> list[str]:
    return sorted(a.tokens & b.tokens, key=lambda value: (len(value), value), reverse=True)[:limit]


def overlap_score(a: SkillMeta, b: SkillMeta) -> float:
    content_score = similarity(a, b)
    # Same category is only a weak hint; content overlap still has to exist.
    if a.primary_category and a.primary_category == b.primary_category:
        return max(content_score, 0.35)
    return content_score


def ensure_sources() -> list[str]:
    missing: list[str] = []
    if not SKILLS_DIR.exists():
        missing.append(".agents/skills")
    for source, _ in CORE_FILES:
        if not source.exists():
            missing.append(str(source.relative_to(ROOT)))
    return missing


def skill_plan(source_skills: list[SkillMeta], target_skills: list[SkillMeta]) -> tuple[list[SkillMeta], list[tuple[SkillMeta, SkillMeta, str]], list[tuple[SkillMeta, SkillMeta, float]]]:
    target_by_name = {skill.name: skill for skill in target_skills}
    missing: list[SkillMeta] = []
    same_name: list[tuple[SkillMeta, SkillMeta, str]] = []
    similar: list[tuple[SkillMeta, SkillMeta, float]] = []

    for source in source_skills:
        target = target_by_name.get(source.name)
        if target:
            same_name.append((source, target, "same skill name"))
            continue
        overlaps = [(target_skill, overlap_score(source, target_skill)) for target_skill in target_skills]
        overlaps = [(target_skill, score) for target_skill, score in overlaps if score >= 0.22]
        if overlaps:
            target_skill, score = sorted(overlaps, key=lambda item: item[1], reverse=True)[0]
            similar.append((source, target_skill, score))
        else:
            missing.append(source)
    return missing, same_name, similar


def merge_block_present(agent_text: str) -> bool:
    return "<!-- learning-skills:start -->" in agent_text and "<!-- learning-skills:end -->" in agent_text


def copy_dir(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def report_lines(target: Path, missing: list[SkillMeta], same_name: list[tuple[SkillMeta, SkillMeta, str]], similar: list[tuple[SkillMeta, SkillMeta, float]], agent_exists: bool, agent_has_block: bool) -> list[str]:
    lines = [
        "# Learning Skill Integration Plan",
        "",
        f"Target repo: `{target}`",
        "",
        "## Summary",
        "",
        f"- Missing learning skills that can be copied safely: {len(missing)}",
        f"- Same-name skill conflicts that need manual review: {len(same_name)}",
        f"- Potentially similar skills that need synthesis: {len(similar)}",
        f"- Existing `AGENTS.md`: {'yes' if agent_exists else 'no'}",
        f"- Learning integration block present: {'yes' if agent_has_block else 'no'}",
        "",
        "## Missing Skills",
        "",
    ]
    if missing:
        lines.extend(f"- `{skill.name}`" for skill in missing)
    else:
        lines.append("- None")
    lines.extend(["", "## Same-Name Conflicts", ""])
    if same_name:
        lines.extend(f"- `{source.name}`: source `{source.path.relative_to(ROOT)}` vs target `{target_skill.path}`" for source, target_skill, _ in same_name)
    else:
        lines.append("- None")
    lines.extend(["", "## Potential Similar Skills", ""])
    if similar:
        for source, target_skill, score in similar:
            terms = ", ".join(shared_terms(source, target_skill)) or "content overlap"
            lines.extend([
                f"- Source `{source.name}` may overlap target `{target_skill.name}` (content score {score:.2f}). Synthesize before copying.",
                f"  - Source purpose: {source.purpose_excerpt}",
                f"  - Target purpose: {target_skill.purpose_excerpt}",
                f"  - Shared content signals: {terms}",
            ])
    else:
        lines.append("- None")
    lines.extend([
        "",
        "## Recommended AGENTS.md Block",
        "",
        "Do not overwrite existing repository instructions. If compatible, merge this block into the target `AGENTS.md` and remove duplicates:",
        "",
        "```markdown",
        AGENT_RULES_BLOCK.strip(),
        "```",
        "",
        "## How To Use This Plan",
        "",
        "- Copy missing skills directly only when they do not overlap existing local skills.",
        "- For same-name or similar skills, use `repo-skill-integrator` to synthesize one target-specific skill instead of keeping duplicates.",
        "- Preserve project-specific rules in `AGENTS.md`; append or merge the learning block only where it does not conflict.",
    ])
    return lines


def main() -> int:
    args = parse_args()
    target = Path(args.target_repo).expanduser().resolve()

    missing_sources = ensure_sources()
    if missing_sources:
        for item in missing_sources:
            print(f"ERROR: missing source {item}", file=sys.stderr)
        return 1
    if not target.exists() or not target.is_dir():
        print(f"ERROR: target repo does not exist or is not a directory: {target}", file=sys.stderr)
        return 1

    source_skills = load_skills(ROOT)
    target_skills = load_skills(target)
    missing, same_name, similar = skill_plan(source_skills, target_skills)

    agent_path = target / "AGENTS.md"
    agent_exists = agent_path.exists()
    agent_text = read_text(agent_path) if agent_exists else ""
    agent_has_block = merge_block_present(agent_text)

    lines = report_lines(target, missing, same_name, similar, agent_exists, agent_has_block)

    print("\n".join(lines))
    print("\nMode: " + ("apply" if args.apply else "dry-run"))

    if not args.apply:
        print("Dry run only. Re-run with --apply to copy safe missing items and write the integration report.")
        return 0

    copied: list[str] = []
    for skill in missing:
        destination = target / ".agents" / "skills" / skill.name
        if not destination.exists():
            copy_dir(skill.path, destination)
            copied.append(f"skill:{skill.name}")

    if not agent_exists:
        copy_file(ROOT / "AGENTS.md", agent_path)
        copied.append("AGENTS.md")
    elif not agent_has_block:
        report_path = target / INTEGRATION_REPORT
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        copied.append(str(INTEGRATION_REPORT))

    for source, relative_destination in CORE_FILES:
        destination = target / relative_destination
        if not destination.exists():
            copy_file(source, destination)
            copied.append(str(relative_destination))

    optional = [(ROOT / "docs" / "templates", Path("docs") / "templates")]
    if args.include_research:
        optional.extend(OPTIONAL_DIRS)
    for source, relative_destination in optional:
        destination = target / relative_destination
        if source.exists() and not destination.exists():
            copy_dir(source, destination)
            copied.append(str(relative_destination))

    print("\nApplied safe changes:")
    if copied:
        for item in copied:
            print(f"- {item}")
    else:
        print("- None")
    print("\nNo existing AGENTS.md or skill directories were overwritten.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
