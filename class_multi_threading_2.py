import random
from collections import defaultdict
from threading import Thread

FISH = (None, "плотва", "окунь", "лещ")

class Fisher(Thread):
    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms

    def run(self):
        try:
            #  Обработка исключений в потоке
            catch = defaultdict(int)
            for worm in range(self.worms):
                print(f"{self.name}: Червяк номер {worm} запущен, ждем...\n", flush=True)
                _ = 3 ** (random.randint(50, 70) * 10000)  # Задержка
                fish = random.choice(FISH)
                dice = random.randint(1, 5)
                if self.name == "Коля" and dice == 1:
                    raise ValueError(f"Блин, у меня сломалась удочка на {worm} черве")
                if fish is None:
                    print(f"{self.name}: Тьфу ты, сожрали червя\n", flush=True)
                else:
                    print(f"{self.name}:Ага, у меня {fish}\n", flush=True)
                    catch[fish] += 1

            print(f"Итого рыбак {self.name} поймал:\n")
            for fish, count in catch.items():
                print(f"{fish} - {count}")
        except Exception as exc:
            print(exc)


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name="Коля", worms=10)
print('Они пошли на рыбалку ...........................................\n')


vasya.start()
kolya.start()

print("Ждем, пока они вернутся......................................\n")


vasya.join()
kolya.join()


print("Итак, они вернулись .........................................\n")
