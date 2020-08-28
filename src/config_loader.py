import configparser

def loadConfig():
    config = configparser.ConfigParser()
    config.read('data-test.cfg')
    return {
        'username': config['login']['username'],
        'password': config['login']['password'],
        'course': config['basic data']['course'],
        'url': config['basic data']['url'],
        'chromedriver': config['basic data']['chromedriver'],
        'filter' : config['basic data']['participantsFilter']
    }