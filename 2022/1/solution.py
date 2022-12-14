#!/usr/env/bin python3

# https://adventofcode.com/2022/day/1

def get_calories_list():
    calories_per_elf = []
    cals = 0
    with open("input.txt") as fp:
        for line in fp.readlines():
            if not line.strip():
                calories_per_elf.append(cals)
                cals = 0
            else:
                cals += int(line)

    calories_per_elf.sort() # Sort in ascending order
    return calories_per_elf

def main():
    calories_per_elf = get_calories_list()

    max_cals = calories_per_elf[-1]
    print(f"Part One: {max_cals}")

    n = 3
    max_n_cals = sum(calories_per_elf[-n:]) 
    print(f"Part Two: {max_n_cals}")

if __name__ == "__main__":
    main()