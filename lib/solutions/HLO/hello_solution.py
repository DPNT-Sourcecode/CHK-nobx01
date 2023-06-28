

# noinspection PyUnusedLocal
# friend_name = unicode string

BASE_STRING = "Hello, "
DEFAULT = "World"
DELIMETER = "!"

def hello(friend_name: str) -> str:
    if not isinstance(friend_name, str) or len(input) == 0:
        return f"{BASE_STRING}{DEFAULT}{DELIMETER}"
    return f"{BASE_STRING}{friend_name}{DELIMETER}"


