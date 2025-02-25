import pandas as pd
import pymysql
import json
from sqlalchemy

# Load the enhanced dataset
df = pd.read_csv('data/enhanced_ipl_data.csv')

# Load database credentials from config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# MySQL connection
mysql_connection = pymysql.connect(
    host=config['mysql']['host'],
    user=config['mysql']['user'],
    password=config['mysql']['password'],
    database=config['mysql']['database']
)

try:
    cursor = mysql_connection.cursor()
    
    # Creating table if it does not exist (Example for MySQL)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS matches (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        team1 VARCHAR(100) NOT NULL,
        team2 VARCHAR(100) NOT NULL,
        toss_winner VARCHAR(100),
        decision VARCHAR(50),
        first_score INT,
        first_wickets INT,
        second_score INT,
        second_wickets INT,
        match_winner VARCHAR(100),
        player_of_the_match VARCHAR(100),
        team1_batting_average FLOAT,
        team2_batting_average FLOAT
    );
    """
    cursor.execute(create_table_query)
    mysql_connection.commit()

    # Inserting data into the MySQL table
    for index, row in df.iterrows():
        insert_query = """
        INSERT INTO matches (date, team1, team2, toss_winner, decision, first_score, 
                             first_wickets, second_score, second_wickets, match_winner, 
                             player_of_the_match, team1_batting_average, team2_batting_average)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            row['date'], row['team1'], row['team2'], row['toss_winner'], row['decision'],
            row['first_score'], row['first_wickets'], row['second_score'], row['second_wickets'],
            row['match_winner'], row['player_of_the_match'], row['team1_batting_average'], row['team2_batting_average']
        )
        cursor.execute(insert_query, values)
    
    mysql_connection.commit()
    print("Data successfully inserted into MySQL.")
except Exception as e:
    print(f"Error inserting into MySQL: {e}")
finally:
    mysql_connection.close()
