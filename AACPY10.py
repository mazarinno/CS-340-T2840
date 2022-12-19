from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://aacuser:123@localhost:38748/AAC')
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data:
            #data should be dictionary
            return self.database.animals.find(data, {"_id": False})
        else:
            return self.database.animals.find({}, {"_id": False})

# create method to implement U in CRUD 
    def update(self, dataOne, dataTwo):
        if dataOne is not None and dataTwo is not None:
            self.database.animals.update(dataOne, { "$set": dataTwo}, {"multi": true})
        else:
            raise Exception("one or more data paramaeters empty, update fail")
            
# create method to implement D in CRUD
    def delete(self, data):
        if data is not None:
            for x in self.database.animals.find(data):
                self.database.animals.delete_one(data)
        else:
            raise Exception("nothing to delete, data parameter empty")