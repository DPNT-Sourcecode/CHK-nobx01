# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y:int) -> int:
    """ Check if x and y are positive integers between 0 and 100 and if so return their sum. """
    if not (0<=x <=100) or not(0<=y<=100):
        raise ValueError("Both integers must be positive and between 0 and 100.")
    return x+y

