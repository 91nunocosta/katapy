"""Provides main program."""
from invoke import (
    Collection,
    Program,
)

from literature import tasks

collection = Collection.from_module(tasks)

collection.configure(
    {
        'run.shell': '/bin/fish',
    },
)

program = Program(namespace=collection)
