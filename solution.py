import socket


def make_socket(interface: str) -> socket.socket:
    pass


def receive_frame(sock: socket.socket) -> bytes:
    pass


def close_socket(sock: socket.socket) -> None:
    pass


if __name__ == "__main__":
    # Run with sudo on your Linux machine: sudo python3 solution.py
    # Replace "eth0" with your interface's name (find it with `ip a`).
    sock = make_socket("eth0")
    print(receive_frame(sock))
    close_socket(sock)
