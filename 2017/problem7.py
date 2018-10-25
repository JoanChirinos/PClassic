def find_path(inp_array, x_at, y_at, x_max, y_max):
    if (x_at == x_max and y_at == y_max):
        return 0
    if (x_at == x_max):
        return int(inp_array[x_at][y_at]) + find_path(inp_array, x_at, y_at + 1, x_max, y_max)
    if (y_at == y_max):
        return int(inp_array[x_at][y_at]) + find_path(inp_array, x_at + 1, y_at, x_max, y_max)
    path1 = int(inp_array[x_at][y_at]) + find_path(inp_array, x_at, y_at + 1, x_max, y_max)
    path2 = int(inp_array[x_at][y_at]) + find_path(inp_array, x_at + 1, y_at, x_max, y_max)
    return min([path1, path2])
    

def stressful_park(inp):
    arr = in_to_array(inp)
    x_max = int(arr[0][0])
    y_max = int(arr[0][1])
    return find_path(arr[1:], 0, 0, x_max - 1, y_max - 1)


def in_to_array(inp):
    vals = inp.split('\n')
    to_return = []
    for i in vals:
        to_return += [i.split(' ')]
    return to_return

def main():
    in1 = "5 4\n0 1 2 3\n1 2 3 4\n2 3 4 5\n3 4 5 6\n4 5 6 0"
    in2 = "6 6\n0 1 1 2 9 9\n4 1 1 9 9 9\n3 9 9 9 9 9\n1 1 1 1 9 9\n9 9 9 1 1 1\n9 9 9 9 9 0"
    in3 = "3 5\n0 9 1 1 1\n1 9 1 9 1\n1 1 1 7 0"

    print('in1 returns: {}'.format(stressful_park(in1)))
    print('in2 returns: {}'.format(stressful_park(in2)))
    print('in3 returns: {}'.format(stressful_park(in3)))

main()
