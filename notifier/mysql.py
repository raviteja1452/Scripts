import MySQLdb
import datetime

class MYSQL:
    db_connection = None

    def __init__(self):
        self.__connect()

    def __connect(self):
        if MYSQL.db_connection is None:
            MYSQL.db_connection = MySQLdb.connect(host="localhost",
                                                  user="root",
                                                  passwd="ravi1234",
                                                  db="notifier")
        return MYSQL.db_connection

    def execute(self,query):
        cursor = MYSQL.db_connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            MYSQL.db_connection.commit()
            return result
        except Exception as e:
            print "Mysql Exception :",e

if __name__ == "__main__":
    mysql = MYSQL()
    print mysql.execute("select * from notifier")
    date = str(datetime.datetime(2017, 1, 9, 1, 6, 4))
    iQuery = " INSERT INTO `notifier` (`date`, `title`, `description`) VALUES ('" + date + "', 'Test', 'Notifier test 8')"
    print mysql.execute(iQuery)
    print mysql.execute("select * from notifier")
    MYSQL.db_connection.close()
    print MYSQL.db_connection
