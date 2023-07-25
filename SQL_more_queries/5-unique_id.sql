-- Creates the table unique_id on server with the id set to the default value 1
-- id value must be unique
CREATE TABLE IF NOT EXISTS unique_id (
  id INT UNIQUE DEFAULT 1,
  name VARCHAR(256)
);
