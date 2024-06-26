-- creates table
SELECT
	tv_genres.name
FROM
	tv_genres
WHERE
	id NOT IN (
SELECT
	tv_genres.id
FROM
	tv_genres
INNER JOIN 
	tv_show_genres
ON
	tv_show_genres.genre_id = tv_genres.id
INNER JOIN
	tv_shows
ON
	tv_shows.id = tv_show_genres.show_id
WHERE
	title = "Dexter"
)
ORDER BY
	name;
