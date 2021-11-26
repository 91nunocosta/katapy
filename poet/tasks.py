"""Provides tasks."""
from invoke import Collection, task

from poet import code, tox


@task
def check(c):
    """Check implementation."""
    code.check_source(c)
    tox.run(c)


ns = Collection(
    check,
    code,
    tox,
)
