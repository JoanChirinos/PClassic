def ruby_bridge(inp):
    x = inp.split('\n')[1]
    start = 0
    end = len(x)
    while (start < end):
        current_max = end
        while (current_max > start):
            new_x = x[start:current_max]
            if (new_x.count('P') == new_x.count('T')):
                return current_max - start
            current_max -= 1
        start += 1
    return 0
        


def main():
    in1 = "10\nPTPPTTPTTP"
    in2 = "11\nPTPTPTPPPTP"
    in3 = "3\nPTP"

    print("in1 returns: {}".format(ruby_bridge(in1)))
    print("in2 returns: {}".format(ruby_bridge(in2)))
    print("in3 returns: {}".format(ruby_bridge(in3)))

main()
