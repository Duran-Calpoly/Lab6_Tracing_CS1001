import unittest
import day4


class TestDay4(unittest.TestCase):
    def test_basic_comprehension(self):
        self.assertEqual(day4.more, [2, 3, 4, 5])

    def test_square_comprehension(self):
        self.assertEqual(day4.square(3), 9)
        self.assertEqual(day4.squares, [1, 4, 9, 16])

    def test_filtering_comprehension(self):
        self.assertFalse(day4.check(2))
        self.assertTrue(day4.check(3))
        self.assertEqual(day4.filtered, [3, 4])

    def test_filtering_and_transforming(self):
        self.assertEqual(day4.inc(3), 4)
        self.assertEqual(day4.answer, [4, 5])

    def test_process_mutates_output_not_source(self):
        source = [-1, 3, 0, 5]
        output = []
        total = day4.process(source, output)

        self.assertEqual(total, 8)
        self.assertEqual(source, [-1, 3, 0, 5])
        self.assertEqual(output, [6, 10])

    def test_process_with_intentional_alias(self):
        source = [-1, 3, 0, 5]
        output = []
        alias = output

        day4.process(source, alias)

        self.assertIs(alias, output)
        self.assertEqual(output, [6, 10])
        self.assertEqual(source, [-1, 3, 0, 5])


if __name__ == "__main__":
    unittest.main()
