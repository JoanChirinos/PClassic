def perfect(inp):
    inp = int(inp)
    s = 0
    for i in range(1, inp):
        if inp % i == 0:
            s += i
    return inp == s


def main():
    in1 = '3'
    in2 = '6'
    in3 = '4'

    print('in1 returns: {}'.format(perfect(in1)))
    print('in2 returns: {}'.format(perfect(in2)))
    print('in3 returns: {}'.format(perfect(in3)))

main()
