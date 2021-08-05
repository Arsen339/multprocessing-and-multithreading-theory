import random
from collections import defaultdict
from threading import Thread, Lock
#  Исправим гонку потоков блокировкой на добаление рыбы

FISH = (None, "плотва", "окунь", "лещ")

class Fisher(Thread):
    def __init__(self, name, worms, fish_tank, lock, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank
        #  замок для остальных потоков на время выполнения команды
        self.fish_tank_lock = lock

    def run(self):

        #  Обработка исключений в потоке

        for worm in range(self.worms):
            #  _ = 3 ** (random.randint(50, 70) * 10000)  # Задержка
            fish = random.choice(FISH)

            if fish is not None:
                #  Закрытие и открытие потоков
                try:
                    self.fish_tank_lock.acquire()
                    self.fish_tank[fish] += 1
                finally:
                    self.fish_tank_lock.release()
                self.catched += 1


#  Общий сачок для рыбы
global_fish_tank = defaultdict(int)
#  Замок
lock = Lock()

humans = ["Васек", "Колян", "Петрович", "Хмурый", "Клава"]
fishers = [Fisher(name=name, worms=100000, fish_tank=global_fish_tank, lock=lock) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())
print(f"Итого рыбаки поймали {total_fish_from_fishers}, а с берега увидели {total_fish_in_tank}")