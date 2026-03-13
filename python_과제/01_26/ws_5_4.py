# 아래 함수를 수정하시오.
def capitalize_words(s):
    words = s.split(' ')
    result = []

    for word in words:
        result.append(word.capitalize())

    return ' '.join(result)



result = capitalize_words("hello, world!")
print(result)
