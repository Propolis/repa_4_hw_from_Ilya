from models import (
    Shrek, ShrekInAction, ShrekFunkoPop, ShrekCosplayer,
    PussInBoots, Donkey, JackHorner
)

def test_character_variants():
    print("--- Тестирование Шрека ---")
    
    # Обычный
    s = Shrek("Шрек")
    s.speak()
    s.make_laugh()
    print(f"Анимированный: {s.is_animated}")
    
    # In Action
    sa = ShrekInAction("Шрек в деле")
    sa.perform_action()
    
    # Funko Pop
    sf = ShrekFunkoPop("Шрек")
    sf.display()
    print(f"Коллекционный: {sf.is_collectible}")
    
    # Cosplayer
    sc = ShrekCosplayer("Шрек", "чел")
    sc.pose()
    print(f"Человек: {sc.is_human}, Костюм: {sc.costume}")
    
    print("\n--- Проверка других персов ---")
    puss = PussInBoots("Кот в сапогах")
    donkey = Donkey("Осел")
    jack = JackHorner("Джек Хорнер")
    
    for char in [puss, donkey, jack]:
        char.speak()

if __name__ == "__main__":
    test_character_variants()
