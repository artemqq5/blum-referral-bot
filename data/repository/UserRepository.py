from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def add(self, userid, username, firstname, lastname, lang_code):
        query = "INSERT INTO `users` (`userid`, `username`, `firstname`, `lastname`, `lang_code`) VALUES (%s, %s, %s, %s, %s);"
        return self._insert(query, (userid, username, firstname, lastname, lang_code))

    def user(self, userid):
        query = "SELECT * FROM `users` WHERE `userid` = %s;"
        return self._select_one(query, (userid,))

    def users(self):
        query = "SELECT * FROM `users` WHERE `role` = 'user' ORDER BY `join_at` DESC;"
        return self._select(query)

    def admins(self):
        query = "SELECT * FROM `users` WHERE `role` = 'admin';"
        return self._select(query)
