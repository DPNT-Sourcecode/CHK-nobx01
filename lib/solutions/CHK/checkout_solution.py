

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    'A':{'price': 50, 'offer': {'quantity': 3, 'price': 130}},
    'B':{'price': 30, 'offer': {'quantity': 2, 'price': 45}},
    'C':{'price': 20, 'offer': None},
    'D':{'price': 15, 'offer': None},
}



def clean_input(input: str) -> str | None:
    if not isinstance(input, str) or len(input) == 0:
        return
    input = input.replace(' ', '').upper()
    if not input.isalpha():
        return
    available_items = set(PRICES.keys())
    if not set(input).issubset(available_items):
        return
    return input

def checkout(skus):
    raise NotImplementedError()

