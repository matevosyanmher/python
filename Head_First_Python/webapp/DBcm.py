import mysql.connector


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    """
    UseDatabase is a context manager that will make a connection to the
    database, and then close the connection when the context is exited.
    """

    def __init__(self, config: dict) -> None:
        """
        Initialize the context manager.
        """
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """
        Connect to the database and return a cursor to the database.
        """
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """
        Close the connection to the database.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)

