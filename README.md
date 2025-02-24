# Trustless_Trust-P2P-chat-network-
This a Peer-to-Peer Chat Application made by Nityam Gupta, Nitin, Ajay Sonamani. (Group-name: Trustless_Trust)
We have also done the bonus question.

# P2P Chat Application

A simple peer-to-peer (P2P) chatting application implemented in Python that uses sockets and threading to enable direct messaging between peers without relying on a centralized server.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

This application provides a basic framework for P2P communication. Peers can send messages, discover other active peers, and manage connections dynamically. The system uses a simple command-line interface that allows users to send messages, query active peers, and establish connections with new peers.

---

## Features

- **Direct Peer Communication:** Connect directly to peers using their IP address and port.
- **Peer Discovery:** Automatically detect and manage active, known, and connected peers.
- **Threaded Server:** Uses threading to handle multiple incoming connections concurrently.
- **Dynamic Messaging:** Allows sending of messages, including a special "exit" command to disconnect.
- **Menu-Driven Interface:** Provides an interactive CLI for easy usage.

---

## Requirements

- **Python 3.x**
- Standard Python libraries:
  - `socket`
  - `threading`
  - `time`

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/p2p-chat-app.git
   cd p2p-chat-app
   ```

2. **Ensure Python 3.x is installed:**

   ```bash
   python3 --version
   ```

   or

   ```bash
   python --version
   ```

---

## Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Follow the on-screen instructions:**

   - **Enter your team name:** (Ensure there are no spaces in the name.)
   - **Enter your port number:** This will be used for the local server.
   - **Interact with the menu options:**
     - **1. Send message:** Send a custom message to a peer by providing their IP and port.
     - **2. Query active peers:** View the list of known peers along with their connection status.
     - **3. Connect to active peers:** Establish a connection with peers that are not yet connected.
     - **0. Quit:** Disconnect from all peers by sending an "exit" message and close the application.

3. **Mandatory Peer:**
   - The application is pre-configured with a mandatory peer (`10.206.5.228:6555`) for initial connectivity. Adjust this configuration as needed.

---

## Code Structure

- **Global Variables:**
  - `active_peers`: List of currently active peers.
  - `known_peers`: Set of all known peers.
  - `connected_peers`: Set of peers with an established connection.
  - `peer_names`: Dictionary mapping peer addresses to their names.
  - `lock`: Threading lock for managing concurrent access.

- **Key Functions:**
  - `start_server(port, name)`: Starts the server to listen for incoming peer connections.
  - `handle_client(client_socket, name)`: Handles messages received from other peers.
  - `send_message(ip, port, sender_name, sender_port, message)`: Sends a message to a specific peer.
  - `connect_to_peer(ip, port, sender_name, sender_port)`: Initiates a connection with a peer.
  - `main()`: Manages user interaction, initiates the server thread, and provides the menu for user actions.

---

## Future Enhancements

- **User Interface:** Develop a graphical user interface (GUI) for improved user experience.
- **Security:** Implement encryption for secure peer-to-peer communication.
- **Scalability:** Enhance peer discovery protocols to better support large networks.
- **Reliability:** Add robust error handling and connection recovery mechanisms.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy chatting!




