import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://localhost:8765') as websocket:
        message = input("Message:")

        await websocket.send(message)
        print(f">sent {message}")
        echo = await websocket.recv()
        print(echo)

async def receive_message():
    print("test")
    async with websockets.connect('ws://localhost:8765') as websocket:
        print("test2")
        while True:
            echo = await websocket.recv()
            print("echo")
            print(f"<received {echo}")

asyncio.get_event_loop().run_until_complete(send_message())
asyncio.get_event_loop().run_until_complete(receive_message())
asyncio.get_event_loop().run_forever()
