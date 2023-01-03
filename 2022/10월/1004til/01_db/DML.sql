CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
    );

SELECT first_name, age
FROM users;

SELECT * FROM users;

SELECT rowid,first_name FROM users;

SELECT first_name, age FROM users
ORDER BY age ASC;

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

SELECT country FROM users;

SELECT DISTINCT country FROM users;

SELECT DISTINCT country FROM users
ORDER BY country;

SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

SELECT first_name, age, balance FROM users
WHERE age >= 30;

SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance >500000;





