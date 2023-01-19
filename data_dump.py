import pymongo
import pandas as pd
import json

'''
#provide the mongodb localhost url to connct python to mongodb
#client=pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")

#DATA_FILE_PATH = "D://proj_1_adult_census_prediction//data//processed//final_data_with_SMOTE.csv"
#DATABASE_NAME = "adult"
#COLLECTION_NAME = "final_train"
'''

'''
#if __name__=="__main__":
    #df=pd.read_csv("D://proj_1_adult_census_prediction//data//processed//final_data_with_SMOTE.csv")
    #df.reset_index(drop=True, inplace=True,)
    #print(df)
    #json_df=df.to_json(orient="records")
    #data=json.loads(json_df)
    #print(data)
    #client=pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")
    #database=client[DATABASE_NAME]
    #collection=database[COLLECTION_NAME]
    #collection.insert_many(data)

    #convert dataframe to jason format so thet we can dump record in mongo db
    #df.reset_index(drop=True, inplace=True)
    #json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])
'''

class MongoDB(object):

    def __init__(self,dbName=None, collectionName=None):
        self.dbName=dbName
        self.collectioName= collectionName
        self.client = pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")
        self.DB = self.client[self.dbName]
        self.collection = self.DB[self.collectioName]


    def InsertData(self,path=None):
        '''
         param path : Path os csv file
        return: None
        '''

        df= pd.read_csv(path)
        data= df.to_dict('records')

        self.collection.insert_many(data)
        print("All the data has been exported to mongoDb server....")

if __name__=="__main__":
    mongodb= MongoDB(dbName="adult_census", collectionName="final_train_with_smote")
    mongodb.InsertData(path= "D://proj_1_adult_census_prediction//data//processed//final_data_with_SMOTE.csv")


