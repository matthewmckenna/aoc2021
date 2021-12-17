"""utility functions for advent of code 2021"""
from pathlib import Path
from typing import Iterator


def text_to_ints(filepath: Path) -> Iterator[int]:
    """read a file of numbers and yield a generator of ints"""
    with open(filepath, 'rt') as f:
        for line in f:
            yield int(line.rstrip())


def get_lines(filepath: Path) -> Iterator[str]:
    """read a file and yield a generator of stripped lines"""
    with open(filepath, 'rt') as f:
        for line in f:
            yield line.rstrip()
