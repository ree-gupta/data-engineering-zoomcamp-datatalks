"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('green_taxi_etl', 'load_api_data_green', 'output_0')

vendor_ids = df['VendorID'].unique()

print(vendor_ids)