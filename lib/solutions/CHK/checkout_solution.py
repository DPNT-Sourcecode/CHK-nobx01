

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A':{'price': 50, 'offer': {'quantity': 3, 'price': 130}},
    'B':{'price': 30, 'offer': {'quantity': 2, 'price': 45}},
    'C':{'price': 20, 'offer': None},
    'D':{'price': 15, 'offer': None},
}


def clean_and_check_input(input: str):
    """
    This function removes spaces and delimeters (e.g. dashes and underscores), it capitalises the letters,
    and checks if the SKU items are valid. It also checks the input is of instance type string and is non-empty.
    If so, it returns a string of characters otherwise it returns None.
    """
    if not isinstance(input, str) or len(input) == 0:
        return
    input = input.replace(' ', '').replace('-','').replace('_','').upper()
    if not input.isalpha():
        return
    available_items = set(PRICES.keys())
    if not set(input).issubset(available_items):
        return
    return input


def count_items(input: str) -> dict:
    """
    Given a valid string input comprising of letters indicative of SKU items, this function calculates the quantity
    of each item and returns it in a dictionary.
    E.g. "AABBBBBCDDAADD" -> {'A': 4, 'B': 5, 'C': 1, 'D': 4}
    """
    counts = {}
    for letter in input:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


def checkout(skus):
    raise NotImplementedError()

