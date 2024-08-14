def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # Check reverse of word is equal to the word
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def is_palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
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
