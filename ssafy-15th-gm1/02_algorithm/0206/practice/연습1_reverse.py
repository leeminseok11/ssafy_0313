def my_strrev(str):
    arr = list(str)  # str -> list
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], str[i]

    str = "".join(arr)  # list -> str
    return str


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s = input()

    # s = my_strrev(s)
    # print(f'#{tc} {s}')
    #

    arr = list(s)  # str -> list
    arr.reverse()
    s = ''.join(arr)  # list -> str
    print(f'#{tc} {s}')
    #
    # s = "Reverse this strings"
    # s = s[::-1]
    # print(s)
    print(sys.getsizeof(s, str))  # 빈문자열도 49Byte 메모리차지
