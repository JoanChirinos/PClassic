def unlock_all_safes(inp):
    out = []
    print(inp)
    inp = [i.split(' ') for i in inp.split('\n')[1:]]
    

def main():
    in1 = '2\n1 2 3\n8 9 4\n7 6 5'
    in2 = '4\n1 2 4 5\n0 10 11 12\n6 7 8 9\n13 14 15 16'
    in3 = '5\n1 2 3 4 5\n16 17 18 19 6\n15 24 25 20 7\n14 23 22 21 8\n13 12 11 10 9'

    print('in1 returns {}'.format(unlock_all_safes(in1)))
    print('in2 returns {}'.format(unlock_all_safes(in2)))
    print('in3 returns {}'.format(unlock_all_safes(in3)))

main()
