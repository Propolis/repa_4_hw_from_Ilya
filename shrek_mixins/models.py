class MixinSpeakable:
    def speak(self):
        print(f"{getattr(self, 'name', 'Перс')} говорит!")

class MixinActionable:
    def perform_action(self):
        print(f"{getattr(self, 'name', 'Перс')} выполняет действие!")

class MixinCollectible:
    is_collectible = True

class MixinPoseable:
    def pose(self):
        print(f"{getattr(self, 'name', 'Перс')} позирует для фото!")

class MixinCostumeWearable:
    costume = " костюм"

class MixinAnimated:
    is_animated = True

class MixinFunny:
    def make_laugh(self):
        print(f"{getattr(self, 'name', 'Перс')} всех рассмешил!")

# === Базовые классы ===

class BaseCharacter(MixinSpeakable, MixinAnimated, MixinFunny):
    def __init__(self, name):
        self.name = name

class BaseHuman:
    is_human = True

class BaseInActionCharacter(BaseCharacter, MixinActionable):
    pass

class BaseFunkoPop(BaseCharacter, MixinCollectible):
    def display(self):
        print(f"Выставили Funko Pop {self.name} на полку")

class BaseCosplayer(BaseCharacter, BaseHuman, MixinPoseable, MixinCostumeWearable):
    def __init__(self, name, human_name):
        super().__init__(name)
        self.human_name = human_name

# Обычные персонажи
class Shrek(BaseCharacter): pass
class PussInBoots(BaseCharacter): pass
class Donkey(BaseCharacter): pass
class JackHorner(BaseCharacter): pass

# In Action
class ShrekInAction(BaseInActionCharacter): pass
class PussInBootsInAction(BaseInActionCharacter): pass
class DonkeyInAction(BaseInActionCharacter): pass
class JackHornerInAction(BaseInActionCharacter): pass

# Funko Pop
class ShrekFunkoPop(BaseFunkoPop): pass
class PussInBootsFunkoPop(BaseFunkoPop): pass
class DonkeyFunkoPop(BaseFunkoPop): pass
class JackHornerFunkoPop(BaseFunkoPop): pass

# Cosplayers
class ShrekCosplayer(BaseCosplayer): pass
class PussInBootsCosplayer(BaseCosplayer): pass
class DonkeyCosplayer(BaseCosplayer): pass
class JackHornerCosplayer(BaseCosplayer): pass
