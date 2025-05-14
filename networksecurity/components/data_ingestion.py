from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Configuration of Data Ingestion Config - config_entity.py
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            # pass
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    # function we using instead of MongoDB
    def load_data_from_local(self):
        """"
        Load Data from local
        """
        try:
            # pass
            # file_path = self.data_ingestion_config.feature_store_file_path # Use raw data file path from config
            file_path = r"D:\personal_workspace\NetworkSecurity\Network_Data\phisingData.csv"
            df = pd.read_csv(file_path)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            # pass
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            
            return dataframe
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            # pass
            train_set , test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info("Performed train test split over dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path,exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test file path.")

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiata_data_ingestion(self):
        try:
            # pass
            dataframe = self.load_data_from_local() 
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_fact = DataIngestionArtifact(
                trained_file_path = self.data_ingestion_config.training_file_path,
                test_file_path = self.data_ingestion_config.testing_file_path
            )
            return data_ingestion_fact
        except Exception as e:
            raise NetworkSecurityException(e,sys)