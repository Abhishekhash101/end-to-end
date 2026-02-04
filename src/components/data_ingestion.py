import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException

from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion")
            # Read dataset
            df = pd.read_csv(r"notebook/data/StudentsPerformance.csv")
            logging.info("Dataset read successfully")

            # Create artifacts directory
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # Save raw data
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )
            logging.info("Raw data saved")

            # Train-test split
            train_df, test_df = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save train and test data
            train_df.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )
            test_df.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error occurred in data ingestion", exc_info=True)
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transfomation=DataTransformation()
    data_transfomation.initiate_data_transformation(train_data,test_data)


