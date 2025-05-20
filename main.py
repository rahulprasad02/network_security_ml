from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
import os
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        # pass
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.initiata_data_ingestion()
        logging.info("Data Initiation Completed")
        print(data_ingestion_artifact)
        logging.info("Iniate Data Validation")
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        logging.info("Iniate Data Transformation")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
