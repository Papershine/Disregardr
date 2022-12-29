# Startup script
import requestposts
import atexit
import globalvars
import data
import chat


def exit_cleanup():
    print("Closing resources...")
    globalvars.CHAT.client.logout()
    data.close()


# Script entry point
if __name__ == '__main__':
    print('Starting Disregardr')

    # load user settings from config file and database
    print('Loading data...')
    # TODO: load settings
    atexit.register(exit_cleanup)
    data.init()

    # join chat room
    print('Joining chat room...')
    globalvars.CHAT.start()
    # TODO: start listening to chat commands

    # start post scanning
    print('Starting post scanning service')
    requestposts.start_service()

    # TODO: start listening to command line

