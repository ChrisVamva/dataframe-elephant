# SQL Basics

## Overview
SQL (Structured Query Language) is a domain-specific language used for managing and manipulating relational databases. First developed at IBM in the 1970s, it is the standard language for relational database management systems (RDBMS) like PostgreSQL, MySQL, SQL Server, and Oracle.

## Key Characteristics
- **Paradigm**: Declarative (specify what, not how)
- **Typing**: Static (schema-defined)
- **Execution**: Interpreted by the database engine
- **Primary Use**: Data definition, manipulation, and querying
- **Standard**: ANSI SQL (with vendor-specific extensions)

## Syntax Fundamentals

### Basic Query Structure
```sql
-- SELECT statement
SELECT column1, column2
FROM table_name
WHERE condition
GROUP BY column1
HAVING condition
ORDER BY column1 ASC/DESC
LIMIT 10;
```

### Data Types
```sql
-- Numeric
INT, INTEGER, SMALLINT, BIGINT
DECIMAL(precision, scale), NUMERIC(precision, scale)
FLOAT, DOUBLE, REAL

-- Character
CHAR(n)          -- Fixed-length
VARCHAR(n)       -- Variable-length
TEXT             -- Unlimited length

-- Date and Time
DATE             -- YYYY-MM-DD
TIME             -- HH:MM:SS
DATETIME         -- Date + Time
TIMESTAMP        -- Date + Time with timezone

-- Boolean
BOOLEAN          -- TRUE or FALSE

-- Binary
BLOB, BINARY, VARBINARY
```

### Creating Tables
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    age INT CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### Inserting Data
```sql
-- Single row
INSERT INTO users (username, email, password_hash, age)
VALUES ('alice', 'alice@example.com', 'hashed_pw', 30);

-- Multiple rows
INSERT INTO users (username, email, password_hash, age)
VALUES
    ('bob', 'bob@example.com', 'hashed_pw', 25),
    ('charlie', 'charlie@example.com', 'hashed_pw', 35);

-- Insert from another table
INSERT INTO inactive_users
SELECT * FROM users WHERE is_active = FALSE;
```

### Querying Data
```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, username, email FROM users;

-- Aliasing
SELECT username AS name, email AS contact FROM users;

-- Distinct values
SELECT DISTINCT city FROM users;

-- Limiting results
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Pagination

-- Ordering
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users ORDER BY last_name, first_name;
```

### Filtering with WHERE
```sql
-- Comparison operators
SELECT * FROM users WHERE age > 18;
SELECT * FROM users WHERE age >= 18 AND age <= 65;
SELECT * FROM users WHERE age BETWEEN 18 AND 65;
SELECT * FROM users WHERE age IN (18, 21, 65);
SELECT * FROM users WHERE age NOT IN (18, 21, 65);

-- Pattern matching
SELECT * FROM users WHERE username LIKE 'a%';     -- Starts with 'a'
SELECT * FROM users WHERE username LIKE '%a';     -- Ends with 'a'
SELECT * FROM users WHERE username LIKE '%a%';    -- Contains 'a'
SELECT * FROM users WHERE username LIKE '_lice';  -- Single char wildcard

-- NULL checks
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- Logical operators
SELECT * FROM users WHERE age > 18 AND is_active = TRUE;
SELECT * FROM users WHERE age < 18 OR age > 65;
SELECT * FROM users WHERE NOT is_active;
```

### Joins
```sql
-- INNER JOIN (matching rows only)
SELECT u.username, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN (all from left, matching from right)
SELECT u.username, o.total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN (all from right, matching from left)
SELECT u.username, o.total_amount
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN (all from both)
SELECT u.username, o.total_amount
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- CROSS JOIN (cartesian product)
SELECT u.username, p.product_name
FROM users u
CROSS JOIN products p;

-- Self join
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

### Aggregation
```sql
-- Aggregate functions
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT city) FROM users;
SELECT AVG(age) FROM users;
SELECT MIN(age), MAX(age) FROM users;
SELECT SUM(total_amount) FROM orders;

-- GROUP BY
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city;

-- HAVING (filter groups)
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
HAVING COUNT(*) > 10;

-- Multiple grouping
SELECT city, is_active, COUNT(*) AS count
FROM users
GROUP BY city, is_active;
```

### Subqueries
```sql
-- Subquery in WHERE
SELECT * FROM users
WHERE age > (SELECT AVG(age) FROM users);

-- Subquery in FROM
SELECT city, avg_age
FROM (
    SELECT city, AVG(age) AS avg_age
    FROM users
    GROUP BY city
) AS city_ages
WHERE avg_age > 30;

-- Subquery in SELECT
SELECT
    username,
    (SELECT COUNT(*) FROM orders WHERE orders.user_id = users.id) AS order_count
FROM users;

-- EXISTS
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);

-- IN with subquery
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total_amount > 100);
```

### Updating and Deleting
```sql
-- Update
UPDATE users
SET is_active = FALSE
WHERE last_login < '2023-01-01';

-- Update multiple columns
UPDATE users
SET email = 'newemail@example.com', age = 31
WHERE id = 1;

-- Update with subquery
UPDATE orders
SET status = 'archived'
WHERE user_id IN (SELECT id FROM users WHERE is_active = FALSE);

-- Delete
DELETE FROM users WHERE id = 1;

-- Delete with subquery
DELETE FROM orders
WHERE user_id IN (SELECT id FROM users WHERE is_active = FALSE);

-- Truncate (remove all rows, faster)
TRUNCATE TABLE orders;
```

### Modifying Schema
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Drop column
ALTER TABLE users DROP COLUMN phone;

-- Modify column
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;

-- Add constraint
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- Drop constraint
ALTER TABLE users DROP CONSTRAINT unique_email;

-- Rename table
ALTER TABLE users RENAME TO customers;

-- Drop table
DROP TABLE IF EXISTS orders;
```

### Indexes
```sql
-- Create index
CREATE INDEX idx_users_email ON users(email);

-- Unique index
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- Composite index
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Drop index
DROP INDEX idx_users_email;

-- Analyze query performance
EXPLAIN SELECT * FROM users WHERE email = 'alice@example.com';
```

### Transactions
```sql
-- Begin transaction
BEGIN;

-- Multiple operations
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit (save changes)
COMMIT;

-- Rollback (undo changes)
ROLLBACK;

-- Savepoint
SAVEPOINT before_update;
UPDATE users SET age = 30;
ROLLBACK TO SAVEPOINT before_update;
```

### Common Table Expressions (CTEs)
```sql
-- Simple CTE
WITH active_users AS (
    SELECT * FROM users WHERE is_active = TRUE
)
SELECT * FROM active_users WHERE age > 18;

-- Multiple CTEs
WITH
    user_orders AS (
        SELECT user_id, COUNT(*) AS order_count
        FROM orders
        GROUP BY user_id
    ),
    high_value_users AS (
        SELECT user_id FROM orders
        GROUP BY user_id
        HAVING SUM(total_amount) > 1000
    )
SELECT u.username, uo.order_count
FROM users u
JOIN user_orders uo ON u.id = uo.user_id
JOIN high_value_users hvu ON u.id = hvu.user_id;

-- Recursive CTE
WITH RECURSIVE category_tree AS (
    -- Base case
    SELECT id, name, parent_id, 1 AS depth
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT c.id, c.name, c.parent_id, ct.depth + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY depth;
```

### Window Functions
```sql
-- ROW_NUMBER
SELECT
    username,
    age,
    ROW_NUMBER() OVER (ORDER BY age DESC) AS rank
FROM users;

-- RANK and DENSE_RANK
SELECT
    username,
    score,
    RANK() OVER (ORDER BY score DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank
FROM results;

-- Running total
SELECT
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM sales;

-- Moving average
SELECT
    order_date,
    amount,
    AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales;

-- Partition by
SELECT
    department,
    employee_name,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

## Common Database-Specific Features
- **PostgreSQL**: JSONB, arrays, full-text search, CTEs, window functions
- **MySQL**: AUTO_INCREMENT, ENUM, full-text search
- **SQL Server**: TOP, OFFSET/FETCH, T-SQL extensions
- **Oracle**: CONNECT BY, PL/SQL, analytic functions

## Strengths
- Universal language for relational databases
- Declarative (focus on what, not how)
- Powerful querying capabilities
- ACID compliance for data integrity
- Mature and standardized

## Weaknesses
- Not suitable for non-relational data
- Vendor-specific extensions reduce portability
- Complex queries can be hard to optimize
- Not a general-purpose programming language
- Schema changes can be difficult in production
