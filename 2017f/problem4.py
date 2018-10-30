def parking_spots(inp):
    pairs = [i.split(' ') for i in inp.split('\n')[1:]]
    for i in pairs:
        for x in range(2):
            i[x] = int(i[x])

    out = []
    current = pairs[0]
    for i in pairs[1:]:
        if i[0] in range(current[0], current[1] + 1):
           current[1] = i[1]
        else:
            out += [current]
            current = i
    out += [current]
    return out


def main():
    in1 = "4\n1 3\n2 6\n8 10\n15 18"
    in2 = "3\n1 3\n3 5\n5 7"
    in3 = "7\n1 3\n2 6\n8 10\n15 18\n17 21\n22 23\n23 24"

    print('in1 returns {}'.format(parking_spots(in1)))
    print('in2 returns {}'.format(parking_spots(in2)))
    print('in3 returns {}'.format(parking_spots(in3)))

main()
