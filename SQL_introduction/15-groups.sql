-- Lists the number of records with the same score in a table ordered by number of records
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;