def cardinal_confusion(inp):
    s = 0
    for a in range(1, inp + 1):
        for b in range(1, inp + 1):
            for c in range(1, inp + 1):
                for d in range(1, inp + 1):
                    if (a * b - c * d == 1):
                        s += 1
    return s
                    
def main():
    in1 = 2
    in2 = 3
    in3 = 14

    print('in1 returns {}'.format(cardinal_confusion(in1)))
    print('in2 returns {}'.format(cardinal_confusion(in2)))
    print('in3 returns {}'.format(cardinal_confusion(in3)))

main()
