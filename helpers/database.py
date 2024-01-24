from pymongo import MongoClient
import configuration

connection_params = configuration.connection_params

#connect to mongodb
mongoconnection = MongoClient(
    'mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/27017:total_records.register?retryWrites=false'.format(**connection_params)
)


db = mongoconnection.databasename
