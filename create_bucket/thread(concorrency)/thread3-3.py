import concurrent.futures
import time


def do_something(duration=1):
    print(F"start task number {duration} ")
    time.sleep(duration)
    print(F" task number {duration} done!!")
    return duration


if __name__ == "__main__":
    print("the main program has started ...")
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as excecuter:
        x = (1, 2, 3, 4, 7)
        result = excecuter.map(do_something, x)

    finish = time.perf_counter()

    print(
        f"the main program has just finished , the total duration is {round(finish-start,2) } seconds")
