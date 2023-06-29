

# noinspection PyUnusedLocal
# skus = unicode string

FREE_ITEM_KEY = 'free_item'

#TODO: populate directly from .txt file
PRICES = {
    'A':{'price': 50, 'offers': [{'quantity': 3, 'price': 130}, {'quantity': 5, 'price': 200}]},
    'B':{'price': 30, 'offers': [{'quantity': 2, 'price': 45}]},
    'C':{'price': 20, 'offers': None},
    'D':{'price': 15, 'offers': None},
    'E':{'price': 40, 'offers': [{'quantity': 2, FREE_ITEM_KEY: 'B'}]},
    'F':{'price': 10, 'offers': [{'quantity': 2, FREE_ITEM_KEY: 'F'}]},
    'G':{'price': 20, 'offers': None},
    'H':{'price': 10, 'offers': [{'quantity': 5, 'price': 45}, {'quantity': 10, 'price': 80}]},
    'I':{'price': 35, 'offers': None},
    'J':{'price': 60, 'offers': None},
    'K':{'price': 80, 'offers': [{'quantity': 2, 'price': 150}]},
    'L':{'price': 90, 'offers': None},
    'M':{'price': 15, 'offers': None},
    'N':{'price': 40, 'offers': [{'quantity': 3, FREE_ITEM_KEY: 'M'}]},
    'O':{'price': 10, 'offers': None},
    'P':{'price': 50, 'offers': [{'quantity': 5, 'price': 200}]},
    'Q':{'price': 30, 'offers': [{'quantity': 3, 'price': 80}]},
    'R':{'price': 50, 'offers': [{'quantity': 3, FREE_ITEM_KEY: 'Q'}]},
    'S':{'price': 30, 'offers': None},
    'T':{'price': 20, 'offers': None},
    'U':{'price': 40, 'offers': [{'quantity': 3, FREE_ITEM_KEY: 'U'}]},
    'V':{'price': 50, 'offers': [{'quantity': 2, 'price': 90}, {'quantity': 3, 'price': 130}]},
    'W':{'price': 20, 'offers': None},
    'X':{'price': 90, 'offers': None},
    'Y':{'price': 10, 'offers': None},
    'Z':{'price': 50, 'offers': None},
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
    for sku in input:
        counts[sku] = counts.get(sku, 0) + 1
    return counts


def sort_offers(offers: list) -> list:
    """
    Given a list of dicts comprising of quantity and price keys (and occasionally quantity and free_item),
    return the list in a sorted order such that the most valuable offers (i.e. the ones minimising price/quantity ratio)
    show up first.
    """
    free_item = next((item for item in offers if FREE_ITEM_KEY in item), None)
    remaining_items = [item for item in offers if FREE_ITEM_KEY not in item]
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
        if data.get('offers') and any(FREE_ITEM_KEY in offer for offer in data['offers'])
    ]
    return items_with_free_item


def get_offer_with_free_item(offers: list) -> dict:
    """
    Given a list of dictionaries, return the one with the key 'free_item'
    """
    return next((d for d in offers if FREE_ITEM_KEY in d), None)


def apply_free_items(counted_items):
    """
    Remove from counted_items the qualified free items, where applicable. The case of an item possessing a
    free offer for itself is treated separately.
    """
    items_with_free_item = get_items_with_free_item()
    for item in items_with_free_item:
        if item in counted_items:
            offers = PRICES[item]['offers']
            offer = get_offer_with_free_item(offers)
            free_sku = offer[FREE_ITEM_KEY]
            # item==free_sku is an 'activation switch', if True it represents the case of free self item e.g. case F
            offer_quantity = counted_items[item] // (offer['quantity'] + (item == free_sku))
            if free_sku in counted_items:
                counted_items[free_sku] -= min(counted_items[free_sku], offer_quantity)
    return counted_items


def checkout(input: str) -> int:
    """
    This function returns 0 if the input is  clean_and_check_input and if the input is illegal it returns -1.
    If the input is accepted it calls count_items (which returns a dictionary item, quantity).
    It then eliminates free items from the counting, where applicable. Finally, it loops through and calculates
    the offer_quantity for each applicable offer and it applies the most valuable offers first (favouring the customer).
    The remaining quantities are computed on the basis of unit_price. The sum is the total checkout value.
    """
    if len(input) == 0:
        return 0

    cleaned_input = clean_and_check_input(input)

    if cleaned_input is None:
        return -1

    counted_items = count_items(cleaned_input)
    counted_items = apply_free_items(counted_items)

    total_prices = {}
    for sku, quantity in counted_items.items():
        unit_price = PRICES[sku]['price']
        total_price = 0
        offers = PRICES[sku]['offers']
        if offers:
            for offer in sort_offers(offers):
                if FREE_ITEM_KEY not in offer and quantity >= offer['quantity']:
                    offer_quantity = quantity // offer['quantity']
                    quantity = quantity % offer['quantity']
                    total_price += offer['price'] * offer_quantity
        total_price += unit_price * quantity
        total_prices[sku] = total_price
    return sum(total_prices.values())
