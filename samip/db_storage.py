from mongoengine import connect


class DBStorage():
    mongo_db = None

    def init_storage(self, config):
        self.mongo_db = self.mongo_db if self.mongo_db else connect(host= config['MONGO_CONNECTION_URL'])

storage = DBStorage()
