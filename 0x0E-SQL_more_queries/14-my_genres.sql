-- creates table
SELECT
	tv_genres.name AS name
FROM
	tv_genres
WHERE
	tv_genres.id IN (
		SELECT genre_id
		FROM tv_show_genres
		WHERE show_id IN (
			SELECT id
			FROM tv_shows
			WHERE title = "DEXTER"
		))
ORDER BY
	name;
