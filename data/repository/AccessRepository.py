from data.DefaultDataBase import DefaultDataBase


class AccessRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def create(self, userid, uuid_key):
        query = "INSERT INTO `access` (`userid`, `uuid_key`) VALUES (%s, %s);"
        return self._insert(query, (userid, uuid_key))

    def access(self, userid):
        query = "SELECT * FROM `access` WHERE `userid` = %s;"
        return self._select_one(query, (userid,))

    def accesses(self):
        query = "SELECT * FROM `access`;"
        return self._select(query)
