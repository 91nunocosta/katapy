"""nox configuration."""
from pathlib import Path

import nox
from poetry.core.pyproject.toml import PyProjectTOML

PROJECT = PyProjectTOML(Path.cwd() / "pyproject.toml").poetry_config

PROJECT_NAME = PROJECT["name"]
PROJECT_VERSION = PROJECT["version"]

SRC_DIR = PROJECT_NAME.replace("-", "_")

TEST_COVERAGE = 100


@nox.session(python=None, reuse_venv=True)
def check_source(session):
    """Check the source code."""
    session.run("literature", "code.check-source")


@nox.session(python="3.9")
def test_package(session):
    """Test package."""
    session.run("literature", "tox.run")
