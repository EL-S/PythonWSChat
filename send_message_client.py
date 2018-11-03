import asyncio
import websockets
from random import randint
import hashlib

name = ""
while name == "":
    name = input("Name: ")
unique_identifier = hashlib.sha224((str(name)+str(randint(0,10000000000))).encode('utf-8')).hexdigest()[:4]

async def send_message():
    global name,unique_identifier
    async with websockets.connect('ws://localhost:8765') as websocket:
        message = ""
        while message == "":
            message = input("Message: ")
            if message != "":
                await websocket.send("("+unique_identifier+") "+name+": "+message)
                await send_message()
            else:
                pass
        


asyncio.get_event_loop().run_until_complete(send_message())
asyncio.get_event_loop().run_forever()
