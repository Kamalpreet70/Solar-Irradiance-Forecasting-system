import pandas as pd

# Load the hourly data from the CSV file into a pandas DataFrame
df = pd.read_csv("C:\\Users\\1212k\\OneDrive\\Desktop\\Sem 6\\Minor Project\\Data\\PreProcess_NITJ_Data.csv")

# Combine 'YEAR', 'MO', 'DY', and 'HR' columns into a single string format
df['DateTime'] = df['YEAR'].astype(str) + '-' + df['MO'].astype(str).str.zfill(2) + '-' + df['DY'].astype(str).str.zfill(2) + ' ' + df['HR'].astype(str).str.zfill(2) + ':00:00'

# Convert the combined column to datetime format
df['Date'] = pd.to_datetime(df['DateTime'])

# Define a function to determine the season based on the date
def get_season(date):
    month = date.month
    if month in [11, 12, 1, 2, 3]:
        return 'Cold Season'
    elif month in [4, 5, 6]:
        return 'Summer Season'
    elif month in [7, 8, 9]:
        return 'South-West Monsoon Season'
    elif month in [10]:
        return 'Post-Monsoon/Transition Period'
    else:
        return 'Unknown'

# Apply the function to create a new 'Season' column
df['Season'] = df['Date'].apply(get_season)

# Split the DataFrame into separate DataFrames for each season
cold_season_df = df[df['Season'] == 'Cold Season']
summer_season_df = df[df['Season'] == 'Summer Season']
monsoon_season_df = df[df['Season'] == 'South-West Monsoon Season']
post_monsoon_df = df[df['Season'] == 'Post-Monsoon/Transition Period']

# Save each season's data to a separate CSV file
cold_season_df.to_csv("C:\\Users\\1212k\\OneDrive\\Desktop\\Sem 6\\Minor Project\\Data\\cold_season_data.csv", index=False)
summer_season_df.to_csv("C:\\Users\\1212k\\OneDrive\\Desktop\\Sem 6\\Minor Project\\Data\\summer_season_data.csv", index=False)
monsoon_season_df.to_csv("C:\\Users\\1212k\\OneDrive\\Desktop\\Sem 6\\Minor Project\\Data\\monsoon_season_data.csv", index=False)
post_monsoon_df.to_csv("C:\\Users\\1212k\\OneDrive\\Desktop\\Sem 6\\Minor Project\\Data\\post_monsoon_data.csv", index=False)

print("Data has been split into four seasons and saved into separate CSV files.")
