-- Creates the table id_not_null on the server with the id set to the default value 1
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
