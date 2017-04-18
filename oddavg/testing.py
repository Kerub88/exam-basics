import unittest
import odd_avg

class Test_Odd_Av(unittest.TestCase):
    def test_odd_av_letter_list(self):
        test_list = [1, 2, 3, 4, 5, a, b, c]
        self.assertEqual(odd_avg.odd_average(test_list), 3)

if __name__ == "__main__":
    unittest.main()
