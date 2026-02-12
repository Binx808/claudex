"""claudex: Set up Claude Code for any project in one command."""

from dataclasses import dataclass, field

__version__ = "1.0.0"


@dataclass
class ProjectProfile:
    """Detected project characteristics used to generate CLAUDE.md."""

    name: str = ""
    description: str = ""
    language: str = ""  # "python" | "typescript" | "javascript" | "mixed"
    framework: str | None = None  # "FastAPI" | "Django" | "Next.js" | etc.
    package_manager: str | None = None  # "uv" | "poetry" | "pip" | "npm" | "pnpm" | "yarn"
    python_version: str | None = None  # from pyproject.toml requires-python
    src_dirs: list[str] = field(default_factory=list)
    test_dirs: list[str] = field(default_factory=list)
    has_docker: bool = False
    has_ci: bool = False
    has_db: bool = False
    db_type: str | None = None  # "postgresql" | "sqlite" | "mysql" | "mongodb"
    has_redis: bool = False
    entry_points: list[str] = field(default_factory=list)
    directory_tree: str = ""  # Formatted tree (depth 2)
    existing_claude_md: bool = False
    existing_claude_dir: bool = False
    existing_linter: str | None = None  # "ruff" | "eslint" | "biome" | None
    git_initialized: bool = False
    preset_selected: str = "generic"
