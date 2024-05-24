-- 2nd table
DROP TABLE if exists second_table;

CREATE TABLE second_table(
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table(
	VALUES(1, "John", 10),
	VALUES(2, "ALex", 3),
	VALUES(3, "Bob", 14),
	VALUES(4, "Geoge", 8)
);
