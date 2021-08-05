import os
import random
from collections import defaultdict
from multiprocessing import Process, Pipe, Queue
from queue import Empty

FISH = (None, "плотва", "окунь", "лещ")

def fishing(name, worms):
    print(f"{name} parent process", os.getppid())  # Идентификатор процесса
    print(f"{name}  process id", os.getpid())
    catch = defaultdict(int)
    for worm in range(worms):
        print(f'{name}: Червяк номер {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f"{name}: Тьфу! сожрали червяка", flush=True)
        else:
            print(f"{name}: Ага! у меня {fish}", flush=True)
            catch[fish] += 1

    print(f"Итого рыбак {name} поймал")
    for fish, count in catch.items():
        print(f"  {fish} - {count} ")


if __name__ == '__main__':
    # Для windows это условие обязательно
    # Второй рыбак ловят в отдельном процессе
    proc = Process(target=fishing, kwargs=dict(name="Вася", worms=10))
    proc.start()

    fishing(name="Коля", worms=10)

    proc.join()










