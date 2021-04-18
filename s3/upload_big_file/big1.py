import time
import sys

for i in range(5):
    sys.stdout.write(str(i))
    sys.stdout.flush()
    time.sleep(1)
