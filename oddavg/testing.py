import unittest
import odd_avg

class Test_Odd_Av(unittest.TestCase):
    def test_odd_av_letter_list(self):
        test_list = [1, 2, 3, 4, 5, "a", "b", "c"]
        self.assertEqual(odd_avg.odd_average(test_list), 3)

    def test_odd_av_no_list(self):
        self.assertEqual(odd_avg.odd_average(1, 2, 3), 2)

    def test_odd_av_not_just_numbers(self):
        test_list = [2 + 3, 2 * 2, 5 - 1]
        self.assertEqual(odd_avg.odd_average(test_list), 5)

if __name__ == "__main__":
    unittest.main()
