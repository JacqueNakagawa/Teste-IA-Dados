CREATE TABLE carros (
	id BIGINT,
	modelo TEXT,
	ano INTEGER,
	novo boolean
)

COPY carros
FROM 'C:\Users\Jacqueline Nakagawa\Desktop\Banco relacional\carros.csv'
DELIMITER ','
CSV HEADER;

SELECT *
FROM carros;