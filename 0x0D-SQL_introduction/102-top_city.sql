-- avg temp
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
HAVING month = "July" or month = "August"
ORDER BY avg_temp DESC
LIMIT 3;
