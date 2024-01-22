import configparser

config = configparser.RawConfigParser()
config.read('Configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getapplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getuserpassword():
        password = config.get('common info', 'password')
        return password
