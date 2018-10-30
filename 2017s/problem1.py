def treasure_chest_scanner(inp):
    nums = [int(i) for i in inp.split(' ')]
    return nums[0] * nums[1] * nums[2]


def main():
    in1 = '3 2 6'
    in2 = '5 5 5'
    in3 = '0 0 0'

    print('in1 returns {}'.format(treasure_chest_scanner(in1)))
    print('in2 returns {}'.format(treasure_chest_scanner(in2)))
    print('in3 returns {}'.format(treasure_chest_scanner(in3)))


main()
