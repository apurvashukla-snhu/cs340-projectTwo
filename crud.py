from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter():
    #Connecting to MongoDB client
    def __init__(self,username,password):
        username = urllib.parse.quote_plus('aacuser')
        password = urllib.parse.quote_plus('dw@Mongo!23')
        self.client = MongoClient('mongodb://%s:%s@localhost:46937/AAC' % (username, password))
        self.database = self.client['AAC']
        
    #Implemented Create (C) method
    def create(self, data):
        if data is not None:
            dataDict = self.database.animals.insert_one(data)
            if dataDict != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save,because data parameter is empty")
            
    #Implemented Read (R) method
    def read(self, search=None):
        if search:
            animal_query = self.database.animals.find(search, {"_id":False})
        else:
            animal_query = self.database.animals.find({}, {"_id":False})
            return animal_query
        
    
    #Implemented Update (U) method
    def update(self, value):
        if value is not None:
            if value:
                result = self.database.animals.insert_one(value)
                return result
            else:
                raise Exception("Nothing to update, parameter empty")
    
    #Implemented Delete (D) method
    def delete(self, deleteData):
        if deleteData is not None:
            if deleteData:
                result = self.database.animals.delete(deleteData)
            else:
                raise Exception("Nothing to delete, parameter empty")
