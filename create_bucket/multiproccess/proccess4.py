import multiprocessing
import time
import concurrent.futures


def do_something(duration=1):
    print(F"start the task number {duration}")
    time.sleep(duration)
    print(F"the job has finished {duration}")
    return duration


if __name__ == "__main__":
    print("start of the main ....")
    start = time.perf_counter()
    list_task = [1, 2, 3, 4, 6, 1, 1, 5]
    with concurrent.futures.ProcessPoolExecutor() as executer:
        result = executer.map(do_something, list_task)

    for item in result:
        print(item)

    finish = time.perf_counter()
    print(
        F"the end of the main, Total time = {round (finish-start,2)} seconds.")
