import random
from enum import Enum
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class Names(str, Enum):
    JOHN = "Джон Леннон"
    PAUL = "Пол Маккартни"
    GEORGE = "Джордж Харрисон"
    RINGO = "Ринго Старр"

class Beetle:
    health_points: int
    max_hp: int
    name: Names

    def __init__(
        self,
        health_points: int = 100,
        name: Names = Names.JOHN,
    ) -> None:
        self.health_points = health_points
        self.max_hp = health_points
        self.name = name

    def __eq__(self, other: "Beetle") -> bool:
        return self.health_points == other.health_points

    def __lt__(self, other: "Beetle") -> bool:
        return self.health_points < other.health_points

    def __le__(self, other: "Beetle") -> bool:
        return self.health_points <= other.health_points

    def __str__(self) -> str:
        return f'Beetle(name="{self.name}", hp={self.health_points!r})'

    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "в стиле Джона"
        elif self.name is Names.PAUL:
            return "в стиле Пола"
        elif self.name is Names.GEORGE:
            return "в стиле Джорджа"
        return "в стиле Ринго"

    def attack(self, other: "Beetle") -> int:
        damage = random.randint(5, 25)
        other.health_points -= damage
        return damage

    def is_alive(self) -> bool:
        return self.health_points > 0

    def heal(self, amount: int):
        self.health_points = min(self.max_hp, self.health_points + amount)

class BeetlesArmy:
    beetles_list: list[Beetle]
    beetles_name: Names
    army_id: str

    def __init__(
        self,
        beetles_name: Names,
        army_id: str,
        beetles_army_size: int = 20,
        beetles_max_health_points: int = 100,
    ):
        self.beetles_list = []
        self.beetles_name = beetles_name
        self.army_id = army_id
        for _ in range(beetles_army_size):
            hp = random.randint(30, beetles_max_health_points)
            self.beetles_list.append(Beetle(health_points=hp, name=self.beetles_name))

    def __len__(self) -> int:
        return len([b for b in self.beetles_list if b.is_alive()])

    def __add__(self, other: "BeetlesArmy") -> "BeetlesArmy":
        if self.beetles_name != other.beetles_name:
            raise ValueError("Нельзя объединять жуков с разными именами!")
        new_army = BeetlesArmy(self.beetles_name, f"{self.army_id}+{other.army_id}", 0)
        new_army.beetles_list = self.beetles_list + other.beetles_list
        return new_army
    
    def __gt__(self, other: "BeetlesArmy") -> bool:
        return len(self) > len(other)

    def get_fighter(self) -> Beetle | None:
        for b in self.beetles_list:
            if b.is_alive():
                return b
        return None

def battle(army1: BeetlesArmy, army2: BeetlesArmy):
    console.print(Panel.fit(f"[bold yellow]БИТВА НАЧАЛАСЬ![/bold yellow]\n{army1.beetles_name} ({army1.army_id}) VS {army2.beetles_name} ({army2.army_id})", border_style="red"))
    
    turn = 1
    while len(army1) > 0 and len(army2) > 0:
        if turn % 2 == 1:
            attacker_army, defender_army = army1, army2
        else:
            attacker_army, defender_army = army2, army1
        
        attacker = attacker_army.get_fighter()
        defender = defender_army.get_fighter()
        
        if attacker and defender:
            dmg = attacker.attack(defender)
            msg = f"[bold cyan]{attacker.name}[/bold cyan] ({attacker_army.army_id}) атакует [bold magenta]{defender.name}[/bold magenta] ({defender_army.army_id}) {attacker.styling()} на [white]{dmg}[/white] урона!"
            
            if not defender.is_alive():
                msg += f"\n[bold red]ЖУК УБИТ![/bold red] {attacker.name} получает +10 HP бонус."
                attacker.heal(10)
            
            console.print(msg)
        
        turn += 1
        if turn > 1000: break
    
    winner = army1 if len(army1) > 0 else army2
    console.print(Panel(f"[bold green]ПОБЕДИТЕЛЬ: {winner.beetles_name} ({winner.army_id})![/bold green]", border_style="gold1"))

def main():
    console.print(Panel.fit("=== Настройка Битвы Жуков ===", style="bold magenta"))
    
    try:
        name_map = {"1": Names.JOHN, "2": Names.PAUL, "3": Names.GEORGE, "4": Names.RINGO}
        console.print("Доступные герои: 1) John, 2) Paul, 3) George, 4) Ringo")
        
        id1 = input("ID первой армии: ")
        choice1 = input("Выберите героя для первой армии (1-4): ")
        size1 = int(input("Размер первой армии (жуков): "))
        
        id2 = input("ID второй армии: ")
        choice2 = input("Выберите героя для второй армии (1-4): ")
        size2 = int(input("Размер второй армии (жуков): "))
        
        army1 = BeetlesArmy(name_map.get(choice1, Names.JOHN), id1, size1)
        army2 = BeetlesArmy(name_map.get(choice2, Names.JOHN), id2, size2)
        
        battle(army1, army2)
        
        if len(army1) > len(army2):
            console.print(f"Армия {army1.army_id} была больше в конце.")
        elif len(army2) > len(army1):
            console.print(f"Армия {army2.army_id} была больше в конце.")
            
    except Exception as e:
        console.print(f"[bold red]Ошибка:[/bold red] {e}")

if __name__ == "__main__":
    main()
