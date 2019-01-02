import unittest
from unit_testing import cap_text


class TestCap(unittest.TestCase):

    def test_one_word(self):
        '''It should capitalize the first word when provided one word
        '''
        text = 'python'
        result = cap_text(text)
        self.assertEqual(result, 'Python')
        self.shortDescription()

    def test_multiple_words(self):
        '''It should capitalize the first word when provided two words
        '''
        text = 'monty python'
        result = cap_text(text)
        self.assertEqual(result, 'Monty python')
        self.shortDescription()


if __name__ == '__main__':
    print('The cap_text function')
    unittest.main(verbosity=2)
