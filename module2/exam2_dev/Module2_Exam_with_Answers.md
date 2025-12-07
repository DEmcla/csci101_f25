# CSCI 101: Module 2 Exam - WITH ANSWERS
## Database Design, ERD, Normalization, and Relationships

**Time Limit:** 75 minutes
**Total Points:** 100 points
**Exam Type:** Open book, open notes, NO AI tools permitted

---

## Instructions

- This exam consists of **40 questions** divided into three sections:
  - **Part A: True/False** (15 questions, 1.5 points each = 22.5 points)
  - **Part B: Multiple Choice** (18 questions, 2.5 points each = 45 points)
  - **Part C: Short Answer** (7 questions, varies = 32.5 points)
- Time management suggestion:
  - Part A: 12 minutes
  - Part B: 30 minutes
  - Part C: 30 minutes
  - Review: 3 minutes

---

## PART A: TRUE/FALSE (22.5 points total)

**Instructions:** Each question is worth 1.5 points.

---

**1.** In an Entity Relationship Diagram (ERD), a rectangle represents an entity and an oval represents an attribute.

**ANSWER: TRUE**
- Rectangles = entities, ovals = attributes (standard ERD notation)

---

**2.** A primary key can be composed of multiple columns working together (a composite key).

**ANSWER: TRUE**
- Composite keys are made of 2+ columns (e.g., {StudentID, CourseID})

---

**3.** In crow's feet notation, a "crow's foot" symbol indicates the "many" side of a relationship.

**ANSWER: TRUE**
- Crow's foot (≺) indicates the "many" side

---

**4.** First Normal Form (1NF) requires eliminating transitive dependencies.

**ANSWER: FALSE**
- 1NF eliminates non-atomic values and repeating groups
- 3NF eliminates transitive dependencies

---

**5.** A functional dependency X → Y means "if you know X, you can determine Y."

**ANSWER: TRUE**
- This is the definition of functional dependency

---

**6.** Bridge tables (junction tables) are used to resolve one-to-one relationships.

**ANSWER: FALSE**
- Bridge tables resolve **many-to-many** relationships, not one-to-one

---

**7.** A partial dependency occurs when a non-key attribute depends on only part of a composite primary key.

**ANSWER: TRUE**
- This is the definition of partial dependency (violates 2NF)

---

**8.** Denormalization means intentionally adding redundancy back into a database, often for performance reasons.

**ANSWER: TRUE**
- Denormalization adds redundancy intentionally, often for performance

---

**9.** Second Normal Form (2NF) requires that the table must first be in 1NF and have no partial dependencies.

**ANSWER: TRUE**
- This is the definition of 2NF

---

**10.** A foreign key in one table references the primary key of another table, creating a relationship between them.

**ANSWER: TRUE**
- This is the definition and purpose of foreign keys

---

**11.** In a many-to-many relationship, you can directly connect two tables without a bridge entity.

**ANSWER: FALSE**
- Many-to-many requires a bridge entity/table in between

---

**12.** Third Normal Form (3NF) is considered the industry standard for most database applications.

**ANSWER: TRUE**
- 3NF is the industry standard for most applications

---

**13.** Cardinality refers to the number of instances of one entity that can be associated with instances of another entity.

**ANSWER: TRUE**
- This is the definition of cardinality

---

**14.** BCNF, 4NF, and 5NF are more commonly used in practice than 3NF.

**ANSWER: FALSE**
- 3NF is more common; BCNF/4NF/5NF are used less frequently

---

**15.** Update anomalies, insertion anomalies, and deletion anomalies are problems that normalization helps prevent.

**ANSWER: TRUE**
- These are the three anomalies normalization prevents

---

## PART B: MULTIPLE CHOICE (45 points total)

**Instructions:** Each question is worth 2.5 points.

---

**16.** Which of the following is an example of a **non-atomic value** that violates 1NF?
- a) StudentID: 12345
- b) PhoneNumber: "555-1234, 555-5678"
- c) LastName: "Smith"
- d) GPA: 3.75

**ANSWER: b) PhoneNumber: "555-1234, 555-5678"**
- Multiple values in one cell violates atomicity (1NF)

---

**17.** In crow's feet notation, which symbol combination represents a **one-to-many** relationship?
- a) Single line on both ends
- b) Single line on one end, crow's foot on the other
- c) Crow's foot on both ends
- d) Double line on both ends

**ANSWER: b) Single line on one end, crow's foot on the other**
- One side = single, many side = crow's foot

---

**18.** Given the functional dependency `{OrderID, ProductID} → Quantity`, what type of key is `{OrderID, ProductID}`?
- a) Foreign key
- b) Simple primary key
- c) Composite primary key
- d) Candidate key

**ANSWER: c) Composite primary key**
- Made of two columns working together

---

**19.** Which normal form specifically addresses the elimination of **partial dependencies**?
- a) First Normal Form (1NF)
- b) Second Normal Form (2NF)
- c) Third Normal Form (3NF)
- d) Boyce-Codd Normal Form (BCNF)

**ANSWER: b) Second Normal Form (2NF)**
- 2NF specifically eliminates partial dependencies

---

**20.** What is a **transitive dependency**?
- a) When an attribute depends on the entire composite key
- b) When A → B and B → C, so A → C indirectly
- c) When an attribute depends on only part of the primary key
- d) When two attributes depend on each other

**ANSWER: b) When A → B and B → C, so A → C indirectly**
- This is the definition of transitive dependency

---

**21.** In an ERD, what does a **bridge entity** (associative entity) represent?
- a) A weak entity that cannot exist independently
- b) An entity that resolves a many-to-many relationship
- c) An entity with no attributes
- d) The primary entity in a one-to-one relationship

**ANSWER: b) An entity that resolves a many-to-many relationship**
- Bridge/associative entities break M:N into two 1:M relationships

---

**22.** Consider this table: **COURSE(CourseID, CourseName, InstructorID, InstructorName, InstructorOffice)**

If `CourseID → InstructorID` and `InstructorID → InstructorName, InstructorOffice`, which normal form is violated?
- a) 1NF
- b) 2NF
- c) 3NF
- d) None - this is properly normalized

**ANSWER: c) 3NF**
- Transitive dependency exists: CourseID → InstructorID → InstructorName/Office
- Table is in 2NF (no partial dependencies with single-column PK) but violates 3NF

---

**23.** What is the primary purpose of **normalization**?
- a) To make queries run faster
- b) To reduce data redundancy and prevent anomalies
- c) To combine multiple tables into one
- d) To create more complex database structures

**ANSWER: b) To reduce data redundancy and prevent anomalies**
- This is the primary purpose of normalization

---

**24.** In the functional dependency notation `ISBN → BookTitle`, which term describes ISBN?
- a) Dependent
- b) Determinant
- c) Composite key
- d) Foreign key

**ANSWER: b) Determinant**
- The left side of X → Y is the determinant

---

**25.** Which of the following scenarios would most likely benefit from **denormalization**?
- a) A frequently-run report that requires joining 8 tables and is too slow
- b) A brand new database with no performance issues
- c) A table with update anomalies
- d) A table that violates 1NF

**ANSWER: a) A frequently-run report that requires joining 8 tables and is too slow**
- Performance issues are the main reason to denormalize

---

**26.** Consider: **ENROLLMENT(StudentID, CourseID, StudentName, Grade)**

Primary Key: `{StudentID, CourseID}`

Dependency: `StudentID → StudentName`

What type of dependency problem exists?
- a) Full dependency
- b) Partial dependency
- c) Transitive dependency
- d) No problem exists

**ANSWER: b) Partial dependency**
- StudentName depends on only part of the composite key {StudentID, CourseID}

---

**27.** In crow's feet notation, what does a **perpendicular line** (|) on a relationship line indicate?
- a) Optional participation (zero allowed)
- b) Mandatory participation (at least one required)
- c) Many instances
- d) Exactly one instance

**ANSWER: b) Mandatory participation (at least one required)**
- Perpendicular line = mandatory, circle = optional

---

**28.** Which normal form requires that **every determinant must be a candidate key**?
- a) 1NF
- b) 2NF
- c) 3NF
- d) BCNF

**ANSWER: d) BCNF**
- BCNF requires all determinants to be candidate keys

---

**29.** What is the relationship between STUDENT and COURSE entities if:
- One student can enroll in many courses
- One course can have many students enrolled
- a) One-to-one
- b) One-to-many
- c) Many-to-one
- d) Many-to-many

**ANSWER: d) Many-to-many**
- Many students can take many courses (M:N relationship)

---

**30.** Given: **ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName)**

Primary Key: `{OrderID, ProductID}`

If `ProductID → ProductName`, to achieve 2NF you should:
- a) Remove ProductName entirely
- b) Create a separate PRODUCT table with ProductID and ProductName
- c) Add ProductName to the primary key
- d) Leave it as is - it's already in 2NF

**ANSWER: b) Create a separate PRODUCT table with ProductID and ProductName**
- This removes the partial dependency (ProductID → ProductName)

---

**31.** Which of the following best describes **cardinality constraints**?
- a) The data types allowed in a column
- b) The number of rows in a table
- c) The number of entity instances that can participate in a relationship
- d) The number of attributes an entity has

**ANSWER: c) The number of entity instances that can participate in a relationship**
- Cardinality defines relationship quantities (1:1, 1:M, M:N)

---

**32.** Why is 3NF considered sufficient for most real-world applications?
- a) It's the easiest to understand
- b) It balances data integrity with reasonable complexity
- c) Higher normal forms don't exist
- d) It requires the fewest number of tables

**ANSWER: b) It balances data integrity with reasonable complexity**
- 3NF provides good integrity without excessive complexity

---

**33.** What type of attribute would "DateOfBirth" be in a PERSON entity on an ERD?
- a) Composite attribute
- b) Multivalued attribute
- c) Derived attribute
- d) Simple attribute

**ANSWER: d) Simple attribute**
- DateOfBirth is a single, atomic value (not composite, multivalued, or derived)

---

## PART C: SHORT ANSWER (32.5 points total)

---

**Question 34 (4 points):** Explain the difference between a **primary key** and a **foreign key**. Provide an example of each.

**ANSWER:**

**Primary Key (PK):** (2 points)
- A column (or set of columns) that uniquely identifies each row in a table
- Cannot contain NULL values
- Example: StudentID in STUDENT table

**Foreign Key (FK):** (2 points)
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

**ANSWER:**

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

a) **One and only one** (mandatory one)

b) **Zero or many** (optional many)

c) **One or many** (mandatory many)

**ANSWER:**

a) **One and only one** (mandatory one): **|—** (1.5 points)
   - Perpendicular line (mandatory) + single line (one)
   - Drawing: `|—` or `⊣—`

b) **Zero or many** (optional many): **o≺** (1.5 points)
   - Circle (optional) + crow's foot (many)
   - Drawing: `o≺` or `○<`

c) **One or many** (mandatory many): **|≺** (2 points)
   - Perpendicular line (mandatory) + crow's foot (many)
   - Drawing: `|≺` or `⊣<`

**Grading:**
- Award full points if symbols are correct
- Deduct 0.5 points if close but minor errors
- Must show both the mandatory/optional indicator AND the one/many indicator

---

**Question 37 (6 points):** Given this table in 1NF:

**EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)**

- Primary Key: EmpID
- Functional Dependencies:
  - `EmpID → EmpName, DeptID`
  - `DeptID → DeptName, DeptLocation`

a) What normal form violation exists in this table? **(2 points)**

b) Explain why this is a problem (what anomaly could occur?). **(2 points)**

c) Decompose this table to fix the problem. Show the resulting table structures with their primary keys. **(2 points)**

**ANSWER:**

**a) Transitive dependency / Violates 3NF** (2 points)
- EmpID → DeptID → DeptName, DeptLocation
- This is a transitive dependency

**b) Anomalies that could occur:** (2 points - must mention at least one specific anomaly)
- **Update anomaly:** If a department changes location, must update multiple employee records
- **Deletion anomaly:** If the last employee in a department is deleted, we lose department information
- **Insertion anomaly:** Cannot add a new department without hiring an employee

(Student needs only one, but any of these answers is acceptable)

**c) Decomposed tables:** (2 points)

**EMPLOYEE Table:**
- EmpID (PK)
- EmpName
- DeptID (FK)

**DEPARTMENT Table:**
- DeptID (PK)
- DeptName
- DeptLocation

**Grading:**
- Part (a): 2 points for identifying transitive dependency or 3NF violation
- Part (b): 2 points for explaining a specific anomaly
- Part (c): 1 point for correct EMPLOYEE table, 1 point for correct DEPARTMENT table
- Must show primary keys (PK) indicated

---

**Question 38 (5 points):** A university database needs to track students and courses.

- A student can enroll in many courses
- A course can have many students
- For each enrollment, we need to track the grade and semester

Draw a simple ERD showing these three entities (STUDENT, COURSE, and the appropriate bridge entity) with their relationships using crow's feet notation. Label the entities and show the relationship lines with proper notation.

**ANSWER:**

```
     One student, many enrollments          One course, many enrollments
              (1:M)                                    (1:M)

STUDENT ——|—————o≺—— ENROLLMENT ——≺o—————|—— COURSE

┌─────────┐          ┌────────────┐          ┌─────────┐
│ STUDENT │          │ ENROLLMENT │          │ COURSE  │
├─────────┤          ├────────────┤          ├─────────┤
│StudentID│          │StudentID(FK)│         │CourseID │
│  (PK)   │          │CourseID(FK)│          │  (PK)   │
│         │          │ {PK}       │          │         │
│         │          │Grade       │          │         │
│         │          │Semester    │          │         │
└─────────┘          └────────────┘          └─────────┘
```

**Text description:**
- STUDENT entity with one-to-many relationship to ENROLLMENT
- COURSE entity with one-to-many relationship to ENROLLMENT
- ENROLLMENT is the bridge entity with composite key {StudentID, CourseID}
- ENROLLMENT contains Grade and Semester attributes
- Crow's feet notation showing "many" on ENROLLMENT side

**Grading:**
- 1 point for STUDENT entity box/label
- 1 point for COURSE entity box/label
- 1 point for ENROLLMENT bridge entity
- 1 point for correct relationship lines with crow's feet notation
- 1 point for indicating Grade and Semester are stored in ENROLLMENT

**Accept reasonable variations in notation as long as the relationships are correct**

---

**Question 39 (3.5 points):** List the three types of database anomalies that normalization helps prevent and provide a one-sentence description of each.

**ANSWER:**

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

**ANSWER:** (2 points each scenario)

Acceptable scenarios include:

**Scenario 1: Read-heavy reporting/analytics**
- Frequently-run reports that join many tables and perform slowly
- Data warehouse or business intelligence applications
- Dashboard queries that need fast response times

**Scenario 2: Performance-critical queries**
- High-traffic queries that are causing bottlenecks
- Real-time systems where query speed is critical
- Calculated fields that are expensive to compute repeatedly

**Other acceptable scenarios:**

**Historical/archived data:**
- Snapshot tables that preserve data as it was at a point in time
- Audit trails or versioning systems

**Materialized views:**
- Pre-computed aggregations or summaries
- Caching complex join results

**Grading:**
- 2 points per valid scenario
- Must be specific and explain WHY denormalization helps
- Generic answers like "for performance" without specifics = 1 point
- Must identify TWO distinct scenarios

---

## END OF EXAM

---

## GRADING RUBRIC SUMMARY

| Section | Points | Notes |
|---------|--------|-------|
| **Part A (T/F)** | 22.5 | 1.5 points × 15 questions |
| **Part B (Multiple Choice)** | 45 | 2.5 points × 18 questions |
| **Part C (Short Answer)** | 32.5 | Variable points, see individual answers |
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
