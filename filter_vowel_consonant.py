# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
