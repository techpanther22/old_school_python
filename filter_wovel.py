# This is a sample Python script
# for filtering the vowels using the list comprehension
# basiscally it is creating new string using a list using nested condition and join keyword


def print_vowel(user_input):
    value = ''
    for i in user_input:
        # print("inside")
        if i in ['a', 'e', 'i', 'o', 'u']:
            # print(i)
            value += i
            # value = "hello".i
            # print(123)
    print(value)


def print_consonant(user_input):
    value = ''
    for i in user_input:
        # print("inside")
        if i not in ['a', 'e', 'i', 'o', 'u']:
            value += i
    return value


# Press the green button in the gutter to run the script.
s = input("enter the string\n")
print_vowel(s)
print(print_consonant(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
