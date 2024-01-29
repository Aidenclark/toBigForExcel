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
