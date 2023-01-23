from source.logger import logging
from source.exception import sourceException
from source.utils import get_collection_as_dataframe
import sys,os
from source.entity import config_entity
#from source.components.data_ingestion import DataIngestion


def test_logger_and_exception():
    try:
        get_collection_as_dataframe(database_name="adult_census",collection_name="final_data")
        #logging.info("Satrting the test_logger_and_exception")
        #result=3/0
        #print(result)
        #logging.info("Stopping the test_logger_and_exception")
    except Exception as e:
        print(e)
        #logging.debug("Stopping the test_logger_and_exception")
        #raise sourceException(e, sys)

'''
if __name__=="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)
'''       

if __name__=="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        #data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        #print(data_ingestion.initiate_data_ingestion())
    except Exception as e:
        print(e)
       