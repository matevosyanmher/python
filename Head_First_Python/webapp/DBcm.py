import mysql.connector


class UseDatabase:
    """Context manager for connecting to a database"""

    def __init__(self, config: dict) -> None:    # initialize configuration
        self.configuration = config            # store configuration

    def __enter__(self) -> 'cursor':    # return cursor
        self.conn = mysql.connector.connect(**self.configuration)    # connect to database
        self.cursor = self.conn.cursor()
        return self.cursor  # return cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.cursor.commit()         # commit changes
        self.cursor.close()          # close cursor
        self.conn.close()            # close connection

