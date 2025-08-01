import threading
import time
import random
from datetime import datetime


# CÂU 1: KHAI BÁO CẤU TRÚC DỮ LIỆU CHIA SẺ

BUFFER_SIZE = 2
buffer = []

full = threading.Semaphore(10)
mutex = threading.Semaphore(1)

def current_time():
    return datetime.now().strftime("%H:%M:%S")


# CÂU 2: LUỒNG SINH DỮ LIỆU

def producer(pid):
    while True:
        time.sleep(random.uniform(0.3, 1.2))
        value = random.randint(1, 100)

        empty.acquire()
        mutex.acquire()
        buffer.append(value)
        mutex.release()
        full.release()

        print(f"P{pid}: Giá trị vừa ghi -> {value} -> {current_time()}4", flush=True)


# CÂU 3: LUỒNG XỬ LÝ DỮ LIỆU (BÌNH PHƯƠNG)

def consumer(cid):
    while True:
        time.sleep(random.uniform(0.3, 1.2))

        full.acquire()
        mutex.acquire()
        if buffer:
            value = buffer.pop(0)
        else:
            value = None
        mutex.release()
        empty.release()

        if value is not None:
            square = value ** 2
            print(f"C{cid}: {value} -> Bình phương = {square} -> {current_time()}", flush=True)


#  CÂU 4: TẠO K + H LUỒNG CHẠY VÔ HẠN

k = int(input("Nhập số luồng sinh dữ liệu (k ≥ 1): "))
h = int(input("Nhập số luồng xử lý dữ liệu (h ≥ 1): "))

for i in range(k):
    threading.Thread(target=producer, args=(i+1,), daemon=True).start()

for i in range(h):
    threading.Thread(target=consumer, args=(i+1,), daemon=True).start()

print(f"\n Đã khởi tạo {k} producer và {h} consumer. Các luồng đang chạy...\n")

while True:
    time.sleep(1)
