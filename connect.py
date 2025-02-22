import socket
import threading

peer_list = set()

def start_server(my_ip: str, my_port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((my_ip, my_port))
        server.listen(5)
        print(f" Server started on {my_ip}:{my_port}")
        
        while True:
            client_socket, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()

def handle_client(client_socket: socket.socket, addr: tuple):
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            parts = message.split(" ", 2)
            if len(parts) == 3:
                sender_info, team_name, msg = parts
                sender_ip, sender_port = sender_info.split(":")
                peer_list.add((sender_ip, int(sender_port)))
                print(f"\n Message from {sender_ip}:{sender_port} ({team_name}): {msg}")
            else:
                print("\n Malformed message received")
    except Exception as e:
        print(f" Error processing message: {e}")
    finally:
        client_socket.close()

def send_message(target_ip: str, target_port: int, my_port: int, team_name: str, msg: str):
    try:
        my_ip = socket.gethostbyname(socket.gethostname())
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((target_ip, target_port))
            client.send(f"{my_ip}:{my_port} {team_name} {msg}".encode())
            print(f" Message sent to {target_ip}:{target_port}")
            response = client.recv(1024).decode().strip()
            if response:
                print(f" Response from peer: {response}")
    except Exception as e:
        print(f" Could not send message to {target_ip}:{target_port} → {e}")

def query_peers():
    if peer_list:
        print("\n Active Peers:")
        for ip, port in peer_list:
            print(f" {ip}:{port}")
    else:
        print("\n No active peers found.")

def connect_to_peers(my_port: int, team_name: str):
    if not peer_list:
        print("\n No known peers to connect to.")
        return
    for peer_ip, peer_port in peer_list:
        print(f" Connecting to {peer_ip}:{peer_port}...")
        send_message(peer_ip, peer_port, my_port, team_name, "Hello, peer! Connecting...")

def main():
    my_ip = input("🔹 Enter your IP address (Use 0.0.0.0 to listen on all networks): ").strip()
    my_port = int(input("🔹 Enter your port number: ").strip())
    team_name = input("🔹 Enter your team name: ").strip()
    threading.Thread(target=start_server, args=(my_ip, my_port), daemon=True).start()
    
    while True:
        print("\n***** 🛠 MENU *****")
        print("1️. Send a message")
        print("2. View active peers")
        print("3. Connect to peers")
        print("4. Exit")
        
        choice = input("🔹 Choose an option: ").strip()
        if choice == "1":
            target_ip = input(" Enter recipient's IP: ").strip()
            target_port = int(input(" Enter recipient's port: ").strip())
            msg = input(" Type your message: ").strip()
            send_message(target_ip, target_port, my_port, team_name, msg)
        elif choice == "2":
            query_peers()
        elif choice == "3":
            connect_to_peers(my_port, team_name)
        elif choice == "0":
            print(" Exiting...")
            break

if __name__ == "__main__":
    main()
