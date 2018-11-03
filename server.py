import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    # Register.
    print("uwu")
    connected.add(websocket)
    try:
        echo = await websocket.recv()
        print(echo)
        print(connected)
        for websoc in connected:
            websoc.send(echo)
    finally:
        # Unregister.
        # connected.remove(websocket)
        pass

start_server = websockets.serve(handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
