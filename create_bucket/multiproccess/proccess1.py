# multi processing

import multiprocessing
import time


def do_something(task_id):
    print(f"start processing task {task_id}")
    time.sleep(task_id)
    print(f"finish processing task {task_id}")
    return task_id


if __name__ == "__main__":
    print("main process statred ....")
    t1 = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something, args=(2,))
    p2 = multiprocessing.Process(target=do_something, args=(1,))
    p3 = multiprocessing.Process(target=do_something, args=(3,))
    p4 = multiprocessing.Process(target=do_something, args=(4,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    # p3.join()
    # p4.join()

    t2 = time.perf_counter()
    print(f"Proccess has just finished in {round(t2-t1,2)} second(s)")
