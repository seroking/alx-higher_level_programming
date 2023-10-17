-- group

SELECT score, COUNT(*) as count
FROM second_table
GROUP BY score
HAVING count > 1
ORDER BY count DESC;
