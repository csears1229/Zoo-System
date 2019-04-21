CREATE DATABASE zoo;
USE zoo;
CREATE TABLE IF NOT EXISTS name (
  name_id INT AUTO_INCREMENT,
  first_name VARCHAR(16) NOT NULL,
  last_name VARCHAR(16) NOT NULL,
  PRIMARY KEY (name_id));
CREATE TABLE IF NOT EXISTS users (
  username VARCHAR(16) NOT NULL,
  password VARCHAR(100) NOT NULL,
  role VARCHAR(5) NOT NULL,
  lockout_status VARCHAR(1) NOT NULL,
  namekey INT NOT NULL,
  FOREIGN KEY (namekey) REFERENCES name(name_id)
  ON DELETE CASCADE);

