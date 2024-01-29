import pandas as pd

def find_matches(df):
    # Create a new column for the output
    df['Matched_Data'] = ''

    # Iterate over the rows in the dataframe
    for index, row in df.iterrows():
        comm_id = row['COMM_ID_NB']
        mac_address = row['configuration.MacAddress'][3:]  # Exclude the first three characters
        matches = []

        # Check for 4-character matches
        for i in range(len(comm_id) - 3):
            for j in range(len(mac_address) - 3):
                if comm_id[i:i+4] == mac_address[j:j+4]:
                    matches.append((mac_address, row['GPS_LATITUDE_TX'], row['GPS_LONGITUDE_TX']))
                    break  # Stop searching after the first match for this row

        # Add matches to the new column
        if matches:
            df.at[index, 'Matched_Data'] = matches

    return df

# Load your Excel file
file_path = 'your_file.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Call the function to find matches
result_df = find_matches(df)

# Save the results to a new Excel file
result_df.to_excel('matched_results.xlsx', index=False)







import pandas as pd

def find_matches(df):
    # Create a new column for the output
    df['Matched_Data'] = ''

    # Convert the columns to string type to handle non-string data
    df['COMM_ID_NB'] = df['COMM_ID_NB'].astype(str)
    df['configuration.MacAddress'] = df['configuration.MacAddress'].astype(str)

    # Iterate over the rows in the dataframe
    for index, row in df.iterrows():
        comm_id = row['COMM_ID_NB']
        mac_address = row['configuration.MacAddress'][3:]  # Exclude the first three characters
        matches = []

        # Check for 4-character matches
        for i in range(len(comm_id) - 3):
            for j in range(len(mac_address) - 3):
                if comm_id[i:i+4] == mac_address[j:j+4]:
                    matches.append((mac_address, row['GPS_LATITUDE_TX'], row['GPS_LONGITUDE_TX']))
                    break  # Stop searching after the first match for this row

        # Add matches to the new column
        if matches:
            df.at[index, 'Matched_Data'] = matches

    return df

# Load your Excel file
file_path = 'your_file.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Call the function to find matches
result_df = find_matches(df)

# Save the results to a new Excel file
result_df.to_excel('matched_results.xlsx', index=False)







import pandas as pd

def find_matches(df):
    # Create new columns for the output
    df['Matched_MacAddress'] = None
    df['Matched_Latitude'] = None
    df['Matched_Longitude'] = None

    # Convert the columns to string type to handle non-string data
    df['COMM_ID_NB'] = df['COMM_ID_NB'].astype(str)
    df['configuration.MacAddress'] = df['configuration.MacAddress'].astype(str)

    # Iterate over the rows in the dataframe
    for index, row in df.iterrows():
        comm_id = row['COMM_ID_NB']
        mac_address = row['configuration.MacAddress'][3:]  # Exclude the first three characters

        # Check for 4-character matches
        for i in range(len(comm_id) - 3):
            for j in range(len(mac_address) - 3):
                if comm_id[i:i+4] == mac_address[j:j+4]:
                    # Update the new columns with matched data
                    df.at[index, 'Matched_MacAddress'] = mac_address
                    df.at[index, 'Matched_Latitude'] = row['GPS_LATITUDE_TX']
                    df.at[index, 'Matched_Longitude'] = row['GPS_LONGITUDE_TX']
                    break  # Stop searching after the first match for this row

    return df
















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

# Path to the Excel file
dataset_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/MeteringReport.xlsx' 
dataset = pd.read_excel(dataset_path)

# Columns to compare
column1 = 'configuration.MacAddress'
column2 = 'COMM_ID_NB'

# Matched rows
matched_rows = []

for _, row in dataset.iterrows():
    if is_similar(row[column1], row[column2]):
        matched_rows.append({column1: row[column1], column2: row[column2]})

mapped_output = pd.DataFrame(matched_rows)

# Save the result
output_path = r'C:/Users/aclark/OneDrive - patrickengineering/Documents/ArcGIS/Projects/Playground/mapped_output.xlsx'
mapped_output.to_excel(output_path, index=False)

print("The data has been compared and the results are saved in 'mapped_output.xlsx'")












import pandas as pd

def find_matches(df):
    # Create new columns for the output
    df['Matched_MacAddress'] = None
    df['Matched_Latitude'] = None
    df['Matched_Longitude'] = None

    # Convert the columns to string type to handle non-string data
    df['COMM_ID_NB'] = df['COMM_ID_NB'].astype(str)
    df['configuration.MacAddress'] = df['configuration.MacAddress'].astype(str)

    # Variables to track matches and non-matches
    match_count = 0
    no_match_count = 0

    # Iterate over the rows in the dataframe
    for index, row in df.iterrows():
        comm_id = row['COMM_ID_NB']
        mac_address = row['configuration.MacAddress'][3:]  # Exclude the first three characters
        match_found = False

        # Check for 4-character matches
        for i in range(len(comm_id) - 3):
            for j in range(len(mac_address) - 3):
                if comm_id[i:i+4] == mac_address[j:j+4]:
                    # Update the new columns with matched data
                    df.at[index, 'Matched_MacAddress'] = mac_address
                    df.at[index, 'Matched_Latitude'] = row['GPS_LATITUDE_TX']
                    df.at[index, 'Matched_Longitude'] = row['GPS_LONGITUDE_TX']
                    match_found = True
                    match_count += 1
                    break  # Stop searching after the first match for this row
            if match_found:
                break

        if not match_found:
            no_match_count += 1

    print(f"Total matches found: {match_count}")
    print(f"Total no matches found: {no_match_count}")

    return df

# Load your Excel file
file_path = 'your_file.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Call the function to find matches
result_df = find_matches(df)

# Save the results to a new Excel file
result_df.to_excel('matched_results.xlsx', index=False)














import pandas as pd

def find_matches(df):
    # Create new columns for the output
    df['Matched_MacAddress'] = [[] for _ in range(len(df))]
    df['Matched_Latitude'] = [[] for _ in range(len(df))]
    df['Matched_Longitude'] = [[] for _ in range(len(df))]

    # Convert the columns to string type to handle non-string data
    df['COMM_ID_NB'] = df['COMM_ID_NB'].astype(str)
    df['configuration.MacAddress'] = df['configuration.MacAddress'].astype(str)

    # Iterate over each MacAddress and compare with every COMM_ID_NB
    for index, mac_row in df.iterrows():
        mac_address = mac_row['configuration.MacAddress'][3:]  # Exclude the first three characters

        for _, comm_row in df.iterrows():
            comm_id = comm_row['COMM_ID_NB']

            # Check for 4-character matches
            for i in range(len(comm_id) - 3):
                if comm_id[i:i+4] in mac_address:
                    # Update the new columns with matched data
                    df.at[index, 'Matched_MacAddress'].append(mac_row['configuration.MacAddress'])
                    df.at[index, 'Matched_Latitude'].append(comm_row['GPS_LATITUDE_TX'])
                    df.at[index, 'Matched_Longitude'].append(comm_row['GPS_LONGITUDE_TX'])
                    break  # Stop searching after the first match for this COMM_ID_NB

    return df

# Load your Excel file
file_path = 'your_file.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Call the function to find matches
result_df = find_matches(df)

# Save the results to a new Excel file
result_df.to_excel('matched_results.xlsx', index=False)


