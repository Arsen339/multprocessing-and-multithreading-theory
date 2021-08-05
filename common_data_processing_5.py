import random
from collections import defaultdict
from threading import Thread

FISH = (None, "плотва", "окунь", "лещ")

class Fisher(Thread):
    def __init__(self, name, worms, fish_tank,  *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank

    def run(self):

        #  Обработка исключений в потоке

        for worm in range(self.worms):
            #  _ = 3 ** (random.randint(50, 70) * 10000)  # Задержка
            fish = random.choice(FISH)

            if fish is not None:
                self.fish_tank[fish] += 1
                self.catched += 1


#  Общий сачок для рыбы
global_fish_tank = defaultdict(int)

humans = ["Васек", "Колян", "Петрович", "Хмурый", "Клава"]
fishers = [Fisher(name=name, worms=100000, fish_tank=global_fish_tank) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())
print(f"Итого рыбаки поймали {total_fish_from_fishers}, а с берега увидели {total_fish_in_tank}")

#  Из-за общего доступа к памяти происходят ошибки(состояние гонки, race condition)
#  Необходимо использовать атомарные операции