import threading
from datetime import datetime

# CÂU 1 
print("=== Câu 1: Tạo mảng A có n = 11 phần tử, phần tử cuối là 1000 ===")
n = 11
k = 4
A = [10, 20, 300, 450, 12, 999, 678, 900, 850, 300, 1000]
print("Mảng A =", A)

# CÂU 2
print("\n=== Câu 2: Tạo", k, "luồng cùng tìm max toàn bộ mảng ===")
max_results_all = [None] * k
lock = threading.Lock()

def find_max_all(index, thread_id, data):
    res = max(data)
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"T{thread_id}:{res}:{timestamp}")
    with lock:
        max_results_all[index] = res

threads_all = []
for i in range(k):
    t = threading.Thread(target=find_max_all, args=(i, i + 1, A))
    threads_all.append(t)
    t.start()

for t in threads_all:
    t.join()

# CÂU 3
print("\n=== Câu 3: Chia A thành", k, "đoạn riêng rẽ, mỗi luồng tìm max từng đoạn ===")
chunk_size = n // k
max_results_chunks = [None] * k

def find_max_chunk(index, thread_id, sub_data):
    res = max(sub_data)
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"T{thread_id}:{res}:{timestamp}")
    with lock:
        max_results_chunks[index] = res

threads_chunks = []
for i in range(k):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < k - 1 else n
    chunk = A[start:end]
    t = threading.Thread(target=find_max_chunk, args=(i, i + 1, chunk))
    threads_chunks.append(t)
    t.start()

for t in threads_chunks:
    t.join()

# CÂU 4
print("\n=== Câu 4: Luồng chính tổng hợp kết quả ===")

print("\n[Max toàn bộ mảng từ mỗi luồng]:")
for i, val in enumerate(max_results_all):
    print(f"  T{i + 1}: {val}")
print(f"=> Max cuối cùng toàn bộ mảng: {max(max_results_all)}")

print("\n[Max từng đoạn (không giao nhau)]:")
for i, val in enumerate(max_results_chunks):
    print(f"  Đoạn {i + 1}: {val}")
print(f"=> Max lớn nhất trong các đoạn: {max(max_results_chunks)}")
