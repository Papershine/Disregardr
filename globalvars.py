import chat

# Global Variables
USER_ID = 111111
API_KEY = "6DPAhNDsWGUW70trfsV0)Q((" # HARDCODED
CHAT = chat.ChatClient()
conn = None


def append_key(link): # UNUSED
    return link + "&key=" + API_KEY
