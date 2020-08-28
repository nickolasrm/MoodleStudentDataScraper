import configparser

def loadConfig():
    print('Loading config...')

    config = configparser.ConfigParser()
    config.read('data.cfg')
    cfg = {
        'username': config['login']['username'],
        'password': config['login']['password'],
        'course': config['basic data']['course'],
        'url': config['basic data']['url'],
        'chromedriver': config['basic data']['chromedriver'],
        'filter' : config['basic data']['participantsFilter']
    }

    print('Config loaded!')

    return cfg