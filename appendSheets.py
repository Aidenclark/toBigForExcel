import pandas as pd

# Load the Excel sheets
sheet1 = pd.read_excel('path_to_your_first_excel_file.xlsx', sheet_name='YourFirstSheetName')
sheet2 = pd.read_excel('path_to_your_second_excel_file.xlsx', sheet_name='YourSecondSheetName')

# Append sheet2 to sheet1
combined_sheet = sheet1.append(sheet2, ignore_index=True)

# Save the combined sheet to a new Excel file
combined_sheet.to_excel('combined_excel_file.xlsx', index=False)
