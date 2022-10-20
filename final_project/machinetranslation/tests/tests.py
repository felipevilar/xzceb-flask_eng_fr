import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
  def test_null(self):
    self.assertEqual(english_to_french(None), 'Bonjour')
  def test_hello(self):
    self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
  def test_null(self):
    self.assertEqual(french_to_english(None), 'Hello')
  def test_bonjour(self):
    self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
  unittest.main()
