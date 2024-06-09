import uuid

from data.repository.AccessRepository import AccessRepository


class AccessGenerate:

    @staticmethod
    def generate_access(user):
        generated_uuid = str(uuid.uuid4())
        if AccessRepository().create(user['userid'], generated_uuid):
            return generated_uuid
