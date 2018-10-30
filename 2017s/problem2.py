def making_a_profit(inp):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_sum = []

    day_parts = [i.split(' ') for i in inp.split('\n')]
    for i in day_parts:
        for x in range(len(i)):
            i[x] = int(i[x])
    

def main():
    in1 = '7\n4\n50 200 700 13\n20 1000 0 0\n0 0 0 0\n50 0 0 10\n23 15 0 0\n0 0 13 0\n0 13 35 68'
    in2 = '7\n2\n10 20\n20 30\n40 70\n20 20\n40 60\n10 10\n0 0'

    print('in1 returns {}'.format(making_a_profit(in1)))
    print('in2 returns {}'.format(making_a_profit(in2)))

main()
