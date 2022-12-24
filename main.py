# Startup script
import requestposts


# Script entry point
if __name__ == '__main__':
    print('Starting Disregardr')

    # load user settings from config file
    print('Loading user settings...')

    # join chat room
    print('Joining chat room...')

    # start post scanning
    print('Starting post scanning service')
    requestposts.start_service()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
