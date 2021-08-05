import random
import time
from collections import defaultdict
from threading import Thread
#  Сравним время работы многопоточного и однопоточного исполнения


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

                #  _ = worm**10000  # Задержка
                time.sleep(0.01)  #  - завтавить текущий поток заснуть на 0.01 с
                fish = random.choice(FISH)

                if fish is None:
                    pass
                else:

                    catch[fish] += 1

            print(f"Итого рыбак {self.name} поймал:\n")
            for fish, count in catch.items():
                print(f"{fish} - {count}")
        except Exception as exc:
            print(exc)


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = abs(round(ended_at - started_at, 6))
        print(f"Функция {func.__name__} работала {elapsed} секунд")
        return result
    return surrogate


@time_track
def run_in_one_thread(fishers):
    for fisher in fishers:
        fisher.run()

@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ["Васек", "Колян", "Петрович", "Хмурый", "Клава"]
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_thread(fishers)
run_in_threads(fishers)

#  Вывод: многопоточность не всегда дает выигрыш во времени при использовании
#  _=
#  Но если заставить "заснуть весь поток"  с помощью команды sleep, выигрыш будет порядка
#  В 7 раз