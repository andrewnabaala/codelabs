import pandas as pd 
import numpy as np
from functions.functions import generate_email

excel_file = "data/TestFiles.xlsx"
all_sheets= pd.read_excel(excel_file, sheet_name=None)

for sheet_name, sheet_data in all_sheets.items():
    sheet_data["Email Address"] = sheet_data.apply(generate_email, axis=1)
    output_file = f'data/{sheet_name}.tsv'
    sheet_data.to_csv(output_file, sep="\t",  index=False)


