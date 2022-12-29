# !!IMPORTANT!! Current ChatExchange version: commit 12b3cc, Apr 20 2022

import chatexchange.client
import chatexchange.events
import getpass
import chatcommands

from chatexchange.rooms import Room


class ChatClient:
    room = None
    client = None

    def __init__(self):
        return

    def start(self):
        host_id = 'stackoverflow.com'
        room_id = '250724'  # hardcoded test bot room

        print("[ChatScanner] Beginning chat login")
        email = input("Email: ")
        password = getpass.getpass("Password: ")
        self.client = chatexchange.client.Client(host_id)
        self.client.login(email, password)

        self.room = self.client.get_room(room_id)
        self.room.join()
        self.room.watch(on_message)
        print("[ChatScanner] Joined room %s on %s and listening!" % (room_id, host_id))
        self.send_message("started!")

    def send_message(self, message):
        self.room.send_message("[ [Disregardr](https://bit.ly/disregardr) ]" + message)


def on_message(message, client):
    if not isinstance(message, chatexchange.events.MessagePosted):
        # Ignore non-message_posted events.
        print("[ChatScanner] event: %r", message)
        return

    print("\n[ChatScanner] >> (%s) %s" % (message.user.name, message.content))
    if message.content.startswith('@Pape'):
        print("[ChatScanner] Command Received")
        command = message.content.split(' ')[1:]
        match command:
            case ['alive']:
                chatcommands.alive(message)
            case _:
                print("[ChatScanner] Unknown Command")
