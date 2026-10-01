import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_task1_mutation_through_alias(self):
        self.assertEqual(day1.first, [2, 4, 6, 8])
        self.assertEqual(day1.second, [2, 4, 6, 8])
        self.assertIs(day1.first, day1.second)

    def test_task2_alias_and_separate_list(self):
        self.assertEqual(day1.a, [1, 2, 3, 4])
        self.assertEqual(day1.b, [1, 2, 3, 4])
        self.assertEqual(day1.c, [1, 2, 3])
        self.assertIs(day1.a, day1.b)
        self.assertIsNot(day1.a, day1.c)


if __name__ == "__main__":
    unittest.main()
