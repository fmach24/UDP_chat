import asyncio
import socket
import json
from datetime import datetime
BROADCAST_PORT = 9999
RECEIVE_BUFFER_SIZE = 1024

class BroadcastListener:
    def __init__(self):
        self.server_info = None

    async def listen_for_broadcast(self):
        loop = asyncio.get_running_loop()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(('', BROADCAST_PORT))

        print(f"[BROADCAST] Nasłuchiwanie na porcie {BROADCAST_PORT}...")

        while True:
            data, addr = await loop.run_in_executor(None, sock.recvfrom, RECEIVE_BUFFER_SIZE)
            try:
                msg = json.loads(data.decode())
                print(f"[BROADCAST ODEBRANY] {msg}")
                self.server_info = (msg['host'], int(msg['port']))
                break
            except Exception as e:
                print(f"[BŁĄD BROADCASTU] {e}")
        
        sock.close()
        return self.server_info


class ClientProtocol(asyncio.DatagramProtocol):
    def __init__(self,nick):
        self.transport = None
        self.nick = nick

    def connection_made(self, transport):
        self.transport = transport
        print("[KLIENT] Połączenie ustanowione.")

    def datagram_received(self, data, addr):
        decoded = json.loads( data.decode())
        if decoded["type"] == "admin":
            msg = decoded["msg"]
            print(f"[INFO]: {msg}")
            return
        nick = decoded["nick"]
        msg = decoded["msg"]
        time = decoded["stamp"]
        print(f"[{time}] {nick}: {msg}")

    def send_message(self, message, server_addr):
        if self.transport:
            data = {"type":"regular" ,"nick":self.nick, "msg":message, "stamp":datetime.now().strftime("%H:%M")}
            self.transport.sendto(json.dumps(data).encode(), server_addr)


async def input_loop(protocol: ClientProtocol, server_addr):
    while True:
        stamp = datetime.now().strftime("%H:%M")
        msg = await asyncio.to_thread(input, "")
        protocol.send_message(msg, server_addr)


async def main():
    # 1. Odbierz broadcast serwera
    listener = BroadcastListener()
    server_addr = await listener.listen_for_broadcast()

    print(f"[INFO] Serwer znaleziony: {server_addr}")


    # 2. Połącz się z serwerem przez UDP
    nick = input("Podaj swoj nick: ")
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientProtocol(nick),
        local_addr=("0.0.0.0", 0)  # automatyczny port klienta
    )

    try:
        await input_loop(protocol, server_addr)
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())
