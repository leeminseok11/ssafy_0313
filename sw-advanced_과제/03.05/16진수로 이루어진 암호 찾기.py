import sys
sys.stdin = open('16진수로 이루어진 암호 찾기.txt')

T = int(input())
for tc in range(1, T + 1):
    n = input()
    mapping = {
        '0':'0000', '1':'0001','2':'0010',
        '3':'0011', '4':'0100', '5':'0101',
        '6':'0110', '7':'0111', '8':'1000',
        '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110',
        'F':'1111'
    }
    bit_pattern ={
        '001101':'0','010011':'1','111011':'2',
        '110001':'3','100011':'4','110111':'5',
        '001011':'6','111101':'7','011001':'8',
        '101111':'9'
    }
    binary = ''
    for x in n:
        binary += mapping[x]
    binary = binary.rstrip('0')
    result = []

    for i in range(len(binary)-6, -1, -6):
        code = binary[i:i+6]
        if code in bit_pattern:
            result.append(bit_pattern[code])
    result.reverse()
    print(f'#{tc}', *result)