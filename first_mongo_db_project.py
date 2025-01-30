import pymongo
from tabulate import tabulate
from session18A import Customer
from bson.objectid import ObjectId
class MongoDBHelper:
    def __init__(self, collection = "customers"):

        url = "mongodb+srv://arpit_aggarwal2005:root@myfirstproject.4yjw8fn.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        self.db = client['my_1st_project']
        self.collection = self.db[collection]
        print("MongoDB connected")
    def insert(self,document):
        result = self.collection.insert_one(document = document)
        print("document inserted")
    def delete(self,query):
        result = self.collection.delete_one(query)
        print("document deleted")
    def fetch(self,query):
        document = self.collection.find(query)
        #print("document fetched\n\n")
        #print(tabulate(document, headers="keys", tablefmt="grid"))
        return document
    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print('updated document', result.modified_count)
def main():
    db = MongoDBHelper()
    customer = Customer()
    customer.read_customer_data()
    document = vars(customer)
    #db.insert(document=document)
    query = {"_id": ObjectId('64cdd2c0ede0e3ff1572d70e')}
    #db.delete(query = query)
    db.fetch(query)
    db.update(document,query)
    db.fetch(query)

if __name__== "__main__":
    main()
