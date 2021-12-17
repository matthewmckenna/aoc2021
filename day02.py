#!usr/bin/env python
"""day 02 of advent of code 2021"""
from pathlib import Path

from aoc_utils import get_lines


def main():
    """main entry point"""
    filepath = Path('data/day02.txt')

    print(f'part1: {part_one(filepath)}')
    print(f'part2: {part_two(filepath)}')


def part_two(filepath: Path) -> int:
    """return solution to part 2"""
    instructions = get_lines(filepath)
    # forward X
    # - increases horizontal position by X
    # - increases depth by aim * X
    # down X
    # - increases aim by X
    # up X
    # - decreases aim by X
    horizontal, depth, aim = 0, 0, 0

    for line in instructions:
        movement, magnitude = line.split()
        mag = int(magnitude)

        if movement == 'forward':
            horizontal += mag
            depth += mag * aim
        elif movement == 'down':
            aim += mag
        elif movement == 'up':
            aim -= mag

    return horizontal * depth


def part_one(filepath: Path) -> int:
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
