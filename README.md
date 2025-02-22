# Trustless_Trust-P2P-chat-network-
This a Peer-to-Peer Chat Application made by Nityam Gupta, Nitin, Ajay Sonamani. (Group-name: Trustless_less)
We have also done the bonus question.

# P2P Chat Application

This is a simple peer-to-peer (P2P) chat application using Python's `socket` and `threading` modules. It allows users to send and receive messages directly between peers without a centralized server.

## Features
- Start a server to listen for incoming messages.
- Send messages to other peers.
- Keep track of active peers.
- Connect to known peers.

## Requirements
- Python 3.x

## How to Use

### 1. Run the Server
Each peer must run the server to listen for incoming connections. Run the script and enter your IP and port when prompted.
```bash
python p2p_chat.py
```

### 2. Choose an Option from the Menu
Once the server is running, you will see a menu:
```
***** 🛠 MENU *****
1. Send a message
2. View active peers
3. Connect to peers
4. Exit
```

#### Option 1: Send a Message
To send a message to another peer:
1. Choose option `1`.
2. Enter the recipient's IP address and port number.
3. Type your message and press Enter.

#### Option 2: View Active Peers
To see the list of peers that have communicated with you, choose option `2`.

#### Option 3: Connect to Peers
To establish connections with known peers, choose option `3`. This will send a greeting message to each active peer.

#### Option 4: Exit
To stop the program, choose option `4`.

## Notes
- Use `0.0.0.0` as the IP to listen on all available networks.
- Ensure your firewall allows communication over the chosen port.
- Peers must manually exchange IP addresses and ports to initiate communication.

## Example Usage
### Peer 1 (Listening on Port 5000)
```bash
python p2p_chat.py
🔹 Enter your IP address: 192.168.255.32
🔹 Enter your port number: 5000
🔹 Enter your team name: Alpha
```
### Peer 2 (Listening on Port 6000)
```bash
python p2p_chat.py
🔹 Enter your IP address: 192.168.255.98
🔹 Enter your port number: 6000
🔹 Enter your team name: Beta
```
### Sending a Message
Peer 1 sends a message to Peer 2:
```
1. Send a message
 Enter recipient's IP: <Peer 2's IP>
 Enter recipient's port: 6000
 Type your message: Hello from Alpha!
```
Peer 2 receives:
```
Message from <Peer 1's IP>:5000 (Alpha): Hello from Alpha!
```


