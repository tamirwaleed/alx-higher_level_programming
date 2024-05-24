-- avg temp
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
HAVING month = 7 or month = 8
ORDER BY avg_temp DESC
LIMIT 3;
