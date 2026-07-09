class CandyStash:
    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Кількість цукерок має бути цілим числом (int).")
        if value < 0:
            raise ValueError("Кількість цукерок не може бути від'ємною.")

    def __init__(self, count: int):
        self.validate_amount(count)
        if count > self.MAX_CAPACITY:
            count = self.MAX_CAPACITY
        self._count = count

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self) -> int:
        """Гетер: дозволяє дивитися кількість цукерок."""
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        """Сетер: валідує і міняє кількість цукерок, обмежуючи її максимумом."""
        self.validate_amount(value)
        if value > self.MAX_CAPACITY:
            value = self.MAX_CAPACITY
        self._count = value

    def __str__(self) -> str:
        return f"CandyStash ({self._count}/{self.MAX_CAPACITY})"

    def __repr__(self) -> str:
        return f"CandyStash({self._count})"

    def __add__(self, other: int):
        if not isinstance(other, int):
            raise ValueError("Додавати можна тільки ціле число цукерок.")
        new_count = self._count + other
        if new_count > self.MAX_CAPACITY:
            new_count = self.MAX_CAPACITY
        return CandyStash(new_count)

    def __sub__(self, other: int):
        if not isinstance(other, int):
            raise ValueError("Віднімати можна тільки ціле число цукерок.")
        new_count = self._count - other
        if new_count < 0:
            new_count = 0
        return CandyStash(new_count)

    def __eq__(self, other) -> bool:
        if isinstance(other, CandyStash):
            return self._count == other._count
        if isinstance(other, int):
            return self._count == other
        return False
    

# Перевірка коду
# 1. Перевірка створення та ліміту MAX_CAPACITY
stash1 = CandyStash(20)
print(stash1)  # Очікуємо: CandyStash (20/50)

stash_over = CandyStash(100)
print(stash_over)  # Очікуємо: CandyStash (50/50) (обрізало до 50)

# 2. Перевірка альтернативного конструктора (повний рюкзак)
full = CandyStash.full_stash()
print(f"Повний рюкзак: {full}")  # Очікуємо: CandyStash (50/50)

# 3. Перевірка додавання (+) та ліміту
stash2 = CandyStash(40)
stash2 = stash2 + 15
print(f"Після додавання 15: {stash2}")  # Очікуємо: CandyStash (50/50) (не більше 50)

# 4. Перевірка віднімання (-) та обрізання до 0
stash3 = CandyStash(10)
stash3 = stash3 - 25
print(f"Спробували з'їсти 25 з 10: {stash3}")  # Очікуємо: CandyStash (0/50) (не менше 0)

# 5. Перевірка порівняння (==)
stash_a = CandyStash(15)
stash_b = CandyStash(15)
print(f"Рюкзак == Рюкзак: {stash_a == stash_b}")  # Очікуємо: True
print(f"Рюкзак == Число 15: {stash_a == 15}")  # Очікуємо: True
print(f"Рюкзак == Число 10: {stash_a == 10}")  # Очікуємо: False

# 6. Перевірка помилки (валідація)
print("\n--- Тест помилки (має вибити ValueError) ---")
try:
    bad_stash = CandyStash(-5)
except ValueError as e:
    print(f"Працює! Зловлено помилку: {e}")