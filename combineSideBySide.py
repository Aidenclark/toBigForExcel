import pandas as pd

# Load the Excel sheets
sheet1 = pd.read_excel('path_to_first_excel_file.xlsx', sheet_name='FirstSheetName')
sheet2 = pd.read_excel('path_to_second_excel_file.xlsx', sheet_name='SecondSheetName')

# Aligning rows by reindexing the shorter dataframe
max_rows = max(len(sheet1), len(sheet2))
sheet1 = sheet1.reindex(range(max_rows))
sheet2 = sheet2.reindex(range(max_rows))

# Concatenate sheets side by side
combined_sheet = pd.concat([sheet1, sheet2], axis=1)

# Save the combined sheet to a new Excel file
combined_sheet.to_excel('combined_excel_file.xlsx', index=False)
