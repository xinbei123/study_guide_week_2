"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # set-based answer:
    return set(words)

    # Alternate, dict-comprehension answer:
    # return { w: 1 for w in words }.keys()

    # Long form answer:
    # d = {}

    # for w in words:
    #     d[w] = 1

    # return d.keys()


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    return set(items1) & set(items2)

    # Long form solution:

    # overlap = {}
    #
    # for item1 in items1:
    #     for item2 in items2:
    #         if item1 == item2:
    #             overlap[item1] = item1
    #
    # return overlap.keys()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    
    # Straightforward excellent solution

    result = []
    s = set(numbers)

    for x in s:
        if x >= 0 and -x in s:
            result.append([-x, x])

    return result

    # As a comprehension
    #
    # s = set(numbers)
    # return [[-x, x] for x in s if x >=0 and -x in s]

    # Different style:
    #
    # seen = set()
    # sum_to_zero = set()
    #
    # for x in numbers:
    #     if -x in seen:
    #         # Add them in a predictable lower, higher value
    #         # (so we don't worry about both (-3, 3) and (3, -3)
    #         # being in the list.
    #         sum_to_zero.add((min(x, -x), max(x, -x)))
    #     else:
    #         seen.add(x)
    # return sum_to_zero

    # Set-math solution
    #
    # pos = set(numbers)
    # neg = {-x for x in input_list if x >= 0}
    # return [(-x, x) for x in pos & neg]

    # Potentially more straightforward, double-loop version:
    #
    # found = {}
    # for x in numbers:
    #     for y in input_list:
    #         if x == -y and (y, x) not in found:
    #             found[(x, y)] = 1
    # return found.keys()

    # Or, same ideas as a set:
    #
    # found = set()
    # for x in numbers:
    #     for y in input_list:
    #         if x == -y and (y, x) not in found:
    #             found.add((x, y))
    # return list(found)

    # With an optimization to not walk the whole inner list:
    # found = set()
    # for pos, x in enumerate(numbers):
    #     for y in input_list[pos + 1:]:
    #         if x == -y and (y, x) not in found:
    #             found.add((x, y))
    # return list(found)

    # Alternate functional-style answer:
    # (hold on to your seatbelts!)
    #
    # return list({tuple(sorted((x, y)))
    #              for x in numbers
    #                for y in numbers
    #              if x == -y})


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """


    tallies = {}
    most_common_count = 0

    for letter in phrase:

        if letter == ' ':
            continue

        tallies[letter] = tallies.get(letter, 0) + 1

        if tallies[letter] > most_common_count:
            most_common_count = tallies[letter]

    most_common = []

    for letter, count in tallies.items():
        if count == most_common_count:
            most_common.append(letter)

    return sorted(most_common)
    

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print("{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}")
    else:
        print(d)


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
