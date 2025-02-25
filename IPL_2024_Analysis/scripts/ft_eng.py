import pandas as pd

# Load the enhanced dataset
df = pd.read_csv('data/ipl_2024_cleaned.csv')

# Ensure that the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

# Fill missing values for 'player_of_the_match' and 'decision'
df['player_of_the_match'].fillna('Unknown', inplace=True)
df['decision'].fillna('Unknown', inplace=True)

# Calculate team1 and team2 batting averages
# Avoid division by zero if wickets are zero
df['team1_batting_average'] = df['first_score'] / df['first_wkts'].replace(0, float('nan'))
df['team2_batting_average'] = df['second_score'] / df['second_wkts'].replace(0, float('nan'))

# Save the enhanced dataset
df.to_csv('data/enhanced_ipl_data.csv', index=False)

print("Feature engineering completed successfully!")
