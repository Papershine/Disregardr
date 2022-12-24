# Startup script
import requestposts

def print_hi(name):
    print(f'Hi, {name}!\n')
    print('Disregardr starting up...')


# Script entry point
if __name__ == '__main__':
    print_hi('user')

    # load user settings from config file
    print('Loading user settings...')

    # join chat room
    print('Joining chat room...')

    # start post scanning
    print('Starting post scanning service')
    requestposts.start_service()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
