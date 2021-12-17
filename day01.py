#!usr/bin/env python
"""day 01 of advent of code 2021"""
from itertools import pairwise
from pathlib import Path
from typing import Iterable, Iterator

from aoc_utils import text_to_ints


def main():
    """main entry point"""
    filepath = Path('data/day01.txt')
    print(f'part1: {part_one(filepath)}')
    print(f'part2: {part_two(filepath)}')


def part_two(filepath: str):
    """return solution to part 2"""
    depths = text_to_ints(filepath)
    sums = (sum(v) for v in triplewise(depths))

    return count_next_greater_than_last(sums)


def triplewise(iterable: Iterable) -> Iterator[tuple[int]]:
    "return overlapping triplets from an iterable. taken from itertools docs."
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def count_next_greater_than_last(iterable: Iterable) -> int:
    return sum(second > first for first, second in pairwise(iterable))


def part_one(filepath: Path):
    """return solution to part 1"""
    depths = text_to_ints(filepath)
    
    return count_next_greater_than_last(depths)


if __name__ == '__main__':
    main()
