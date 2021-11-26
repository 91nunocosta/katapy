"""Tasks related with the source code."""
import invoke


@invoke.task
def check_source(c):
    """Check source code using pre-commit."""
    c.run("pre-commit run --all-files", pty=True)
