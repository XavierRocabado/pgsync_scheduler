from environs import collections
import pymongo
import datetime
import time
#from pymongo import connection
#from connection import str_val
from pymongo import MongoClient

cluster = MongoClient()
print(cluster)

db = cluster['Dummy']
print(db)

collection = db['dummy_collection']

while(True):
    ob = collection.insert_one({'Message': "Scheduler code.py", 'Time': datetime.datetime.now().strftime()})
    print("------------------- Added at: " + time.ctime()+ "-----------")
    time.sleep(10)
    print(ob.inserted_id)

