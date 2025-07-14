Database Setup Scripts
This repository contains SQL scripts to create and populate two sample databases:

PUBS Database - A publishing industry database

Employee/Department Database - A simple organizational structure database

Scripts are provided for both Microsoft SQL Server and Oracle Database systems.

Database Descriptions
1. PUBS Database
A comprehensive publishing database containing information about:

Authors and their details

Publishers and their locations

Book titles with publishing details

Author-title relationships

Book stores and their locations

Tables:

authors

publishers

titleauthor

titles

stores

2. Employee/Department Database
A simple organizational database showing:

Employees and their salaries

Department information

Tables:

emp (employees)

dept (departments)

Script Files
Microsoft SQL Server Scripts
PUBS Database
File: create_PUBS_microsoft_new.txt

Creates and populates all PUBS database tables

Uses SQL Server-specific syntax (getdate(), go commands)

Employee/Department Database
File: setup1_emp_dept_Microsoft.txt.txt

Creates and populates emp and dept tables

Uses T-SQL syntax

Oracle Database Scripts
PUBS Database
File: createPUBS_Oracle_new.txt

Creates and populates all PUBS database tables

Uses Oracle-specific syntax (SYSDATE, NUMBER datatype, semicolon terminators)

Employee/Department Database
File: setup1_emp_dept_ORACLE.txt.txt

Creates and populates emp and dept tables

Uses PL/SQL syntax with explicit commit statements

Usage Instructions
For Microsoft SQL Server
Execute create_PUBS_microsoft_new.txt to create PUBS database

Execute setup1_emp_dept_Microsoft.txt.txt to create employee/department database

For Oracle Database
Execute createPUBS_Oracle_new.txt to create PUBS database

Execute setup1_emp_dept_ORACLE.txt.txt to create employee/department database

Notes
The PUBS database contains realistic publishing industry data

The employee/department database is intentionally simple for demonstration purposes

Scripts include both table creation and sample data insertion

Oracle scripts use explicit commit statements for transaction control

Microsoft scripts use go batch separators where needed

These databases are ideal for:

Learning SQL queries

Practicing database joins

Testing application database connectivity

Demonstrating database concepts

