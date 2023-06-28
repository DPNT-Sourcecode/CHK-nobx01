

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
    and checks if the SKU items are valid. It also checks the input is of instance type string.
    If so, it returns a string of characters otherwise it returns None.
    """
    if not isinstance(input, str):
        return
    input = input.replace(' ', '').replace('-','').replace('_','')
    if not input.isalpha():
        return
    available_items = set(PRICES.keys())
    if not set(input).issubset(available_items):
        return
    return input


def count_items(input: str) -> dict:
    """
    Given a valid input string comprising of letters, indicative of SKU items, this function calculates the quantity
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


def checkout(input: str) -> int:
    """
    This function calls clean_and_check_input and if the input is illegal it returns -1. If the input is accepted it
    calls count_items (which returns a dictionary item, quantity) and then loops through and calculates the
    total checkout value if there are admissible offers through a superposition of the
    offer_price * offer_quantity and unit_price * remaining_quantity. If no offers are applicable it computes the
    price as unit_price * quantity. The sum of all total prices is the total checkout value.
    """
    if len(input) == 0:
        return 0
    cleaned_input = clean_and_check_input(input)
    if cleaned_input is None:
        return -1
    counted_items = count_items(cleaned_input)
    total_prices = {}
    for sku, quantity in counted_items.items():
        unit_price = PRICES[sku]['price']
        offer = PRICES[sku]['offer']
        if offer and quantity >= offer['quantity']:
            offer_price = offer['price']
            offer_quantity = quantity // offer['quantity']
            remaining_quantity = quantity % offer['quantity']
            total_price = offer_price * offer_quantity + unit_price * remaining_quantity
        else:
            total_price = unit_price * quantity
        total_prices[sku] = total_price
    return sum(total_prices.values())

