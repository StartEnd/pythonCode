import string
import re


def reverse(text):
    return text[::-1]


def myFormatter(text):
    text.upper()
    subText = re.sub('\s', "", text)
    to_remove = string.punctuation
    table = str.maketrans("", "", to_remove)
    newText = subText.translate(table)
    return newText


def is_palindrome(text):
    newText = myFormatter(text)
    return newText == reverse(newText)


something = 'ab.b a'   # input("Enter text: ")
if is_palindrome(something):
    print("YES, it is a palindrome")
else:
    print('No, it is not palindrome')
