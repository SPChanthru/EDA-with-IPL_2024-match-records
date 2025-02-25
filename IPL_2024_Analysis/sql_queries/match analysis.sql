-- Total Matches Played by Each Team
SELECT team1, COUNT(*) AS matches_played
FROM ipl_2024_matches
GROUP BY team1
ORDER BY matches_played DESC;

-- Top 5 Players with Most "Man of the Match" Awards
SELECT man_of_the_match, COUNT(*) AS awards
FROM ipl_2024_matches
WHERE man_of_the_match != 'Unknown'
GROUP BY man_of_the_match
ORDER BY awards DESC
LIMIT 5;

-- Most Successful Team (Highest Wins)
SELECT winner, COUNT(*) AS wins
FROM ipl_2024_matches
WHERE winner != 'No Result'
GROUP BY winner
ORDER BY wins DESC;
