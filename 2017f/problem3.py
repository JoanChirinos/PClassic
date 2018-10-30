def prank_planning(inp):
    if len(inp) == 1:
        print('')
        return
    for i in inp.split('\n')[1:]:
        print(i[::-1])

def main():
    in1 = '2\nwalnut\nchestnut'
    in2 = '1\noak'
    in3 = '0'

    print('in1:')
    prank_planning(in1)
    print('\nin2:')
    prank_planning(in2)
    print('\nin3:')
    prank_planning(in3)

main()
