from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logging 


class DataValidationTranasformationPipeline:
	def __init__(self) -> None:
		pass
	
	def main(self):
		config = ConfigurationManager()
		data_transformation_config = config.get_data_transfromation_config()
		data_transfomation = DataTransformation(config=data_transformation_config)
		data_transfomation.convert()
