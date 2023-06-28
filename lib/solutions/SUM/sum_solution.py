# noinspection PyShadowingBuiltins,PyUnusedLocal

LOWER_BOUND = 0
UPPER_BOUND = 100
def compute(x: int, y:int) -> int:
    """ Check if x and y are positive integers between 0 and 100 and if so return their sum. """
    if not (LOWER_BOUND <= x <= UPPER_BOUND) or not(LOWER_BOUND <= y<= UPPER_BOUND):
        raise ValueError("Both integers must be positive and between 0 and 100.")
    return x+y
