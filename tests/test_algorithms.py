from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from pathlib import Path
import unittest

from Python_Intermediate.complex_numbers_using_oop import Complex
from Sorting_algo.Bubble_sort_accending import bubble_sort as ascending_bubble_sort
from Sorting_algo.Insertion_sort import insertion_sort
from Sorting_algo.Optimized_Bubble_sort import bubble_sort as optimized_bubble_sort
from Sorting_algo.Selection_sort import selection_sort
from Sorting_algo.bubble_sort_descending import bubble_sort as descending_bubble_sort
from Two_pointer_problems.check_palindrome_using_two_pointer import check_palindrome
from Two_pointer_problems.pair_sum import pair_sum as value_pair_sum
from Two_pointer_problems.two_sum_easy_leetcode import pair_sum as indexed_pair_sum
from Two_pointer_problems.two_sum_medium_leetcode import pair_sum as sorted_two_sum


def load_basic_exercise(module_name, filename):
    exercise = Path(__file__).parents[1] / "Python-Basic" / filename
    spec = spec_from_file_location(module_name, exercise)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {exercise}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


binary_to_decimal = load_basic_exercise(
    "binary_to_decimal", "Binary_to_decimal.py"
).binary_to_decimal
composite_module = load_basic_exercise(
    "print_composite_numbers", "print_composite_numbers.py"
)


class SortingTests(unittest.TestCase):
    def test_ascending_sorts(self):
        algorithms = (
            ascending_bubble_sort,
            optimized_bubble_sort,
            insertion_sort,
            selection_sort,
        )
        cases = (
            ([], []),
            ([1], [1]),
            ([4, 2, 4, -1, 0], [-1, 0, 2, 4, 4]),
            ([1, 2, 3], [1, 2, 3]),
        )
        for algorithm in algorithms:
            for values, expected in cases:
                with self.subTest(algorithm=algorithm.__module__, values=values):
                    result = algorithm(values.copy())
                    self.assertEqual(result, expected)

    def test_descending_bubble_sort(self):
        self.assertEqual(descending_bubble_sort([1, 4, 2, 4, -1]), [4, 4, 2, 1, -1])


class TwoPointerTests(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(check_palindrome([]))
        self.assertTrue(check_palindrome([1, 2, 3, 2, 1]))
        self.assertFalse(check_palindrome([1, 2, 3]))

    def test_value_pairs_and_input_is_not_modified(self):
        values = [1, 3, 6, 2, 5, 4, 3, 2, 4]
        original = values.copy()
        self.assertEqual(value_pair_sum(values, 7), (4, [(1, 6), (2, 5), (3, 4), (3, 4)]))
        self.assertEqual(values, original)
        self.assertEqual(value_pair_sum([1, 1, 1, 1], 2), (2, [(1, 1), (1, 1)]))

    def test_two_sum_returns_original_zero_based_indices(self):
        values = [3, 2, 4]
        original = values.copy()
        self.assertEqual(indexed_pair_sum(values, 6), (1, 2))
        self.assertEqual(indexed_pair_sum([3, 3], 6), (0, 1))
        self.assertEqual(indexed_pair_sum([1, 2], 8), [])
        self.assertEqual(values, original)

    def test_sorted_two_sum_returns_both_index_conventions(self):
        self.assertEqual(sorted_two_sum([1, 2, 3, 4, 6], 7), ((0, 4), (1, 5)))
        self.assertEqual(sorted_two_sum([1, 2, 3], 20), [])

    def test_sorted_two_sum_rejects_unsorted_input(self):
        with self.assertRaisesRegex(ValueError, "sorted"):
            sorted_two_sum([1, 3, 2, 4], 5)


class ComplexNumberTests(unittest.TestCase):
    def test_add_returns_a_new_complex_number(self):
        first = Complex(6, 5)
        second = Complex(2, -4)
        result = first.add(second)
        self.assertEqual((result.real, result.imag), (8, 1))
        self.assertEqual((first.real, first.imag), (6, 5))
        self.assertEqual((second.real, second.imag), (2, -4))


class BinaryConversionTests(unittest.TestCase):
    def test_binary_conversion(self):
        self.assertEqual(binary_to_decimal("1011"), 11)
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("00101"), 5)

    def test_binary_conversion_rejects_invalid_input(self):
        for value in ("", "102", "-1"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    binary_to_decimal(value)


class CompositeNumberTests(unittest.TestCase):
    def test_composite_numbers_up_to_limit(self):
        output = StringIO()
        with redirect_stdout(output):
            composite_module.print_composite(10)
        self.assertEqual(output.getvalue().splitlines(), ["4", "6", "8", "9", "10"])
        self.assertFalse(composite_module.is_prime(1))
        self.assertTrue(composite_module.is_prime(7))


if __name__ == "__main__":
    unittest.main()
