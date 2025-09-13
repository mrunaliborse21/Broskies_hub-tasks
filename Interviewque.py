INTERVIEW QUESTIONS
1. What is normalization?

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller ones and defining relationships between them. Common forms are 1NF, 2NF, 3NF, BCNF.

2. Explain primary vs foreign key.

Primary Key → A unique identifier for each record in a table. It cannot have NULL values.

Foreign Key → A field in one table that references the Primary Key in another table, establishing a relationship between the two tables.

3. What are constraints?

Constraints are rules applied to table columns to ensure data integrity. Examples:

NOT NULL → Column must have a value.

UNIQUE → Prevents duplicate values.

PRIMARY KEY → Unique + Not Null.

FOREIGN KEY → Ensures referential integrity.

CHECK → Validates condition.

DEFAULT → Assigns a default value if no value is provided.

4. What is a surrogate key?

A surrogate key is an artificial or system-generated key (like an auto-increment integer) used to uniquely identify records, instead of using natural keys (like email or SSN).

5. How do you avoid data redundancy?

By applying normalization.

Using Primary and Foreign keys to relate tables.

Maintaining constraints and unique indexes.

Following a proper database schema design.
6. What is an ER diagram?

An Entity-Relationship (ER) diagram is a graphical representation of entities (tables), attributes (columns), and relationships between entities in a database. It is used in database design.


7. What are the types of relationships in DBMS?

1. One-to-One (1:1) → One entity relates to only one other.


2. One-to-Many (1:N) → One entity relates to multiple entities.


3. Many-to-Many (M:N) → Multiple entities relate to multiple entities.

8. Explain the purpose of AUTO_INCREMENT.

AUTO_INCREMENT in MySQL automatically generates a unique sequential value for a column (usually the primary key) whenever a new row is inserted.


9. What is the default storage engine in MySQL?

The default storage engine in MySQL is InnoDB.
(It supports transactions, row-level locking, and foreign keys).


10. What is a composite key?

A composite key is a combination of two or more columns used together to uniquely identify a record in a table. Example: (student_id, course_id) in an enrollment table.










