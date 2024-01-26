import pandas as pd

def is_similar(value1, value2):
    if pd.isna(value1) or pd.isna(value2):
        return False
    value1, value2 = str(value1)[3:], str(value2)  # Strip "915" from value1

    # Any matching substring of 4 characters
    for i in range(len(value1) - 3):
        if value1[i:i+4] in value2:
            return True
    return False

new_dataset_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/MeteringReport.xlsx' 
new_dataset = pd.read_excel(new_dataset_path)

output1_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/output_part1_copy.xlsx' 
output2_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/output_part2_copy.xlsx'  
output1 = pd.read_excel(output1_path)
output2 = pd.read_excel(output2_path)

combined_output = pd.concat([output1, output2])

# Matched rows
matched_rows = []

for _, new_row in new_dataset.iterrows():
    for _, old_row in combined_output.iterrows():
        if is_similar(new_row['configuration.MacAddress'], old_row['COMM_ID_NB']):
            matched_rows.append({'configuration.MacAddress': new_row['configuration.MacAddress'], 'COMM_ID_NB': old_row['COMM_ID_NB']})
            break  # Remove to find all similar entries, not just the first match

mapped_output = pd.DataFrame(matched_rows)

mapped_output.to_excel(r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/mapped_output.xlsx', index=False)

print("The data has been compared and the results are saved in 'mapped_output.xlsx'")
