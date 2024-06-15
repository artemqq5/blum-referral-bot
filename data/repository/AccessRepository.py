from data.DefaultDataBase import DefaultDataBase


class AccessRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def create(self, userid, uuid_key, comment):
        query = "INSERT INTO `access` (`userid`, `uuid_key`, `comment`) VALUES (%s, %s, %s);"
        return self._insert(query, (userid, uuid_key, comment))

    def create_custom(self, userid, uuid_key, comment, days):
        query = "INSERT INTO `access` (`userid`, `uuid_key`, `comment`, `days`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (userid, uuid_key, comment, days))

    def access(self, uuid_key):
        query = "SELECT * FROM `access` WHERE `uuid_key` = %s;"
        return self._select_one(query, (uuid_key,))

    def accesses(self):
        query = "SELECT * FROM `access`;"
        return self._select(query)

    def delete(self, uuid_key):
        query = "DELETE FROM `access` WHERE `uuid_key` = %s;"
        return self._delete(query, (uuid_key,))
