import pandas as pd

# Load the dataset
df = pd.read_csv("data/ipl_2024.csv")

# Check initial info and missing values
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values in 'winner' and 'player_of_the_match' columns
df['winner'] = df['winner'].fillna('No Result')
df['player_of_the_match'] = df['player_of_the_match'].fillna('Unknown')

# Convert the 'date' column to datetime, handle invalid date entries
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove rows where the date is invalid (if needed)
df = df[df['date'].notna()]

# Alternatively, replace invalid dates with a placeholder (e.g., '1900-01-01')
# df['date'] = pd.to_datetime(df['date'], errors='coerce').fillna('1900-01-01')

# Handle missing values in other columns (optional):
df['decision'] = df['decision'].fillna('Unknown')  # Fill missing values in 'decision'

# Optionally, handle other columns if needed (like 'most_runs' and 'most_wkts')
df['most_runs'] = df['most_runs'].fillna('Unknown')
df['most_wkts'] = df['most_wkts'].fillna('Unknown')

# Display cleaned data
print("\nCleaned Data:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv("data/ipl_2024_cleaned.csv", index=False)

print("\nData cleaning completed. Cleaned data saved as 'ipl_2024_cleaned.csv'.")
