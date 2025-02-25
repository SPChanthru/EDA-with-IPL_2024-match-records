CREATE TABLE matches (
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