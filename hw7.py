from functools import wraps
from typing import Any, Callable

def shout(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def positive_only(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Усі позиційні аргументи мають бути додатними!")
        return func(*args, **kwargs)
    return wrapper

#перевірка
@positive_only
def add_two(x: int) -> int:
    return x + 2

@shout
def add_suffix(value: str) -> str:
    return value + "suffix"

#shout
print(add_suffix("i"))  # Виведе: ISUFFIX

#positive_only
print(add_two(5))  # Виведе: 7

# Перевіряємз помилкою
try:
    print(add_two(-3))
except ValueError as e:
    print(f"Зловлено помилку: {e}")