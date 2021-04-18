import multiprocessing
import time


def do_something(duration=1):
    print(F"start the task number {duration}")
    time.sleep(1)
    print(F"the job has finished {duration}")
    return True


if __name__ == "__main__":
    print("start of the main ....")
    start = time.perf_counter()

    p = []
    for i in range(5):
        pi = multiprocessing.Process(target=do_something, args=(i,))
        pi.start()
        p.append(pi)

    for pi in p:
        pi.join()

    finish = time.perf_counter()
    print(
        F"the end of the main, Total time = {round (finish-start,2)} seconds.")
