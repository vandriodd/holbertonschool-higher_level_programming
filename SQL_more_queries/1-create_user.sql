-- Creates the MySQL server user user_0d_1 (if not exists)
-- IDENTIFIED BY 'password' sets a passcode for the user
-- 'GRANT...' line grants all privileges of the database to user_0d_1
-- 'FLUSH PRIVILEGES' flush privileges and reload the permission tables of the server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;