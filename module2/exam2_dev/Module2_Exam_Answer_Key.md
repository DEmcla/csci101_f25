# CSCI 101: Module 2 Exam - ANSWER KEY
## Database Design, ERD, Normalization, and Relationships

**Total Points:** 100 points

---

## PART A: TRUE/FALSE (22.5 points total)

1. **TRUE** - Rectangles = entities, ovals = attributes (standard ERD notation)

2. **TRUE** - Composite keys are made of 2+ columns (e.g., {StudentID, CourseID})

3. **TRUE** - Crow's foot (≺) indicates the "many" side

4. **FALSE** - 1NF eliminates non-atomic values and repeating groups. 3NF eliminates transitive dependencies.

5. **TRUE** - This is the definition of functional dependency

6. **FALSE** - Bridge tables resolve **many-to-many** relationships, not one-to-one

7. **TRUE** - This is the definition of partial dependency (violates 2NF)

8. **TRUE** - Denormalization adds redundancy intentionally, often for performance

9. **TRUE** - This is the definition of 2NF

10. **TRUE** - This is the definition and purpose of foreign keys

11. **FALSE** - Many-to-many requires a bridge entity/table in between

12. **TRUE** - 3NF is the industry standard for most applications

13. **TRUE** - This is the definition of cardinality

14. **FALSE** - 3NF is more common; BCNF/4NF/5NF are used less frequently

15. **TRUE** - These are the three anomalies normalization prevents

---

## PART B: MULTIPLE CHOICE (45 points total)

16. **b) PhoneNumber: "555-1234, 555-5678"**
    - Multiple values in one cell violates atomicity (1NF)

17. **b) Single line on one end, crow's foot on the other**
    - One side = single, many side = crow's foot

18. **c) Composite primary key**
    - Made of two columns working together

19. **b) Second Normal Form (2NF)**
    - 2NF specifically eliminates partial dependencies

20. **b) When A → B and B → C, so A → C indirectly**
    - This is the definition of transitive dependency

21. **b) An entity that resolves a many-to-many relationship**
    - Bridge/associative entities break M:N into two 1:M relationships

22. **c) 3NF**
    - Transitive dependency exists: CourseID → InstructorID → InstructorName/Office
    - Table is in 2NF (no partial dependencies with single-column PK) but violates 3NF

23. **b) To reduce data redundancy and prevent anomalies**
    - This is the primary purpose of normalization

24. **b) Determinant**
    - The left side of X → Y is the determinant

25. **a) A frequently-run report that requires joining 8 tables and is too slow**
    - Performance issues are the main reason to denormalize

26. **b) Partial dependency**
    - StudentName depends on only part of the composite key {StudentID, CourseID}

27. **b) Mandatory participation (at least one required)**
    - Perpendicular line = mandatory, circle = optional

28. **d) BCNF**
    - BCNF requires all determinants to be candidate keys

29. **d) Many-to-many**
    - Many students can take many courses (M:N relationship)

30. **b) Create a separate PRODUCT table with ProductID and ProductName**
    - This removes the partial dependency (ProductID → ProductName)

31. **c) The number of entity instances that can participate in a relationship**
    - Cardinality defines relationship quantities (1:1, 1:M, M:N)

32. **b) It balances data integrity with reasonable complexity**
    - 3NF provides good integrity without excessive complexity

33. **d) Simple attribute**
    - DateOfBirth is a single, atomic value (not composite, multivalued, or derived)

---

## PART C: SHORT ANSWER (32.5 points total)

---

**Question 34 (4 points):** Explain the difference between a **primary key** and a **foreign key**. Provide an example of each.

**Answer:**
- **Primary Key (PK):** (2 points)
  - A column (or set of columns) that uniquely identifies each row in a table
  - Cannot contain NULL values
  - Example: StudentID in STUDENT table

- **Foreign Key (FK):** (2 points)
  - A column in one table that references the primary key of another table
  - Creates a relationship/link between tables
  - Example: StudentID in ENROLLMENT table (references STUDENT.StudentID)

**Grading:**
- 1 point for correct PK definition
- 1 point for PK example
- 1 point for correct FK definition
- 1 point for FK example

---

**Question 35 (5 points):** Consider this unnormalized table:

**LIBRARY_CHECKOUT**
| CardNumber | PatronName | BookISBN | BookTitle | BookAuthors | CheckoutDate |
|------------|------------|----------|-----------|-------------|--------------|
| C001 | Alice Brown | 978-01 | Database Design | Smith, Jones | 2024-01-15 |

Identify **TWO specific violations of First Normal Form (1NF)** in this table and explain why each is a problem.

**Answer:**

**Violation #1: BookAuthors contains multiple values** (2.5 points)
- The BookAuthors field contains "Smith, Jones" - two authors in one cell
- This violates atomicity - each cell should contain only one value
- Problem: Cannot easily query/sort by individual authors, difficult to maintain

**Violation #2: Possible repeating groups if multiple books checked out** (2.5 points)
- If a patron checks out multiple books, you'd need multiple rows with repeated patron info
- OR you might be tempted to put multiple books in one row (repeating groups)
- Problem: Creates redundancy and update anomalies

**Alternative acceptable answer:**
- If the table allows multiple books per row (like BookISBN1, BookISBN2, etc.) that would be repeating groups

**Grading:**
- 1.25 points per violation identified
- 1.25 points per explanation of why it's a problem
- Must identify TWO distinct violations

---

**Question 36 (5 points):** Draw the crow's feet notation symbols for the following:

**Answer:**

a) **One and only one** (mandatory one): **|—** (1.5 points)
   - Perpendicular line (mandatory) + single line (one)

b) **Zero or many** (optional many): **o≺** (1.5 points)
   - Circle (optional) + crow's foot (many)

c) **One or many** (mandatory many): **|≺** (2 points)
   - Perpendicular line (mandatory) + crow's foot (many)

**Grading:**
- Award full points if symbols are correct
- Deduct 0.5 points if close but minor errors
- Must show both the mandatory/optional indicator AND the one/many indicator

---

**Question 37 (6 points):** Given this table in 1NF:

**EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)**

a) What normal form violation exists in this table?

**Answer:** Transitive dependency / Violates 3NF (2 points)

b) Explain why this is a problem (what anomaly could occur?).

**Answer:** (2 points - must mention at least one specific anomaly)
- **Update anomaly:** If a department changes location, must update multiple employee records
- **Deletion anomaly:** If the last employee in a department is deleted, we lose department information
- **Insertion anomaly:** Cannot add a new department without hiring an employee
(Student needs only one, but any of these answers is acceptable)

c) Decompose this table to fix the problem.

**Answer:** (2 points)

**EMPLOYEE Table:**
- EmpID (PK)
- EmpName
- DeptID (FK)

**DEPARTMENT Table:**
- DeptID (PK)
- DeptName
- DeptLocation

**Grading:**
- 1 point for correct EMPLOYEE table structure
- 1 point for correct DEPARTMENT table structure
- Must show primary keys (PK) indicated

---

**Question 38 (5 points):** A university database needs to track students and courses.

Draw a simple ERD showing these three entities (STUDENT, COURSE, and the appropriate bridge entity) with their relationships using crow's feet notation.

**Answer:**

```
STUDENT ——|—————o≺—— ENROLLMENT ——≺o—————|—— COURSE
  (PK: StudentID)    (PK: {StudentID,     (PK: CourseID)
                          CourseID}
                      Attributes: Grade,
                                  Semester)
```

**Alternative text description:**
- STUDENT entity (1 point)
- COURSE entity (1 point)
- ENROLLMENT bridge entity in the middle (1 point)
- Correct crow's feet notation showing:
  - One STUDENT to many ENROLLMENTS (0.5 points)
  - One COURSE to many ENROLLMENTS (0.5 points)
- Attributes mentioned (Grade, Semester) (1 point)

**Grading:**
- 1 point for STUDENT entity box/label
- 1 point for COURSE entity box/label
- 1 point for ENROLLMENT bridge entity
- 1 point for correct relationship lines with crow's feet notation
- 1 point for indicating Grade and Semester are stored in ENROLLMENT

**Accept reasonable variations in notation as long as the relationships are correct**

---

**Question 39 (3.5 points):** List the three types of database anomalies that normalization helps prevent and provide a one-sentence description of each.

**Answer:**

1. **Update Anomaly** (1.17 points)
   - When you have to update the same information in multiple places, creating inconsistency risk
   - OR: Changing one fact requires updating multiple rows

2. **Insertion Anomaly** (1.17 points)
   - When you cannot add data without also adding other unrelated data
   - OR: Cannot add a new record because required information is missing

3. **Deletion Anomaly** (1.16 points)
   - When deleting one piece of information unintentionally loses other important information
   - OR: Removing a record causes loss of other unrelated data

**Grading:**
- ~1.17 points per anomaly
- Must name the anomaly (0.5 points each)
- Must provide reasonable description (0.67 points each)

---

**Question 40 (4 points):** When might a database designer choose to **denormalize** a properly normalized database? Give TWO specific scenarios where denormalization would be appropriate.

**Answer:** (2 points each scenario)

Acceptable scenarios include:

1. **Read-heavy reporting/analytics:**
   - Frequently-run reports that join many tables and perform slowly
   - Data warehouse or business intelligence applications
   - Dashboard queries that need fast response times

2. **Performance-critical queries:**
   - High-traffic queries that are causing bottlenecks
   - Real-time systems where query speed is critical
   - Calculated fields that are expensive to compute repeatedly

3. **Historical/archived data:**
   - Snapshot tables that preserve data as it was at a point in time
   - Audit trails or versioning systems

4. **Materialized views:**
   - Pre-computed aggregations or summaries
   - Caching complex join results

**Grading:**
- 2 points per valid scenario
- Must be specific and explain WHY denormalization helps
- Generic answers like "for performance" without specifics = 1 point
- Must identify TWO distinct scenarios

---

## GRADING RUBRIC SUMMARY

| Section | Points | Notes |
|---------|--------|-------|
| **Part A** | 22.5 | 1.5 points × 15 questions |
| **Part B** | 45 | 2.5 points × 18 questions |
| **Part C** | 32.5 | Variable points, see individual answers |
| **TOTAL** | **100** | |

---

## COMMON GRADING NOTES

**Partial Credit Guidelines:**
- Part A (T/F): No partial credit
- Part B (Multiple Choice): No partial credit
- Part C (Short Answer):
  - Award partial credit for partially correct answers
  - Deduct points for incorrect or missing information
  - Give credit for correct reasoning even if minor details are wrong
  - For decomposition problems, award partial credit if structure is mostly correct

**Common Student Mistakes to Watch For:**
1. Confusing partial dependencies (2NF) with transitive dependencies (3NF)
2. Drawing ERD relationship lines without proper crow's feet notation
3. Forgetting to indicate primary keys in decomposed tables
4. Mixing up determinant and dependent in functional dependencies
5. Not understanding that bridge tables are for M:N relationships
