-- creates table
SELECT
	tv_genres.name,
	SUM(tv_show_ratings.rate) as rating
FROM
	tv_show_ratings
INNER JOIN 
	tv_show_genres
ON
	tv_show_genres.show_id = tv_show_ratings.show_id
INNER JOIN
	tv_genres
ON
	tv_genres.id = tv_show_genres.genre_id
GROUP BY
	tv_genres.name
ORDER BY
	rating DESC;
