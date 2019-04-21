USE zoo;
INSERT INTO name (first_name, last_name) VALUES ("James", "Peterson");
INSERT INTO name (first_name, last_name) VALUES ("Mike", "Rodgers");
INSERT INTO name (first_name, last_name) VALUES ("Justin", "Clark");
INSERT INTO name (first_name, last_name) VALUES ("Barry", "Farese");
INSERT INTO name (first_name, last_name) VALUES ("Aaron", "Lorio");
INSERT INTO name (first_name, last_name) VALUES ("Justin", "Smith");
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("jpeterson", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "Admin", "F", 1);
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("mrodgers", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "Admin", "F", 2);
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("jclark", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "Admin", "F", 2);
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("bfarese", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "User", "F", 4);
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("alorio", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "User", "T", 5);
INSERT INTO users (username, password, role, lockout_status, namekey) VALUES ("jsmith", "$pbkdf2-sha256$10$n7NWqnUOAQDg/A$pgGL8wVyuhjx0bb.eBh72cQRAuBoHkPd3DoqjeXXgRI", "User", "T", 6);

desc name;
desc users;
SELECT * FROM name;
SELECT * FROM users;
SELECT first_name, last_name, username, password, role, lockout_status FROM name INNER JOIN users ON users.namekey = name.name_id;


