import uuid

from data.repository.AccessRepository import AccessRepository


class AccessGenerate:

    @staticmethod
    def generate_access(user):
        generated_uuid = str(uuid.uuid4())
        comment = f"ref | {user['firstname']}"
        if AccessRepository().create(user['userid'], generated_uuid, comment):
            return generated_uuid

    @staticmethod
    def generate_custom_access(userid, comment, days):
        generated_uuid = str(uuid.uuid4())
        if AccessRepository().create_custom(userid, generated_uuid, comment, days):
            return generated_uuid
