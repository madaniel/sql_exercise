import psycopg2
from config import config


class PostgresConnectionHandler(object):

    def __init__(self):
        self.cursor = None
        self.connection = None

    @staticmethod
    def get_config():
        return config(filename='database.ini')

    def connect(self):
        try:
            # read connection parameters
            params = self.get_config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.connection = psycopg2.connect(**params)

            # create a cursor
            self.cursor = self.connection.cursor()

            # execute a statement
            self.cursor.execute('SELECT version()')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            print('Cursor is closed.')

        # close the communication with the PostgreSQL
        if self.connection:
            self.connection.close()
            self.connection = None
            print('Database connection closed.')


class PostgresDatabaseHandler(object):

    def __init__(self, connection: PostgresConnectionHandler):
        connection.connect()
        self.connection = connection

    def __del__(self):
        self.connection.disconnect()

    def run_command(self, command: str):
        cursor = self.connection.cursor
        cursor.execute(command)
        return cursor.fetchall()
