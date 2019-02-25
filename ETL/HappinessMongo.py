# Module used to connect Python with MongoDb
import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.happiness_db


# Query happiness table
# Here, db.happiness refers to the collection 'happiness table '
happiness_tbl = db.happiness_tbl.find()



# Part I
# A dictionary that represents the document to be inserted

# A dictionary that will become a MongoDB document
post = {
    'Country':Country,
    'Region':Region,
    'Happiness Rank':Happiness Rank,
    'Happiness Score':Happiness Score,
    'Standard Error':Standard Error,
    'Economy (GDP per Capita)':Economy (GDP per Capita),
    'Family':Family,
    'Health (Life Expectancy)':Health (Life Expectancy),
    'Freedom':Freedom,
    'Trust (Government Corruption)':Trust (Government Corruption),
    'Generosity':Generosity,
    'Dystopia Residual':Dystopia Residual
}

# Insert document into collection
collection.insert_one(post)


# Verify results:
results = db.happiness_db.find()
for result in results:
    print(result)

