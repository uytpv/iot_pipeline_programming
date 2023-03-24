CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    followers INTEGER NOT NULL
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    tracks INTEGER NOT NULL,
    FOREIGN KEY (artist) REFERENCES artists(id)
);