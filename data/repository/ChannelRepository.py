from data.DefaultDataBase import DefaultDataBase


class ChannelRepository(DefaultDataBase):

    def __init__(self):
        super().__init__()

    def get_channel(self, channel_id, ):
        COMMAND_ = "SELECT * FROM `channels` WHERE `channel_id` = %s;"
        return self._select_one(COMMAND_, (channel_id,))

    def add_channel(self, channel_id, title, user_id):
        COMMAND_ = "INSERT INTO `channels` (`channel_id`, `title`, `user_id`) VALUES (%s, %s, %s);"
        return self._insert(COMMAND_, (channel_id, title, user_id))

    def get_all_channels(self):
        COMMAND_ = "SELECT * FROM `channels` ORDER BY `_at` DESC;"
        return self._select(COMMAND_)

    def delete_channel(self, channel_id):
        COMMAND_ = "DELETE FROM `channels` WHERE `channel_id` = %s;"
        return self._delete(COMMAND_, (channel_id, ))
