-- creates table
SELECT
	tv_shows.title
FROM
	tv_shows
WHERE
	id NOT IN (
SELECT
	tv_shows.id
FROM
	tv_shows
INNER JOIN 
	tv_show_genres
ON
	tv_show_genres.genre_id = tv_shows.id
INNER JOIN
	tv_genres
ON
	tv_genres.id = tv_show_genres.show_id
WHERE
	name = "Comedy"
)
ORDER BY
	title;
