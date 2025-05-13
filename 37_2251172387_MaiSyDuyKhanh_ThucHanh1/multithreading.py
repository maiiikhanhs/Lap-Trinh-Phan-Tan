import threading
import random
from datetime import datetime

# Câu 1: Tạo mảng A với N > 100 phần tử số ngẫu nhiên
N = 150
A = [random.choice([
    random.randint(1, 1000),              
    round(random.uniform(1.0, 1000.0), 2) 
]) for _ in range(N)]

numeric_elements = A  

# Câu 2: Tạo 1 luồng tìm max toàn bộ mảng 
max_result = None
results_lock = threading.Lock()

def find_max(thread_id, data):
    global max_result
    res = max(data)
    print(f"T{thread_id}: {res} : {datetime.now().strftime('%H:%M:%S')}")
    with results_lock:
        max_result = res

# Câu 3: Chia mảng thành 2 phần, tìm max nửa đầu
mid = len(numeric_elements) // 2
max_half = None

def find_max_half(thread_id, sub_data):
    global max_half
    res = max(sub_data)
    print(f"T{thread_id}: {res} : {datetime.now().strftime('%H:%M:%S')}")
    with results_lock:
        max_half = res

# Tạo và chạy luồng 
t1 = threading.Thread(target=find_max, args=(1, numeric_elements))    
t2 = threading.Thread(target=find_max_half, args=(2, numeric_elements[:mid]))  

t1.start()
t2.start()

t1.join()
t2.join()

# Câu 4: Luồng chính tổng hợp kết quả
print("\n--- Kết quả tổng hợp ---")
print(f"Max toàn bộ: {max_result}")
print(f"Max nửa đầu: {max_half}")
