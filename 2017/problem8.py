def leaves_around_the_tree(inp):
    return inp.count(3) * 2 + inp.count(5) * 4

def main():
    in1 = [1, 6]
    in2 = [2, 1, 6, 4, 4]
    in3 = [4, 3, 6, 1, 1, 4, 4, 3, 6, 5]
    in4 = [1, 3, 1, 5, 2, 4, 3, 6, 1, 1, 4, 4, 3, 6, 5, 2, 1, 6, 4, 4]

    print('in1 returns: {}'.format(leaves_around_the_tree(in1)))
    print('in2 returns: {}'.format(leaves_around_the_tree(in2)))
    print('in3 returns: {}'.format(leaves_around_the_tree(in3)))
    print('in4 returns: {}'.format(leaves_around_the_tree(in4)))

main()
