import unittest
from lab_three import get_most_common_word

class TestMostCommonWord(unittest.TestCase):

    def test_simple_text(self):
        text = "apple orange apple banana"
        self.assertEqual(get_most_common_word(text), "apple")

    def test_case_insensitivity(self):
        text = "Apple apple APPLE banana"
        self.assertEqual(get_most_common_word(text), "apple")

    def test_punctuation(self):
        text = "apple, banana! apple. banana? banana"
        self.assertEqual(get_most_common_word(text), "banana")

    def test_empty_string(self):
        text = ""
        self.assertIsNone(get_most_common_word(text))

    def test_all_unique(self):
        text = "one two three"
        self.assertIn(get_most_common_word(text), ["one", "two", "three"])

    def test_multiple_most_common(self):
        text = "cat dog cat dog"
        self.assertIn(get_most_common_word(text), ["cat", "dog"])

if __name__ == '__main__':
    unittest.main()
