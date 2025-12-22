# sql_knowledge.py

SQL_INTRO = """
SQL (Structured Query Language) is used to work with data in relational databases.
A database contains tables. A table has rows (records) and columns (fields).
"""

SQL_BASIC_COMMANDS = """
SELECT: Read data from a table.
Example:
  SELECT name, salary
  FROM employees
  WHERE department = 'IT';

INSERT: Add new rows.
Example:
  INSERT INTO employees (id, name, department, salary)
  VALUES (1, 'Alice', 'IT', 60000);

UPDATE: Change existing rows.
Example:
  UPDATE employees
  SET salary = 65000
  WHERE name = 'Alice';

DELETE: Remove rows.
Example:
  DELETE FROM employees
  WHERE department = 'HR';
"""

SQL_FAQ = """
Q: What is SQL?
A: SQL is a language used to work with data in relational databases.

Q: What does SELECT do?
A: SELECT reads data from one or more tables.

Q: What does INSERT do?
A: INSERT adds new rows into a table.

Q: What does UPDATE do?
A: UPDATE changes existing rows in a table.

Q: What does DELETE do?
A: DELETE removes rows from a table.
"""
