import asyncio
from caseus import Client, enums
from caseus.secrets import Secrets
from caseus.util.crypto import shakikoo
from caseus.packets import clientbound, serverbound

async def main():
    s = Secrets.load_from_leaker_swf(
        "TFMSecretsLeaker.swf",
        debug_standalone="flashplayerdebugger.exe"
    )
    u = "Zhodisov"
    p = ""
    phash = shakikoo(p)
    sroom = "*Zhodisov"
    c = Client(
        secrets=s,
        username=u,
        password_hash=phash,
        start_room=sroom,
        system_language="en",
        desired_language="en",
        connect_to_satellite=True,
    )
    async def on_con(server, packet):
        print("Connected to server")
    async def on_log(server, packet):
        await c.satellite.write_packet(
            serverbound.JoinRoomPacket,
            community="en",
            name="*Zhodisov",
            password="",
            auto=False,
            customization=None
        )
    async def on_room(server, packet):
        print(f"Room: {packet.raw_name}")
        await c.satellite.write_packet(
            serverbound.RoomMessagePacket,
            message="Zhodisov 🐭"
        )
    c.register_packet_listener(on_con, clientbound.HandshakeResponsePacket)
    c.register_packet_listener(on_log, clientbound.LoginSuccessPacket)
    c.register_packet_listener(on_room, clientbound.JoinedRoomPacket)

    await c.start()

    while True:
        await asyncio.sleep(1)

asyncio.run(main())