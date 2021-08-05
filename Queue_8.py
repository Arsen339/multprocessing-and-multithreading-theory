import random
import threading
from collections import defaultdict
import queue
import time

FISH = (None, "плотва", "окунь", "лещ")

class Fisher(threading.Thread):

    def __init__(self, name, worms, catcher, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    def run(self):
        for worm in range(self.worms):
            print(f"{self.name}, {worm}: забросили, ждем", flush=True)
            fish = random.choice(FISH)
            if fish is None:
                print(f"{self.name}: Тьфу ты, сожрали червя\n", flush=True)
            else:
                print(f"{self.name} , {worm}: поймал {fish} и хочет положить его в садок", flush=True)
                if self.catcher.full():
                    #  full - полный поток, empty - пустой
                    print(f"{self.name}, {worm}: садок полон!!!", flush=True)
                    # Этот метод у очереди - атомарный и блокирующий
                    # Поток приостановился, пока нет места в очереди
                self.catcher.put(fish)
                print(f"{self.name}, {worm}: наконец-то положил {fish}  в садок", flush=True)


class Boat(threading.Thread):

    def __init__(self, worms_per_fisher=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.catcher = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, catcher=self.catcher)
        self.fishers.append(fisher)

    def run(self):
        print("Лодка вышла в море", flush=True)
        time.sleep(random.randint(20, 30)/10)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                fish = self.catcher.get(timeout=1)
                print(f"Садок принял {fish}", flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print(f"В садке пусто в течение одной секунды!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break

        for fisher in self.fishers:
            fisher.join()
        print(f"Лодка возвращается домой с {self.fish_tank}", flush=True)


boat = Boat(worms_per_fisher=10)
humans = ["Васек", "Колян", "Петрович", "Хмурый", "Клава"]
for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()
print(f"Лодка привезла {boat.fish_tank}")