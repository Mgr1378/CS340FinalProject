
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. 
        self.client = MongoClient('mongodb://%s:%s@localhost:53364/?authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        print('Connected to database')

    #Implement create in Crud
    def create(self, data=dict()):
            if data is not None:
                insert_result = self.database.animals.insert_one(data) #data should be dictionary
            else:
                #Raise error
                raise Exception("Nothing to save, data is empty")
            
    #Implement read in Crud
    def read(self, data):
            if data is not None:
                read_result = self.database.animals.find(data, {"_id": False})
                #print("Doc Read")
                return read_result
            else:
                raise Exception("Nothing to find. Target is empty.")


    #U operation for update in CRUD
    def update(self, find=dict(), replace=dict()):
        if find is not None:
                update_result = self.database.animals.update(find, {"$set": replace})
                return json.dumps(str(update_result.modified_count) + ' records updated')                              
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to update, because at least one of the target parameters is empty")       

    #D operation for delete in CRUD
    def delete(self, data=dict()):
        if target is not None:
            delete_result = json.dumps(self.database.animals.remove(data), indent = 4)
            return delete_result
                
            
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to delete, because the target parameter is empty")