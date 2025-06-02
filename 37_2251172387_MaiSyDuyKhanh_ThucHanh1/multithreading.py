import threading
import random
from datetime import datetime

n = 11
A = [random.randint(1, 999) for _ in range(n-1)]
A.append(1000)

print("Mảng A: ", A)

k = 4
local_maxima = [None] * k

def find_local_max(thread_id, sub_array, result_index):
    local_max = max(sub_array)  
    timestamp = datetime.now().strftime('%H:%M:%S')  
    print(f"T{thread_id}: {local_max} : {timestamp}\n", flush=True)
    local_maxima[result_index] = local_max

threads = []
chunk_size = n // k

for i in range(k):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < k - 1 else n
    t = threading.Thread(target=find_local_max, args=(i + 1, A[start:end], i))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

global_max = max(local_maxima)
print(f"\nMax toàn mảng là: {global_max}")
