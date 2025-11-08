CREATE TABLE user_info (
    user_id INTEGER NOT NULL,
    name Text NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    postcode TEXT NOT NULL,
    town TEXT,
    street TEXT,
    can_drive INTEGER DEFAULT 0,
    likes_hot INTEGER DEFAULT 0,
    likes_cold INTEGER DEFAULT 0,
    FOREIGN KEY (user_id)
       REFERENCES users (user_id)
);