# Startup script
import requestposts
import atexit
import chat
import globalvars


def exit_cleanup():
    print("Shutting down Disregardr...")
    globalvars.CHAT.client.logout()


# Script entry point
if __name__ == '__main__':
    print('Starting Disregardr')

    # load user settings from config file
    print('Loading user settings...')
    atexit.register(exit_cleanup)

    # join chat room
    print('Joining chat room...')
    globalvars.CHAT.start()
    # TODO: start listening to chat commands

    # start post scanning
    print('Starting post scanning service')
    requestposts.start_service()

    # TODO: start listening to command line

