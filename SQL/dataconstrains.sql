CREATE TABLE Students (
    ID int NOT NULL,
    Name varchar(255) NOT NULL,
    Age int,
    CHECK (Age>=18) /*The CHECK constraint ensures that all values in a column satisfies certain conditions.*/
);