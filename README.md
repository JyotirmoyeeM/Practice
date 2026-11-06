# Python Practice & DSA

A growing collection of Python exercises from my learning journey — from language fundamentals to sorting and two-pointer problem solving. I use this repository to practise, keep track of what I have learned, and build a reference I can return to later.

**Start here:** [View the live showcase](https://jyotirmoyeem.github.io/Practice/) or browse the folders below. To preview locally, open [index.html](index.html) in a browser.

[![Python tests](https://github.com/JyotirmoyeeM/Practice/actions/workflows/tests.yml/badge.svg?branch=dsa-basic)](https://github.com/JyotirmoyeeM/Practice/actions/workflows/tests.yml)

## Learning map

| Topic | What I am practising | Examples |
| --- | --- | --- |
| [Python basics](Python-Basic/) | Loops, conditionals, functions, number problems, and patterns | [Prime numbers](Python-Basic/Prime_not_prime_using_function.py), [composite numbers](Python-Basic/print_composite_numbers.py) |
| [Sorting](Sorting_algo/) | Bubble, insertion, and selection sort | [Optimized bubble sort](Sorting_algo/Optimized_Bubble_sort.py), [insertion sort](Sorting_algo/Insertion_sort.py) |
| [Two-pointer problems](Two_pointer_problems/) | Pair sums, palindrome checking, and Two Sum exercises | [Pair sum](Two_pointer_problems/pair_sum.py), [palindrome check](Two_pointer_problems/check_palindrome_using_two_pointer.py), [Two Sum](Two_pointer_problems/two_sum_easy_leetcode.py), [sorted Two Sum](Two_pointer_problems/two_sum_medium_leetcode.py) |
| [Arrays](Arrays/) | Planned practice: array traversal and complexity basics | — |
| [Hash maps](Hash_Maps/) | Planned practice: lookups, counting, and grouping | — |
| [Binary search](Binary_Search/) | Planned practice: sorted data and range searching | — |
| [Stacks and queues](Stacks_and_Queues/) | Planned practice: LIFO and FIFO problems | — |
| [Dictionaries](Dictionar/) | Creating, merging, and working with dictionaries | [Merge two dictionaries](Dictionar/Merge_two_dict.py) |
| [Strings](String/) | String operations and transformations | [Modify a string](String/Modify_string.py), [Swap case](String/sWap_Case.py) |
| [Intermediate Python](Python_Intermediate/) | List comprehensions, variable arguments, and OOP experiments | [Even-number list comprehension](Python_Intermediate/List_comprehensions/even_number.py) |
| [Decorators](Decorators/) | A small decorator-based experiment | [Jarvis decorator](Decorators/Jarvis_using_decorators.py) |

These are practice files, not a finished library: examples may be exploratory or incomplete. Read a script before running it, especially if it asks for input.

## DSA roadmap

The linked starter folders are intentionally empty of solutions for now:

1. **[Arrays](Arrays/)** — understand time and space complexity, then practise array traversals.
2. **[Hash maps](Hash_Maps/)** — use dictionaries to solve lookup and frequency-counting problems.
3. **[Binary search](Binary_Search/)** — practise searching sorted data and narrowing a range.
4. **[Stacks and queues](Stacks_and_Queues/)** — explore common operations and when each structure is useful.

As exercises are added, link them from the learning map above and update the showcase page.

## Tests

The test suite uses Python's standard library; there are no extra test dependencies.

```bash
python -m unittest discover -s tests -v
```

Tests cover the sorting and two-pointer examples, plus complex-number addition. GitHub Actions runs the same command on pushes and pull requests.

## Adding a solution

Keep each exercise readable and honest about its assumptions. A useful explanation includes:

1. **Problem:** what the function should do, with a small example.
2. **Approach:** why the algorithm works; add short pseudocode if it helps.
3. **Assumptions:** such as whether the input must already be sorted.
4. **Complexity:** time and extra space.
5. **Example:** a small runnable example guarded by `if __name__ == "__main__":`.
6. **Test:** cover a normal case, an edge case, and any important input constraints.

Add a test in `tests/` when introducing a reusable solution, then run the test command above.

## Run an exercise

Install Python 3, then run a file from the repository root:

```bash
python "Sorting_algo/Optimized_Bubble_sort.py"
```

On Windows, `py` can be used instead of `python`:

```powershell
py "Two_pointer_problems/pair_sum.py"
```

## Keep the guide up to date

When adding an exercise, put it in the closest existing topic folder and add a row or example link to this map (and, when useful, to the showcase page). The existing folder names are kept as-is so links to earlier practice work remain stable.
