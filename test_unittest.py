import unittest
# import hangman
#
#
# class TestHideWord(unittest.TestCase):
#     def test_win_msg(self):
#         self.assertEqual(hangman.win_msg(), 'Поздравляем, вы выиграли!')

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()
