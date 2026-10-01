import unittest
import day2


class TestDay2(unittest.TestCase):
    def test_tally_given_values(self):
        values = [4, 9, 2, 1]
        self.assertEqual(day2.tally(values), 16)
        self.assertEqual(values, [4, 9, 2, 1])

    def test_tally_another_list(self):
        values = [3, 5, 2]
        self.assertEqual(day2.tally(values), 10)
        self.assertEqual(values, [3, 5, 2])


if __name__ == "__main__":
    unittest.main()
