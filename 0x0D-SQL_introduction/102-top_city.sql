-- avg temp
SELECT city, AVG(value) as avg_temp
FROM (
	SELECT *
	FROM temperatures
	WHERE month = "July" or month = "August"
)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
