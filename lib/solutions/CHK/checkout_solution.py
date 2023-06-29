

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A':{'price': 50, 'offer': [{'quantity': 3, 'price': 130}, {'quantity': 5, 'price': 200}]},
    'B':{'price': 30, 'offer': [{'quantity': 2, 'price': 45}]},
    'C':{'price': 20, 'offer': None},
    'D':{'price': 15, 'offer': None},
    'E':{'price': 40, 'offer': [{'quantity': 2, 'free_item': 'B'}]},
}


def clean_and_check_input(input: str):
    """
    This function removes spaces and delimeters (e.g. dashes and underscores) and checks
    if the SKU items are valid. It also checks the input is of instance type string.
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


def sort_offers(offers: list) -> list:
    """
    Given a list of dicts comprising of quantity and price keys (and occasionally quantity and free_item),
    return the list in a sorted order such that the most valuable offers (i.e. the ones minimising price/quantity ratio)
    show up first.
    """
    free_item = next((item for item in offers if 'free_item' in item), None)
    remaining_items = [item for item in offers if 'free_item' not in item]
    sorted_items = sorted(remaining_items, key=lambda d: d['price'] / d['quantity'])
    return [free_item] + sorted_items if free_item else sorted_items


def get_items_with_free_item() -> list:
    """
    Although the PRICES dictionary is defined, this function programmatically extracts a list of the items that
    when purchased result in other free items.
    """
    items_with_free_item = [
        item
        for item, data in PRICES.items()
        if data.get('offers') and any('free_item' in offer for offer in data['offers'])
    ]
    return items_with_free_item


def get_offer_with_free_item(offers: list) -> dict:
    """
    Given a list of dictionaries, return the one with the key 'free_item'
    """
    return next((d for d in offers if 'free_item' in d), None)


def apply_free_items(counted_items):
    """
    Reduce quantities in counted_items for qualified free items, if applicable.
    """
    items_with_free_item = get_items_with_free_item()
    for item in items_with_free_item:
        if item in counted_items:
            offers = PRICES[item]['offers']
            offer = get_offer_with_free_item(offers)
            offer_quantity = counted_items[item] // offer['quantity']
            free_sku = offer['free_item']
            number_of_items = counted_items[free_sku]
            applied_quantity = number_of_items if number_of_items <= offer_quantity else offer_quantity
            counted_items[free_sku] -= applied_quantity
    return counted_items

def checkout(input: str) -> int:
    """
    This function returns 0 if the input is  clean_and_check_input and if the input is illegal it returns -1. If the input is accepted it
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
