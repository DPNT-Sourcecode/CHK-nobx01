

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A':{'price': 50, 'offer': {'quantity': 3, 'price': 130}},
    'B':{'price': 30, 'offer': {'quantity': 2, 'price': 45}},
    'C':{'price': 20, 'offer': None},
    'D':{'price': 15, 'offer': None},
}


def clean_and_check_input(input: str):
    if not isinstance(input, str) or len(input) == 0:
        return
    input = input.replace(' ', '').replace('-','').replace('_','').upper()
    if not input.isalpha():
        return
    available_items = set(PRICES.keys())
    if not set(input).issubset(available_items):
        return
    return input

def checkout(skus):
    raise NotImplementedError()

