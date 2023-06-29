# from textSummarizer.logging import logger

# logger.info("Welcome to our custom logging")

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.logging import logger


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f" >>>> stage{STAGE_NAME} <<<<< started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f" >>>>> stage{STAGE_NAME} completed <<<<<<\n\mx=========x")
except Exception as e:
    logger.exception(e)
    raise e