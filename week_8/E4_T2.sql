
SELECT artists.name, artists.followers, albums.name, albums.tracks
FROM artists
INNER JOIN albums
ON artists.name = albums.artist
ORDER BY artists.name ASC, albums.name ASC;