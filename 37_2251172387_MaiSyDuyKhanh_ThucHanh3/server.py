import socket

def handle_data(data):
    numbers = list(map(int, data.strip().split()))
    result = max(numbers)  # Tìm số lớn nhất
    return str(result)

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_sock:
            temp_sock.connect(("8.8.8.8", 80))
            return temp_sock.getsockname()[0]
    except:
        return "localhost"

HOST = "172.20.10.8"
PORT = 12345

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        server_ip = get_local_ip()
        print(f"Server is listening on {server_ip}:{PORT} (bound to 0.0.0.0)")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(4096).decode()
                if not data:
                    continue
                print(f"Received data: {data}")  # <-- In ra dữ liệu nhận được
                result = handle_data(data)
                print(f"Sending result: {result}")
                conn.sendall(result.encode())
except KeyboardInterrupt:
    print("\nServer stopped by user (Ctrl+C)")
except Exception as e:
    print(f"Unexpected error: {e}")
