import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Сканує один порт на заданому хості."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Встановлення тайм-ауту в 1 секунду
            s.connect((host, port))
            print(f"[+] Порт {port} відкритий")
            return port
    except (socket.timeout, ConnectionRefusedError):
        return None

def main():
    print("Сканер портів на сокетах")
    host = input("Введіть адресу хоста для сканування (наприклад, 192.168.1.1): ")
    start_port = int(input("Введіть початковий порт: "))
    end_port = int(input("Введіть кінцевий порт: "))
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)

    print("\nВідкриті порти:")
    if open_ports:
        for port in open_ports:
            print(f"Порт {port}")
    else:
        print("Не знайдено відкритих портів.")

if __name__ == "__main__":
    main()
