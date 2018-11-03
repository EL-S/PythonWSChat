import asyncio
import websockets

connected = set()
remove_queue = []

async def handler(websocket, path):
    global connected, remove_queue
    # Register.
    if websocket not in connected:
        print("New User:",websocket)
        connected.add(websocket)
        print(dir(websocket))
        print("this",websocket.local_address)
        print("this2",websocket.remote_address)
        pong_waiter = await websocket.ping()
        await pong_waiter   # only if you want to wait for the pong
        print(connected)
    try:
        echo = await websocket.recv()
        print(echo)
        for websoc in connected:
            try:
                await websoc.send(echo)
            except:
                # They disconnected
                remove_queue.append(websoc)
                
    except Exception as e:
        print(e)
        remove_queue.append(websocket)
    finally:
        for ws in remove_queue:
            connected.remove(ws)
        remove_queue = []
start_server = websockets.serve(handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
