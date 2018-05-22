import MySQLdb


class Database:

    def __init__(self, db_name):
        pass
        #self._conn = MySQLdb.connect(host="10.20.2.234", user="pi", password="neueda01", db=db_name)
        #self._c = self._conn.cursor()

    @property
    def conn(self):
        return self._conn

    @property
    def c(self):
        return self._c


if __name__ == "__main__":
    print "yarp"
