
# hangman = __import__("hangman.py")
# word = hangman.word
import unittest
import hangman


class TestGame(unittest.TestCase):
    def test_win_msg(self):
        self.assertEqual(hangman.win_msg(), 'Поздравляем, вы выиграли!')


if __name__ == '__main__':
    unittest.main()
