import unittest
import day3


class TestDay3(unittest.TestCase):
    def test_copy_creates_separate_list(self):
        values = [4, 9, 2, 1]
        result = day3.copy(values)

        self.assertEqual(result, [4, 9, 2, 1])
        self.assertEqual(values, [4, 9, 2, 1])
        self.assertIsNot(result, values)

    def test_increment_all(self):
        values = [4, 9, 2, 1]
        result = day3.increment_all(values)

        self.assertEqual(result, [5, 10, 3, 2])
        self.assertEqual(values, [4, 9, 2, 1])
        self.assertIsNot(result, values)

    def test_count_a(self):
        self.assertEqual(day3.count_a("banana"), 3)
        self.assertEqual(day3.count_a("cal poly"), 1)


if __name__ == "__main__":
    unittest.main()
