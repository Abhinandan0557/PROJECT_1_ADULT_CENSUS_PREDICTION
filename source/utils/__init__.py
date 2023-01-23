import pandas as pd
from source.logger import logging
from source.exception import sourceException
from source.config import mongo_client
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id",axis=1)
        if "Unnamed: 0" in df.columns:
            logging.info(f"Dropping column: Unnamed: 0 ")
            df = df.drop("Unnamed: 0",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise sourceException(e, sys)