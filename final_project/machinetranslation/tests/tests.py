import unittest

from translator import english_to_french, french_to_english
class TestEnglish(unittest.TestCase):
    def test_when_is_null(self):
        self.assertIsNone(english_to_french(""), None)
        
    def test_correct_translate(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

  


class TestFrench(unittest.TestCase):
    def test_when_is_null(self):
        self.assertIsNone(french_to_english(""), None)

    def test_correct_translate(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()