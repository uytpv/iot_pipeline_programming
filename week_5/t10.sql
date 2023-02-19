CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  mac STRING NOT NULL,
  location STRING NOT NULL
);

.tables

PRAGMA table_info("device");

INSERT INTO device (mac, location) VALUES ('aa-bb-cc-11-22-33','M19Cxx'), ('ab-cd-ef-12-34-56','S15xx');
SELECT * FROM device;
SELECT location from device;
DELETE FROM device WHERE id = 1;
CREATE TABLE measurement (
  dev_id INTEGER ,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  temperature NUMBER NOT NULL,
  humidity NUMBER NOT NULL,
  power_usage NUMBER NOT NULL,
  FOREIGN KEY(dev_id) REFERENCES device(id)
);
INSERT INTO measurement (dev_id, temperature, humidity, power_usage) VALUES (2,6, 20, 2.3), (2,8,21,1.5);


select dev_id, power_usage from measurement where temperature > 7
