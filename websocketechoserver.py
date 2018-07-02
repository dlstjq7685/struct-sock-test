import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(websockets)
        await websocket.send(message)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8000))
asyncio.get_event_loop().run_forever()
