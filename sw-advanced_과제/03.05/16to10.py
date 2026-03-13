import sys
sys.stdin = open('16to10.txt')

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
    a = ''
    for i in n:
        a += mapping[i]
    result=[]
    for i in range(0, len(a), 7):
        div = a[i:i+7]
        b = 0

        for j in range(len(div)):
            b = b*2 + int(div[j])
        result.append(b)

    print(f'#{tc}',*result)