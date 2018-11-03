import asyncio
import websockets

async def receive_message():
    websocket = await websockets.connect('ws://localhost:8765')
    while True:
        try:
            message = await websocket.recv()
            print(message)
        except Exception as e:
            websocket = await websockets.connect('ws://localhost:8765')

asyncio.get_event_loop().run_until_complete(receive_message())
asyncio.get_event_loop().run_forever()
