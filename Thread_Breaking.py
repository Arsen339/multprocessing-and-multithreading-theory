import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, "плотва", "окунь", "лещ")

class Fisher(Thread):
    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        #  Будем проверять в цикле, а не пора ли нам завершить
        self.need_stop = False

    def run(self):

        #  Обработка исключений в потоке
        catch = defaultdict(int)
        for worm in range(self.worms):
            print(f"{self.name}: Червяк номер {worm} запущен, ждем...\n", flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)  # Задержка
            fish = random.choice(FISH)

            if fish is None:
                print(f"{self.name}: Тьфу ты, сожрали червя\n", flush=True)
            else:
                print(f"{self.name}:Ага, у меня {fish}\n", flush=True)
                catch[fish] += 1
            if self.need_stop is True:
                print("ОЙ! жена ужинать зовет!", flush=True)
                break

        print(f"Итого рыбак {self.name} поймал:\n")
        for fish, count in catch.items():
            print(f"{fish} - {count}")


vasya = Fisher(name='Вася', worms=100)
vasya.start()
time.sleep(1)
if vasya.is_alive():  #  с помощью этого метода можно проверить, выполняется ли поток
    vasya.need_stop = True
vasya.join()
