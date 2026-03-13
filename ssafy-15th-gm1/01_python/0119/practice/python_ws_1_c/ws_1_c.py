password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."

first_char = password[28:35]
# print(first_char)
second_word = password[113:113+5]
# print(second_word)
third_word = password[68:65:-1]
third_word = password[66:69][::-1]
# print(third_word)
fourth_word = password[322:322+4][::-1]
# print(fourth_word)
fifth_word = password[365:365+len('python')]
# print(fifth_word)

print(f'{first_char} {second_word} {third_word} {fourth_word} \"{fifth_word}\".')