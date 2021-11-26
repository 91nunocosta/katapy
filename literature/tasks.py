"""Provides tasks."""
from invoke import Collection

from literature import code, tox

ns = Collection(
    code,
    tox,
)
