import arcpy
import pandas as pd

gdb_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/meters.gdb'
arcpy.env.workspace = gdb_path

table_name = 'PLEASEE'  # table name

# Convert data to DataFrame and export to Excel
def export_to_excel(data, output_path):
    # Extract field names
    fields = [field.name for field in arcpy.ListFields(table_name)]

    df = pd.DataFrame(data, columns=fields)

    df.to_excel(output_path, index=False)

all_data = [row for row in arcpy.da.SearchCursor(table_name, "*")]

half_index = len(all_data) // 2

export_to_excel(all_data[:half_index], r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/output_part1.xlsx')

export_to_excel(all_data[half_index:], r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/output_part2.xlsx')

print(f'Table {table_name} has been exported to two Excel files: output_part1.xlsx and output_part2.xlsx')
