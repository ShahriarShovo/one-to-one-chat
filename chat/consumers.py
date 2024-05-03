from channels.consumer import AsyncConsumer
from users.models.user import User


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket connected", event)

        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Websocket Received", event)

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected", event)
