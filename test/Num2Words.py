import num2words


def convert_to_words():
    num = int(input("Enter any number:"))
    word = num2words.num2words(num)
    print(num, ":", word)


convert_to_words()
