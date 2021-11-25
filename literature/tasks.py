"""Provides tasks."""
from invoke import Collection

from literature import (
    code,
)

ns = Collection(
    code,
)
