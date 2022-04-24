DROP TABLE IF EXISTS commands;

CREATE TABLE commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT UNIQUE NOT NULL,
    description TEXT,
    example TEXT,
    cli TEXT NOT NULL
);

