import MySQLdb
import MySQLdb._exceptions
import py_openthesaurus.log as log


class MySQLWrapper(object):
    def __init__(self, host, port=3306, user="",
                 passwd="", db="", charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

        self.logger = log.setup_custom_logger(__name__)

        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                        db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
            self.conn.autocommit(True)
        except MySQLdb._exceptions.DatabaseError as error:
            self.logger.warn(
                'Error in establishing connection to the host =  %s, port = %s, user = %s, password = %s, db = %s',
                host, port, user, passwd, db)
            raise error

    def select_database(self, db_name):
        select_db_query = """USE %s"""
        self.conn.query(select_db_query % db_name)

    def close(self):
        self.conn.close()

    def select_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def select_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
