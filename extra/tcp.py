"""
- Reference/s:
    - [Digital Ocean](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- Author/s:
    - Engr. Achilles C. Macunlay, ECE
- Updated:
    - 2022-11-13
"""

import socket
import threading
from typing import Union


def __is_ipv4_valid(ip_address: str) -> bool:
    try:
        socket.inet_aton(ip_address)
        return True
    except:
        return False


class Socket(socket.socket):
    def __init__(
        self,
        family: Union[socket.AddressFamily, int],
        type: Union[socket.SocketKind, int],
        proto: int = -1,
        fileno: Union[int, None] = None,
    ) -> None:
        super().__init__(family, type, proto, fileno)


class TCPClient:
    def __init__(
        self,
        server_hostname: Union[str, None] = None,
        server_port: Union[int, None] = None,
        packet_size_bytes: int = 1024,
    ) -> None:

        self.__packet_size: int = packet_size_bytes

        try:
            self.__tcp_server_hostname: str = socket.gethostbyname(server_hostname)

        except socket.gaierror as e:
            raise ValueError(e)

        if server_port == None:
            raise ValueError(f"Invalid server port: {server_port}")

        self.__tcp_server_port: int = server_port

        self.__tcp_client: Socket = Socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__tcp_client.connect((self.__tcp_server_hostname, self.__tcp_server_port))

    def disconnect(self) -> None:
        self.__tcp_client.close()

    def send_data(self, data: bytes) -> int:
        return self.__tcp_client.send(data)

    def recv_data(self) -> bytes:
        return self.__tcp_client.recv(self.__packet_size)


class TCPServer:
    def __init__(
        self,
        server_hostname: Union[str, None] = None,
        server_port: Union[int, None] = None,
        packet_size_bytes: int = 1024,
        client_count: int = 1,
    ) -> None:

        self.__packet_size: int = packet_size_bytes

        if server_hostname == None:
            raise ValueError(f"Invalid server IP address: {server_hostname}")

        if server_port == None:
            raise ValueError(f"Invalid server port: {server_port}")

        NETWORK_PROTOCOL: socket.AddressFamily = socket.AF_INET
        TRANSPORT_PROTOCOL: socket.SocketKind = socket.SOCK_STREAM
        self.__tcp_server: Socket = Socket(NETWORK_PROTOCOL, TRANSPORT_PROTOCOL)
        self.__tcp_server.bind((server_hostname, server_port))
        self.__tcp_server.listen(client_count)

        self.__tcp_conn, self.__tcp_client = self.__tcp_server.accept()
        self.__session = threading.Thread(target=self.__start_session(), daemon=True)
        self.__session.start()

    def send_data(self, data: bytes) -> int:
        return self.__tcp_conn.send(data)

    def recv_data(self) -> bytes:
        return self.__tcp_conn.recv(self.__packet_size)

    def __end_session(self) -> None:
        self.__tcp_conn.close()

    def __start_session(self) -> None:
        is_running: bool = True
        print(f"Connection with: {self.__tcp_client}")

        while is_running:
            data = self.recv_data()

            if not data:
                break

            print(f"{self.__tcp_client} -> {data}")
            data = input(f"{self.__tcp_server} -> ").encode()
            self.send_data(data)

        self.__end_session()
