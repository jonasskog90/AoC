#!/usr/bin/env python3

def bubble_sort(packets):
    while True:
        changed = False
        for i in range(0, len(packets)-1):
            if compare(packets[i], packets[i+1]): # Correct order
                continue
            tmp = packets[i]
            packets[i] = packets[i+1]
            packets[i+1] = tmp
            changed = True
        if not changed:
            break
    return packets


def compare(first, second):
    # Convert to lists
    first = [first] if type(first) != list else first
    second = [second] if type(second) != list else second

    for f, s in zip(first, second):
        if not (type(f) == int and type(s) == int):
            result = compare(f, s)
            if result != None:
                return result
        elif s > f:
            return True
        elif s < f:
            return False
    else:
        if len(second) > len(first):
            return True
        if len(first) > len(second):
            return False
    return None 

def main():
    packets = []
    with open("input.txt") as fp:
        while True:
            first = eval(next(fp))
            second = eval(next(fp))
            packets.append((first, second))
            line = next(fp, None) # newline
            if not line:
                break

    sum = 0
    for i, packet_pair in enumerate(packets):
        if compare(packet_pair[0], packet_pair[1]):
            print(i)
            sum += i + 1
            
    print("Part One Answer: ", sum)

    # Flatten list
    packets = [item for sublist in packets for item in sublist]

    sorted = bubble_sort(packets)
    
    divider_packets = sorted.index([[2]])+1, sorted.index([[6]])+1
    decoder_key = divider_packets[0] * divider_packets[1]

    print("Part Two Answer: ", decoder_key)

if __name__ == "__main__":
    main()