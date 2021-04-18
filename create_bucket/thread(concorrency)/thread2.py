import threading
import time


def do_something(duration=1):
    print(F"start the task number {duration}")
    time.sleep(duration)
    print(F"the job has finished {duration}")
    return True


if __name__ == "__main__":
    print("start of the main ....")
    start = time.perf_counter()
    threads = []
    for i in range(10):
        t = threading.Thread(target=do_something, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    finish = time.perf_counter()
    print(
        F"the end of the main, Total time = {round (finish-start,2)} seconds.")
