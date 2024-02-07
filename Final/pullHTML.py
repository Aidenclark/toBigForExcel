import arcpy
import re

# Set the workspace to your File Geodatabase location
arcpy.env.workspace = r"C:/Users/aclark/Downloads/TexasAllServiceLayerTEST/TexasAllServiceLayer.gdb"

# Feature Class path within the Geodatabase
fc = "Placemarks/Polygons"

# Check for existence of new fields and add them if they don't exist
fields_to_add = ['FID_HTML', 'Id_HTML', 'Supplier_HTML', 'Dual_HTML', 'Area_HTML']
for field in fields_to_add:
    if not arcpy.ListFields(fc, field):
        arcpy.AddField_management(fc, field, "TEXT", field_length=255)
        print(f"Field {field} added.")

# Define a function to extract data using regular expressions
def extract_with_regex(html):
    patterns = {
        'FID': r'<td>FID</td>\s*<td>(.*?)</td>',
        'Id': r'<td>Id</td>\s*<td>(.*?)</td>',
        'Supplier': r'<td>Supplier</td>\s*<td>(.*?)</td>',
        'Dual': r'<td>Dual</td>\s*<td>(.*?)</td>',
        'Area': r'<td>Area</td>\s*<td>(.*?)</td>',
    }
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
        if match:
            data[key] = match.group(1).strip()
        else:
            data[key] = ''  # Default value if pattern not found
    return data

# Update the feature class with extracted data
fields = ['PopupInfo', 'FID_HTML', 'Id_HTML', 'Supplier_HTML', 'Dual_HTML', 'Area_HTML']
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        html_data = row[0]  # The 'PopupInfo' field data
        extracted_data = extract_with_regex(html_data)
        row[1] = extracted_data.get('FID', '')
        row[2] = extracted_data.get('Id', '')
        row[3] = extracted_data.get('Supplier', '')
        row[4] = extracted_data.get('Dual', '')
        row[5] = extracted_data.get('Area', '')
        cursor.updateRow(row)

print("HTML data extraction and field update complete.")
