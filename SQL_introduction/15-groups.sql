-- Lists the n records that have the same score in the table
-- the n record will be labeled with the name number
-- sorted in desc
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;