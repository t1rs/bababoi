class Tomato:
    stages = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self.index = index
        self.stage = 0

    def grow(self):
        if self.stage < len(self.stages) - 1:
            self.stage += 1
        else:
            print(f"Помидоры {self.index} уже спелые!")

    def is_ripe(self):
        return self.stage == len(self.stages) - 1


class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(1, tomato_count + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Ещё не все томаты поспели")

    @staticmethod
    def knowledge_base():
        print("Садоводство - это практика выращивания растений как часть огородничества.")
Gardener.knowledge_base()
# Пример использования:
tomato_bush = TomatoBush(5)
gardener = Gardener("John", tomato_bush)
gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
