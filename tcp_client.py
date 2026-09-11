# Author: Ali Seitkaziyev
import socket

HOST = "127.0.0.1"
PORT = 12345  # Серверде ашық порт

def main():
    try:
        # 1. TCP сокетін құру (IPv4, TCP ағыны)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Сокет құру мүмкін болмады: {e}")
        return

    try:
        # 2. Серверге қосылу (connect)
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Қате: серверге қосылу мүмкін болмады (сервер өшірулі немесе порт бос емес).")
        s.close()
        return
    except socket.timeout:
        print("Қате: қосылу уақыты аяқталды (timeout).")
        s.close()
        return
    except socket.error as e:
        print(f"Қосылу қатесі: {e}")
        s.close()
        return

    print(f"{HOST}:{PORT} серверіне қосылдыңыз. Шығу үшін 'exit' деп жазыңыз.")

    try:
        while True:
            # Пайдаланушыдан хабарлама сұрау
            message = input("Жіберетін хабар: ")
            if message.lower() == "exit":
                print("Байланыс жабылуда...")
                break

            try:
                # 3. Жолды UTF-8 кодировкасында байтқа айналдырып, толық жіберу
                s.sendall(message.encode("utf-8"))
            except socket.error as e:
                print(f"Деректерді жіберу қатесі: {e}")
                break

            try:
                # 4. Серверден жауапты қабылдау (бөлінген буфер 1024 байт)
                response = s.recv(1024)
            except socket.error as e:
                print(f"Деректерді қабылдау қатесі: {e}")
                break

            if not response:
                # Сервер байланысты жапқан жағдайда (0 байт қайтса)
                print("Сервер байланысты жапты.")
                break

            # 5. Байттарды қайтадан UTF-8 жолына түрлендіріп экранға шығару
            print(f"Эхо-жауап: {response.decode('utf-8')}")

    finally:
        # 6. Сокетті міндетті түрде жабу
        s.close()
        print("Сокет жабылды.")

if __name__ == "__main__":
    main()