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