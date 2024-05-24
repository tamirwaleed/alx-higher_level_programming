-- avg temp
SELECT city, AVG(value) as avg_temp
FROM temperatures
ORDER BY avg_temp DESC;
