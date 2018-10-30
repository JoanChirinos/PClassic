def subway_system(inp):
    inps = [int(i) for i in inp.split('\n')]
    return (float(inps[0]) / inps[1] * 100) >= inps[2]


def main():
    in1 = '10\n20\n65'
    in2 = '5\n50\n10'

    print('in1 returns {}'.format(subway_system(in1)))
    print('in2 returns {}'.format(subway_system(in2)))

main()
