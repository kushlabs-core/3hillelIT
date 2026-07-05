class Character:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, amount: int) -> None:
        self._hp = self._hp - amount
        if self._hp < 0:
            self._hp = 0

    def heal(self, amount: int) -> None:
        if not self.is_alive():
            return
            
        self._hp = self._hp + amount
        if self._hp > self.max_hp:
            self._hp = self.max_hp

    def is_alive(self) -> bool:
        return self._hp > 0

    @property
    def hp(self) -> int:
        return self._hp
    
# перевірка коду
hero = Character("Козак", 100)
print(f"Створили героя. ХП: {hero.hp}")

hero.take_damage(40)
print(f"Отримав 40 шкоди. Поточне ХП: {hero.hp}")

hero.take_damage(80)
print(f"Отримав ще 80 шкоди. ХП не впало в мінус? Чи живий? {hero.is_alive()} (ХП: {hero.hp})")

hero.heal(50)
print(f"Спроба полікувати мертвого. ХП залишилось: {hero.hp}")