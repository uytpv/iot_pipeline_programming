
CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  mac STRING NOT NULL,
  location STRING NOT NULL
);

.tables

PRAGMA table_info("device");
