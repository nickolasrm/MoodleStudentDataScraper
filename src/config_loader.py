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
        'filter' : config['basic data']['participantsFilter'],
        'targets' : {
            'name' : config.getboolean('targets','name'),
            'email' : config.getboolean('targets','email'),
            'days' : config.getboolean('targets','days'),
            'assignments' : config.getboolean('targets','assignments'),
            'assignments_finishing_date' : config.getboolean('targets','assignments_finishing_date')
        }
    }

    print('Config loaded!')

    return cfg