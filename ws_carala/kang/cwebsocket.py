import websockets
import asyncio
#import hg_camera

async def connect(hg_data):
    async with websockets.connect("ws://localhost:9998") as websocket:
        await websocket.send(hg_data)
        data = await websocket.recv()
        print(data)

def wb(data):
    #print(data)
    asyncio.get_event_loop().run_until_complete(connect(data))

#def main():



'''
if __name__ == "__main__":
    while True:
        main()
'''