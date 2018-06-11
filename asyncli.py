import asyncio

class EchoCli(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        mes = input('>')
        transport.write(mes.encode())
        print('message sent', mes)

    def eof_received(self):
        self.loop.stop()

    def data_received(self,data):
        print('message receive',data.decode())

    def connection_lost(self, exc):
        self.loop.stop()


loop = asyncio.get_event_loop()
message = 'hello'
coro = loop.create_connection(lambda: EchoCli(message, loop), '127.0.0.1', 8000)
loop.run_until_complete(coro)
loop.close()