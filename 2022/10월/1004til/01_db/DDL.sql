CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME to new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name to last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

