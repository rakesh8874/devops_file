import configparser

configs = configparser.ConfigParser()
configs.read('config.ini')

configs.sections()


class EnvironmentConfigs:
    database = configs['DATABASE']['db']
    postgres_host = configs['DATABASE']['dbHost']
    postgres_user = configs['DATABASE']['dbUser']
    postgres_password = configs['DATABASE']['dbPassword']
    postgres_port = configs['DATABASE']['dbPort']
    postgres_database_name = configs['DATABASE']['dbName']
