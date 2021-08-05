import random
from collections import defaultdict
from threading import Thread

FISH = (None, "плотва", "окунь", "лещ")


# Определим функцию, эмулирующую рыбалку

def fishing(name, worms, catch):
    #  catch = defaultdict(int)  # автоматическое создание словаря
    for worm in range(worms):
        print(f'{name}: Червяк номер {worm} заброшен...Ждем\n', flush=True)
        """Flush true - для вывода сразу без буферизации"""
        _ = 3**(random.randint(50, 70)*10000)  # Задержка
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}:Тьфу! сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}\n', flush=True)
            catch[fish] += 1


# А теперь создадим второго рыбака, пошедшего на рыбалку одновременно с первым
vasya_catch = defaultdict(int)  # автоматическое создание словаря
kolya_catch = defaultdict(int)
thread = Thread(target=fishing, kwargs=dict(name="Вася", worms=10, catch=vasya_catch))
# target - целевая функция
thread.start()
fishing(name="Коля", worms=10, catch=kolya_catch)  # Основной поток
thread.join()  # Ожидание выполнения неосновного потока

for name, catch in (("Вася", vasya_catch), ("Коля", kolya_catch)):
    print(f"Итого рыбак {name} поймал: \n")
    for fish, count in catch.items():
        print(f"{fish} - {count}")