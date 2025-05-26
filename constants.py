"""
This script defines all constants used in the experiments.
    - FOLDER_PATH: the path of your BACI dataset.
    - COUNTRY_FILE: the path of the country code csv file.
    - PRODUCT_FILE: the path of the product code csv file.
    - PROD: all product codes you want to filter.
    - VAL: If you only need calculate the value/quantity, you just need include "V"/"Q"; if you want to calculate both, you need to include "V"&"Q".
    - XWJ_NAMES: all column names for the final "XWJ" file.
    - XWN_NAMES: all column names for the final "XWN" file.
    - XIN_NAMES: all column names for the final "XIN" file.
"""
import os

FOLDER_PATH = os.path.join(os.getcwd(), "BACI_HS12_V202501_test")

COUNTRY_FILE = os.path.join(FOLDER_PATH, "country_codes_V202501.csv")

PRODUCT_FILE = os.path.join(FOLDER_PATH, "product_codes_HS12_V202501.csv")

PROD = [121221, 121229]

VAL = ['V', 'Q']

# --- COLUMN NAMES ---
XWJ_NAMES = ['Year', 'Exporter', 'Importer', 'V', 'Q']
XWN_NAMES = ['Year', 'Importer', 'V', 'Q']
XIN_NAMES = ['Year', 'Importer', 'Product', 'V', 'Q']