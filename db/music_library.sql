DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist VARCHAR(255)
)