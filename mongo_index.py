"""
    This file is for initiate mongodb situation

    When you want to save book file in file system,then you don't need sharding cluster,that the database design is:
    database:nurse_user
    collections:user
    fields:
        user:
            ID:string
            bio:string
            kred_influence:int
            Outreach_level:int
    index:
        ID

    So what this do is to delete books_fs if it has existed,and create index for it.
"""

import types
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

class mongo_indexor(object):
    def __init__(self, dbname, dbcollection, index_array):
        self.db_name = dbname
        self.db_collection = dbcollection
        db_host = "localhost"
        db_port = 27017
        self.client = MongoClient(db_host, db_port)
        self.indices = index_array

    def create_index(self):
        """
            create index for nurse_user.users
        """
        client = self.client
        db_name = self.db_name
        # print(db_name)
        db_collection = self.db_collection
        for index in self.indices:
            client[db_name][db_collection].create_index([(index, ASCENDING)])
        # client.db_collection.db_collection.create_index([("ID", ASCENDING)])
        # for k, v in INDEX.items():
        #     for key, kwargs in v.items():
        #         client[DATABASE_NAME][k].ensure_index(list(key) if type(key)==types.TupleType else key, **kwargs)

def main():
    indices1 = ['screen_name', 'ID']
    indexor1 = mongo_indexor(dbname='nurse_users_2', dbcollection='users', index_array=indices1)
    # drop_database(DATABASE_NAME)
    indexor1.create_index()

if __name__ == "__main__":
    main()
