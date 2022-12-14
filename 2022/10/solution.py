#!/usr/bin/env python3

def render_screen(cycles, register):
    x = cycles % 40
    sprite = [register-1, register, register+1]
    if x in sprite:
        print("#", end="")
    else:
        print(".", end="")
    if x == 39:
        print("")

def read_op(fp):
    try:
        cmd = fp.readline().strip().split()
        op = cmd[0]
    except:
        return None, 0

    try:
        val = int(cmd[1])
    except:
        val = 0
    return op, val

def main():
    cycles = 0
    register = 1
    cycle_counts = [20, 60, 100, 140, 180, 220]
    op = None
    signal_strength = 0

    with open("input.txt") as fp:
        while (True):
            old_register = register
            if not op:
                op, val = read_op(fp)
                if not op:
                    break

            if op == "noop":
                op = None
            elif op == "addx":
                op = "update_register"
            elif op == "update_register":
                register += val
                op = None
            
            cycles += 1
            if cycles in cycle_counts:
                signal_strength += cycles * old_register
            render_screen(cycles-1, old_register)

            
    print(f"Part One Anwer: {signal_strength}")

if __name__ == "__main__":
    main()  