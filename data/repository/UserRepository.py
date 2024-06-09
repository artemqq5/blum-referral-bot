from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def add(self, userid, username, firstname, lastname, lang_code, referral_url):
        query = "INSERT INTO `users` (`userid`, `username`, `firstname`, `lastname`, `lang_code`, `referral_url`) VALUES (%s, %s, %s, %s, %s, %s);"
        return self._insert(query, (userid, username, firstname, lastname, lang_code, referral_url))

    def user(self, userid):
        query = "SELECT * FROM `users` WHERE `userid` = %s;"
        return self._select_one(query, (userid,))

    def update_ref_count(self, userid, ref_count):
        query = "UPDATE `users` SET `ref_count` = %s WHERE `userid` = %s;"
        return self._update(query, (ref_count, userid))

    def user_by_link(self, link):
        query = "SELECT * FROM `users` WHERE `referral_url` = %s;"
        return self._select_one(query, (link,))

    def users(self):
        query = "SELECT * FROM `users`;"
        return self._select(query)

    def admins(self):
        query = "SELECT * FROM `users` WHERE `is_admin` = 1;"
        return self._select(query)
