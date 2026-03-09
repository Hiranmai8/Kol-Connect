CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
);

CREATE TABLE kol_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    full_name TEXT,
    country TEXT,
    niche TEXT,
    platform TEXT
);

CREATE TABLE company_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    company_name TEXT,
    website TEXT,
    industry TEXT,
    country TEXT
);

CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    title TEXT,
    description TEXT,
    budget INTEGER,
    deadline TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER,
    receiver_id INTEGER,
    message TEXT
);

CREATE TABLE wallet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    balance INTEGER
);