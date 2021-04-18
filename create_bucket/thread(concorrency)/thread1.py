import time
import threading

start = time.perf_counter()


def do_something(inp=1):

    print(f"sleeping {inp} second")
    time.sleep(inp)
    print("done sleeping...")


t1 = threading.Thread(target=do_something, args=[1])
t2 = threading.Thread(target=do_something, args=[1])

t1.start()
t2.start()
# do_something()
# do_something()
t1.join()
t2.join()


finish = time.perf_counter()

print(
    f"----------this job is done in {round(finish-start,2)} seconds----------")
