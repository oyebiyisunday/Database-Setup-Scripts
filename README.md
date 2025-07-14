# Database Setup Scripts

This repository contains SQL scripts to create and populate two sample databases for learning, testing, and demonstration purposes.

## Databases Provided

### 1. PUBS Database
A comprehensive publishing industry database, commonly used as a sample schema for SQL learning.

**Entities:**
- **Authors:** Details of book authors
- **Publishers:** Publishing companies and their locations
- **Book Titles:** Book information and publishing details
- **Author-Title Relationships:** Links between authors and their authored titles
- **Book Stores:** Store locations and information

**Tables:**
- `authors`
- `publishers`
- `titleauthor`
- `titles`
- `stores`

### 2. Employee/Department Database
A simple organizational database to demonstrate employee and department structures.

**Entities:**
- **Employees:** Employee records, including salaries
- **Departments:** Department information

**Tables:**
- `emp` (employees)
- `dept` (departments)

---

## Script Files

Scripts are provided for both Microsoft SQL Server and Oracle Database systems.

### Microsoft SQL Server Scripts

- **PUBS Database:**  
  `create_PUBS_microsoft_new.txt`  
  - Creates and populates all PUBS database tables  
  - Uses SQL Server-specific syntax (`getdate()`, `GO` batch separators)

- **Employee/Department Database:**  
  `setup1_emp_dept_Microsoft.txt.txt`  
  - Creates and populates `emp` and `dept` tables  
  - Uses T-SQL syntax

### Oracle Database Scripts

- **PUBS Database:**  
  `createPUBS_Oracle_new.txt`  
  - Creates and populates all PUBS database tables  
  - Uses Oracle syntax (`SYSDATE`, `NUMBER` datatype, `;` statement terminators)

- **Employee/Department Database:**  
  `setup1_emp_dept_ORACLE.txt.txt`  
  - Creates and populates `emp` and `dept` tables  
  - Uses PL/SQL syntax with explicit `COMMIT` statements

---

## Usage Instructions

### For Microsoft SQL Server

1. To set up the PUBS database, run:  
   `create_PUBS_microsoft_new.txt`

2. To set up the Employee/Department database, run:  
   `setup1_emp_dept_Microsoft.txt.txt`

### For Oracle Database

1. To set up the PUBS database, run:  
   `createPUBS_Oracle_new.txt`

2. To set up the Employee/Department database, run:  
   `setup1_emp_dept_ORACLE.txt.txt`

---

## Notes

- The PUBS database contains realistic publishing industry data.
- The employee/department database is intentionally simple for demonstration and learning.
- All scripts include both table creation and sample data insertion.
- **Oracle scripts** use explicit `COMMIT` statements for transaction control.
- **Microsoft SQL Server scripts** use `GO` batch separators where needed.

---

## Ideal Uses

- Learning and practicing SQL queries
- Practicing database joins
- Testing application database connectivity
- Demonstrating database concepts

---
