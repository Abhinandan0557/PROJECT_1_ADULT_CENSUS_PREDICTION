import pymongo
import pandas as pd
#provide the mongodb localhost url to connct python to mongodb
client=pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "D:/proj_1_adult_census_prediction/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "aps_failure_training_set_1"

if __name__=="__main__":
    #cols_name=['age', 'workclass', 'fnlwgt', 'education', 'education-num',
       #'marital-status', 'occupation', 'relationship', 'race', 'sex',
       #'hours-per-week', 'country', 'salary',error_bad_lines=False,engine="python"]
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
