
CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  mac STRING NOT NULL,
  location STRING NOT NULL
);

.tables

PRAGMA table_info("device");

INSERT INTO device (mac, location) VALUES ('aa-bb-cc-11-22-33','M19Cxx'), ('ab-cd-ef-12-34-56','S15xx');

