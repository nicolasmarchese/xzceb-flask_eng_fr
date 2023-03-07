import unittest

from translator import englishToFrench, frenchToEnglish
class TestEnglish(unittest.TestCase):
    def test_when_is_null(self):
        self.assertIsNone(englishToFrench(""), None)
        
    def test_correct_translate(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

  


class TestFrench(unittest.TestCase):
    def test_when_is_null(self):
        self.assertIsNone(frenchToEnglish(""), None)

    def test_correct_translate(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()