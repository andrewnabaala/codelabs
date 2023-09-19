import pandas as pd

excel_file = "codelabs/data/TestFiles.xlsx"
all_sheets= pd.read_excel(excel_file, sheet_name=None)

print(all_sheets)
for sheet_name, sheet_data in all_sheets.items():
    output_file = f'codelabs/data/{sheet_name}.xlsx'
    sheet_data.to_excel(output_file, index=False)
