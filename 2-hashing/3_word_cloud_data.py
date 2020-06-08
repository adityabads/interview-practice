# Word cloud data
# Write code that takes a long string and builds its word cloud data in a
# dictionary, where the keys are words and the values are the number of times
# the words occurred.
#
# Think about capitalized words. For example, look at these sentences:
# 'After beating the eggs, Dana read the next step:'
# 'Add milk and eggs, then add flour and sugar.'
# What do we want to do with "After", "Dana", and "add"?
# Your final dictionary should include one "Add" or "add" with a value of 22.
# Make reasonable (not necessarily perfect) decisions about cases like "After"
# and "Dana".
#
# Assume the input will only contain words and standard punctuation.
#
# BONUS
# 1. We haven't explicitly talked about how to handle more complicated character
# sets. How would you make your solution work with more unicode characters?
# What changes need to be made to handle silly sentences like these:
# I'm singing ♬ on a ☔ day.
# ☹ + ☕ = ☺.
#
# 2. We limited our input to letters, hyphenated words and punctuation. How
# would you expand your functionality to include numbers, email addresses,
# twitter handles, etc.?
#
# 3. How would you add functionality to identify phrases or words that belong
# together but aren't hyphenated? ("Fire truck" or "Interview Cake")
#
# 4. How could you improve your capitalization algorithm?
#
# 5. How would you avoid having duplicate words that are just plural or singular
# possessives?

from collections import defaultdict
from typing import Dict
import unittest


def count_words(s: str, i: int = 0, j: int = None) -> Dict[str, int]:
    """Returns dict of word counts in s[i...j]"""
    if j is None:
        j = len(s) - 1
    is_sentence_start = True
    counts = defaultdict(int)
    while i <= j:
        i, wordend = next_word_inds(s, i, j)
        word = s[i:wordend+1]
        if is_sentence_start:
            word = word.lower()
            is_sentence_start = False
        counts[word] += 1
        if wordend < j and s[wordend+1] in {".", "!", "?"}:
            is_sentence_start = True
        i = wordend + 2
    return counts


def next_word_inds(s: str, i: int, j: int) -> int:
    """Returns start and end indices of next word in s[i...j]"""
    punctuation = {" ", ",", ":", ";", "(", ")", "/", ".", "!", "?"}
    while i < j and s[i] in punctuation:
        i += 1
    wordend = i
    while wordend < j and s[wordend+1] not in punctuation:
        wordend += 1
    return i, wordend


class TestWordCloudData(unittest.TestCase):
    def test_find_counts(self):
        tests = [
            "After beating the eggs, Dana read the next step:",
            "Add milk and eggs, then add flour and sugar.",
            "Hi my name is Angel! I see an angel.",
            "I half-finished my homework.",
            "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.",
            "The bill came to five dollars."
        ]
        for test in tests:
            print(count_words(test))


if __name__ == "__main__":
    unittest.main()
