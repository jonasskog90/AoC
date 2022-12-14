#!/usr/bin/env python3

# https://adventofcode.com/2022/day/9

def update_next_knot(h_pos, t_pos):
    yh, xh = h_pos
    yt, xt = t_pos
    if xh >= xt + 2:
        xt += 1
        if yt < yh:
            yt += 1
        if yt > yh:
            yt -= 1
    if xh <= xt - 2:
        xt -= 1
        if yt < yh:
            yt += 1
        if yt > yh:
            yt -= 1
    if yh >= yt + 2:
        yt += 1
        if xt < xh:
            xt += 1
        if xt > xh:
            xt -= 1
    if yh <= yt - 2:
        yt -= 1
        if xt < xh:
            xt += 1
        if xt > xh:
            xt -= 1
    return (yt, xt)

def update_positions(rope, direction):
    yh, xh = rope[0]
    if direction == "R":
        xh += 1
    elif direction == "L":
        xh -= 1
    elif direction == "U":
        yh += 1
    elif direction == "D":
        yh -= 1
    
    rope[0] = (yh, xh)

    for i in range(0, len(rope)-1):
        rope[i+1] = update_next_knot(rope[i], rope[i+1])
        
    return rope

def get_unique_positions(rope): 
    visited = set()
    with open("input.txt") as fp:
        for line in fp.readlines():
            direction, steps = line.split()
            steps = int(steps)
            for step in range(0, steps):
                rope = update_positions(rope, direction) 
                visited.add(rope[-1])
    return len(visited)

def main():
    rope = [(0,0)] * 2
    result = get_unique_positions(rope)
    print(f"Part One Answer: {result}")

    rope = [(0,0)] * 10
    result = get_unique_positions(rope)
    print(f"Part Two Answer: {result}")


if __name__ == "__main__":
    main()