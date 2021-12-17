#!usr/bin/env python
"""day 02 of advent of code 2021"""
from itertools import pairwise
from os import defpath
from pathlib import Path
from typing import Iterable, Iterator

from aoc_utils import get_lines


def main():
    """main entry point"""
    filepath = Path('data/day02.txt')

    print(f'part1: {part_one(filepath)}')
    # print(f'part2: {part_two(filepath)}')


def part_one(filepath: Path):
    """return solution to part 1"""
    instructions = get_lines(filepath)
    # forward increases horizontal position
    # down increases depth
    # up decreases depth
    horizontal, depth = 0, 0

    for line in instructions:
        movement, magnitude = line.split()
        mag = int(magnitude)

        if movement == 'forward':
            horizontal += mag
        elif movement == 'down':
            depth += mag
        elif movement == 'up':
            depth -= mag

    return horizontal * depth


if __name__ == '__main__':
    main()
