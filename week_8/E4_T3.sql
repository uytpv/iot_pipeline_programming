SELECT artists.name, SUM(albums.tracks) AS 'Album count'
FROM artists
LEFT JOIN albums ON artists.name = albums.artist
GROUP BY artists.id
ORDER BY artists.name DESC;