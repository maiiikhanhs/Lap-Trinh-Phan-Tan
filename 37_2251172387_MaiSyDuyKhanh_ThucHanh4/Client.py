import xmlrpc.client
import random

proxy = xmlrpc.client.ServerProxy("http://172.20.10.10:9000/")
numbers = [random.randint(1, 1000) for _ in range(1)]

print("\nMảng được gửi tới server:")
print("[", ", ".join(map(str, numbers)), "]")

try:
    result = proxy.sum_array(numbers)
    result2 = proxy.square(numbers)
    print("Kết quả từ server:", result, result2)
except Exception as e:
    print("❗ Lỗi Client:", e)
