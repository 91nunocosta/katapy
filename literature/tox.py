"""Tox tasks."""
import invoke


@invoke.task
def run(c):
    """Run tox."""
    c.run("tox")

