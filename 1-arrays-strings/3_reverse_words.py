# Reverse words
# Write a function reverse_words() that takes a message as a list of characters
# and reverses the order of the words in place.
#
# Assume the message contains only letters and spaces, and all words are
# separated by one space.

from typing import List
import unittest


def reverse_words(s: List[str], i: int = 0, j: int = None) -> None:
    """Reverses order of words in list of characters in s[i...j+1]"""
    if j is None:
        j = len(s) - 1
    reverse_string(s, i, j)
    while True:
        i, wordend = next_word_inds(s, i, j)
        reverse_string(s, i, wordend)
        i = wordend + 1
        if i > j:
            return


def reverse_string(s: List[str], i: int, j: int) -> None:
    """Reverses list of characters in place in s[i...j]"""
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def next_word_inds(s: List[str], i: int, j: int) -> int:
    """Returns start and end indices of next word in s[i...j]"""
    while i < j and s[i] == " ":
        i += 1
    wordend = i
    while wordend < j and s[wordend+1] != " ":
        wordend += 1
    return i, wordend


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        messages = ["cake pound steal", "a lovely day",
                    "i am a", "  more   spaces here "]
        stringified = [[x for x in message] for message in messages]
        for message in stringified:
            reverse_words(message)
            print("".join(message))


if __name__ == "__main__":
    unittest.main()
