import configparser

def configRead(section,key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/config.cfg')
    return config.get(section,key)
#print(configRead('Details','APP_URL'))

def ElementsRead(section,key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/Elements.cfg')
    return config.get(section,key)