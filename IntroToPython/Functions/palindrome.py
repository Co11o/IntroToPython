def is_palindrome(string):
    # Check reverse of word is equal to the word
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def is_palindrome_sentence(sentence):
    sentence_chars = ""
    for char in sentence:
        if char.isalnum():
            sentence_chars += char
    return is_palindrome(sentence_chars)


word = input("Please enter a word or sentence to check: ")

if is_palindrome_sentence(word):
    print("{0} is a palindrome".format(word))
else:
    print("{0} is not a palindrome".format(word))
