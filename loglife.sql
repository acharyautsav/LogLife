create database clockmakers;
use clockmakers;
CREATE TABLE journal_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    productivity INT,
    mood INT,
    went_well TEXT,
    went_wrong TEXT,
    thoughts TEXT,
    todo_lists TEXT
);
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,            -- Auto-incrementing primary key
    email VARCHAR(255) NOT NULL UNIQUE,            -- Email must be unique and not null
    password_hash VARCHAR(255) NOT NULL,           -- Store the hashed password
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Automatically sets the creation time
);
select * from users;
drop table users;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- User ID, primary key, auto-incremented
    email VARCHAR(255) UNIQUE NOT NULL,  -- User's email, unique and cannot be null
    password_hash VARCHAR(255) NOT NULL,  -- User's hashed password, cannot be null
    first_name VARCHAR(100) NOT NULL,  -- User's first name
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Time of account creation (auto-filled)
);
select * from users;