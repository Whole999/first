import socket

HOST = "127.0.0.1"
PORT = 12345

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Эхо-сервер тыңдауда: {HOST}:{PORT}...")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Қосылу орнатылды: {addr}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print(f"Клиент байланысты жапты: {addr}")
                        break
                    print(f"Алынған деректер (байт): {data}")
                    conn.sendall(data)
    except KeyboardInterrupt:
        print("\nСервер тоқтатылды.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()