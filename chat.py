# !!IMPORTANT!! Current ChatExchange version: commit 12b3cc, Apr 20 2022

import chatexchange.client
import chatexchange.events
import getpass

from chatexchange.rooms import Room


class ChatClient:
    room = None
    client = None

    def __init__(self):
        return

    def start(self):
        host_id = 'stackoverflow.com'
        room_id = '250724'  # hardcoded test bot room

        print("Beginning chat login")
        email = input("Email: ")
        password = getpass.getpass("Password: ")
        self.client = chatexchange.client.Client(host_id)
        self.client.login(email, password)

        self.room = self.client.get_room(room_id)
        self.room.join()
        self.room.watch(on_message)
        print("Joined room " + room_id + " on " + host_id + " and listening!")
        self.room.send_message("[ Disregardr ] started!")

    def send_message(self, message):
        self.room.send_message(message)


def on_message(message, client):
    if not isinstance(message, chatexchange.events.MessagePosted):
        # Ignore non-message_posted events.
        print("event: %r", message)
        return

    print("")
    print(">> (%s) %s" % (message.user.name, message.content))
    if message.content.startswith('@Pape'):
        print("Tagged!")
