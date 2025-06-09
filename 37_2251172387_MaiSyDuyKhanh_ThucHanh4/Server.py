from xmlrpc.server import SimpleXMLRPCServer

def sum_array(numbers):
    print(f"Đã nhận danh sách số từ client (tính tổng): {numbers}")
    result = sum(numbers)
    print(f"Gửi lại tổng: {result}")
    return result

ip="0.0.0.0"
port=42069
server = SimpleXMLRPCServer((ip, port), allow_none=True)
server.register_function(sum_array, "sum_array")

print(f"Server RPC đang chạy và chờ yêu cầu tại cổng {port}...")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer đã được dừng bởi người dùng (Ctrl+C)")
