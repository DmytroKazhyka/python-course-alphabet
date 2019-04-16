from typing import List, Dict, Union, Generator
import random
import string


# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for member in data:
        member['name'] = member['name'].capitalize()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for dictionary in data:
        for key in redundant_keys:
            if key in dictionary:
                del dictionary[key]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [d for d in data if value in d.values()]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    return max([i for i in filter(lambda i: isinstance(i, str), data)], key = len)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    compare_list = [d[key] for d in data]
    min_value = min(compare_list)
    return [d for d in data if min_value in d.values()]


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    return max(list(map(lambda x: max(x), data)))


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    keys = list(string.ascii_letters)
    values = list(range(97,123)) + list(range(65,91))
    d = dict(zip(keys, values))

    return sum([d.get(char) for char in text])


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    n = 0
    while n <= 200:
        yield print(n)
        n+=1


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    return [random.choice(string.ascii_letters) for _ in range(20)]
