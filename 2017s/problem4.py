def security_analysis(inp):
    inp = inp.split('\n')
    letter = inp[0]
    string_1 = inp[1]
    string_2 = inp[2]

    longest = ''

    for start in range(len(string_1)):
        for end in range(start, len(string_1)):
            if end - start > len(longest) and string_1[start:end][0] == letter and string_1[start:end] in string_2:
                longest = string_1[start:end]
    return longest

def main():
    in1 = 'b\nbabababababab\npabapabapabapabap'
    in2 = 'm\nmommydad\ndaddymommy'
    in3 = 'y\npotatopiefails\nbankheistwillfail'

    print('in1 returns {}'.format(security_analysis(in1)))
    print('in2 returns {}'.format(security_analysis(in2)))
    print('in3 returns {}'.format(security_analysis(in3)))

main()
