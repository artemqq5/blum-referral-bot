from data.DefaultDataBase import DefaultDataBase


class PostRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def add(self, name, year, temp, desc, user_id, identify):
        query = "INSERT INTO `post` (`name`, `year`, `temp`, `desc`, `user_id`, `identify`) VALUES (%s, %s, %s, %s, %s, %s);"
        return self._insert(query, (name, year, temp, desc, user_id, identify))

    def post(self, identify):
        query = "SELECT * FROM `post` WHERE `identify` = %s;"
        return self._select_one(query, (identify,))
