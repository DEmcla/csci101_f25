# CSCI 101: Module 2 Exam
## Database Design, ERD, Normalization, and Relationships

**Name:** _________________________________ **Date:** _____________

**Time Limit:** 75 minutes
**Total Points:** 100 points
**Exam Type:** Open book, open notes, NO AI tools permitted
**Format:** Canvas exam - you may hand-draw diagrams and upload images

---

## Instructions

- This exam consists of **35 questions** divided into three sections:
  - **Part A: True/False** (12 questions, 2 points each = 24 points)
  - **Part B: Multiple Choice** (16 questions, 2.5 points each = 40 points)
  - **Part C: Short Answer** (7 questions, varies = 36 points)
- Write all answers clearly and legibly
- For diagram questions (Q29, Q31), you may hand-draw and upload a photo/scan
- You may use your notes, textbook, and course materials
- **You may NOT use AI tools (ChatGPT, Claude, etc.) or communicate with others**
- Time management suggestion:
  - Part A: 10 minutes
  - Part B: 28 minutes
  - Part C: 32 minutes
  - Review: 5 minutes

---

## PART A: TRUE/FALSE (24 points total)

**Instructions:** Select True or False. Each question is worth 2 points.

1. In an Entity Relationship Diagram (ERD), entities are represented as rectangles with the entity name at the top and attributes listed below in the text property.

2. A primary key can be composed of multiple columns working together (a composite key).

3. In crow's feet notation, a "crow's foot" symbol indicates the "many" side of a relationship.

4. First Normal Form (1NF) requires eliminating transitive dependencies.

5. A functional dependency X → Y means "if you know X, you can determine Y."

6. Bridge tables (junction tables) are used to resolve one-to-one relationships.

7. A partial dependency occurs when a non-key attribute depends on only part of a composite primary key.

8. Second Normal Form (2NF) requires that the table must first be in 1NF and have no partial dependencies.

9. A foreign key in one table references the primary key of another table, creating a relationship between them.

10. In a many-to-many relationship, you must use a bridge table (junction table) to properly connect two entities.

11. Third Normal Form (3NF) is considered the industry standard for most database applications.

12. Update anomalies, insertion anomalies, and deletion anomalies are problems that normalization helps prevent.

---

## PART B: MULTIPLE CHOICE (40 points total)

**Instructions:** Select the BEST answer for each question. Each question is worth 2.5 points.

13. Which of the following is an example of a **non-atomic value** that violates 1NF?
    - a) StudentID: 12345
    - b) PhoneNumber: "555-1234, 555-5678"
    - c) LastName: "Smith"
    - d) GPA: 3.75

14. In crow's feet notation, which symbol combination represents a **one-to-many** relationship?
    - a) Single line on both ends
    - b) Single line on one end, crow's foot on the other
    - c) Crow's foot on both ends
    - d) Double line on both ends

15. Consider a table ORDER_DETAIL with **Primary Key: {OrderID, ProductID}**. Given the functional dependency `{OrderID, ProductID} → Quantity`, what type of key is `{OrderID, ProductID}`?
    - a) Foreign key
    - b) Simple primary key
    - c) Composite primary key
    - d) Candidate key

16. Which normal form specifically addresses the elimination of **partial dependencies**?
    - a) First Normal Form (1NF)
    - b) Second Normal Form (2NF)
    - c) Third Normal Form (3NF)
    - d) Boyce-Codd Normal Form (BCNF)

17. What is a **transitive dependency**?
    - a) When an attribute depends on the entire composite key
    - b) When A → B and B → C, so A → C indirectly
    - c) When an attribute depends on only part of the primary key
    - d) When two attributes depend on each other

18. In an ERD, what does a **bridge entity** (associative entity) represent?
    - a) A weak entity that cannot exist independently
    - b) An entity that resolves a many-to-many relationship
    - c) An entity with no attributes
    - d) The primary entity in a one-to-one relationship

19. Consider this table: **COURSE(CourseID, CourseName, InstructorID, InstructorName, InstructorOffice)**

    If `CourseID → InstructorID` and `InstructorID → InstructorName, InstructorOffice`, which normal form is violated?
    - a) 1NF
    - b) 2NF
    - c) 3NF
    - d) None - this is properly normalized

20. What is the primary purpose of **normalization**?
    - a) To make queries run faster
    - b) To reduce data redundancy and prevent anomalies
    - c) To combine multiple tables into one
    - d) To create more complex database structures

21. In the functional dependency notation `ISBN → BookTitle`, which term describes ISBN?
    - a) Dependent
    - b) Determinant
    - c) Composite key
    - d) Foreign key

22. Which of the following scenarios would most likely benefit from **denormalization**?
    - a) A frequently-run report that requires joining 8 tables and is too slow
    - b) A brand new database with no performance issues
    - c) A table with update anomalies
    - d) A table that violates 1NF

23. Consider: **ENROLLMENT(StudentID, CourseID, StudentName, Grade)**

    Primary Key: `{StudentID, CourseID}`

    Dependency: `StudentID → StudentName`

    What type of dependency problem exists?
    - a) Full dependency
    - b) Partial dependency
    - c) Transitive dependency
    - d) No problem exists

24. In crow's feet notation, what does a **perpendicular line** (|) on a relationship line indicate?
    - a) Optional participation (zero allowed)
    - b) Mandatory participation (at least one required)
    - c) Many instances
    - d) Exactly one instance

25. What is the relationship between STUDENT and COURSE entities if:
    - One student can enroll in many courses
    - One course can have many students enrolled
    - a) One-to-one
    - b) One-to-many
    - c) Many-to-one
    - d) Many-to-many

26. Given: **ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName)**

    Primary Key: `{OrderID, ProductID}`

    If `ProductID → ProductName`, to achieve 2NF you should:
    - a) Remove ProductName entirely
    - b) Create a separate PRODUCT table with ProductID and ProductName
    - c) Add ProductName to the primary key
    - d) Leave it as is - it's already in 2NF

27. Which of the following best describes **cardinality constraints**?
    - a) The data types allowed in a column
    - b) The number of rows in a table
    - c) The number of entity instances that can participate in a relationship
    - d) The number of attributes an entity has

28. Why is 3NF considered sufficient for most real-world applications?
    - a) It's the easiest to understand
    - b) It balances data integrity with reasonable complexity
    - c) Higher normal forms don't exist
    - d) It requires the fewest number of tables

---

## PART C: SHORT ANSWER (36 points total)

**Instructions:** Answer each question clearly and completely. Show your work where applicable.

---

**Question 29 (4 points):** Explain the difference between a **primary key** and a **foreign key**. Provide an example of each.

*Answer:*

<br><br><br><br><br>

---

**Question 30 (5 points):** Consider this unnormalized table:

**LIBRARY_CHECKOUT**
| CardNumber | PatronName | BookISBN1 | BookTitle1 | BookISBN2 | BookTitle2 | CheckoutDate |
|------------|------------|-----------|------------|-----------|------------|--------------|
| C001 | Alice Brown | 978-01 | Database Design | 978-02 | Data Mining | 2024-01-15 |

Identify **TWO distinct structural violations of First Normal Form (1NF)** in this table schema and explain why each is a problem. (Note: Look for two separate types of problems in how the table is designed.)

*Answer:*

<br><br><br><br><br>

---

**Question 31 (6 points):** Draw the crow's feet notation symbols for the following. You may hand-draw and upload an image.

a) **One and only one** (mandatory one) - 2 points

b) **Zero or many** (optional many) - 2 points

c) **One or many** (mandatory many) - 2 points

**Note:** Each symbol should clearly show BOTH the mandatory/optional indicator AND the one/many indicator.

*Answer:* (Draw or upload image)

<br><br><br><br><br><br>

---

**Question 32 (7 points):** Given this table in 1NF:

**EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)**

- Primary Key: EmpID
- Functional Dependencies:
  - `EmpID → EmpName, DeptID`
  - `DeptID → DeptName, DeptLocation`

a) What normal form violation exists in this table? **(2 points)**

b) Explain why this is a problem (what anomaly could occur?). **(2 points)**

c) Decompose this table to fix the problem. Show the resulting table structures with their primary keys clearly marked. **(3 points: 1.5 per table)**

*Answer:*

<br><br><br><br><br><br><br><br>

---

**Question 33 (6 points):** A university database needs to track students and courses.

- A student can enroll in many courses
- A course can have many students
- For each enrollment, we need to track the grade and semester

Draw a simple ERD showing these three entities (STUDENT, COURSE, and the appropriate bridge entity) with their relationships using crow's feet notation. Label the entities and show the relationship lines with proper notation. Clearly indicate where Grade and Semester are stored and label primary keys (PK). You may hand-draw and upload an image.

**Grading breakdown:**
- STUDENT entity with PK labeled: 1 point
- COURSE entity with PK labeled: 1 point
- ENROLLMENT bridge entity with composite PK: 1.5 points
- Correct crow's feet notation on relationships: 1.5 points
- Grade and Semester shown in ENROLLMENT: 1 point

*Answer:* (Draw or upload image)

<br><br><br><br><br><br><br><br>

---

**Question 34 (4 points):** List the three types of database anomalies that normalization helps prevent and provide a one-sentence description of each.

*Answer:*

1.

2.

3.

<br><br>

---

**Question 35 (4 points):** When might a database designer choose to **denormalize** a properly normalized database? Give TWO specific scenarios where denormalization would be appropriate and explain WHY denormalization helps in each case.

**Grading:** 2 points per scenario (1 for scenario description, 1 for explanation of why it helps)

*Answer:*

Scenario 1:

Why it helps:

Scenario 2:

Why it helps:

<br><br>

---

## END OF EXAM

**Before you submit:**
- ✓ Have you answered all questions?
- ✓ Have you uploaded your hand-drawn diagrams for Q31 and Q33?
- ✓ Have you shown your work for short answer questions?
- ✓ Is your name on the exam?
- ✓ Have you reviewed your answers?

---

## FOR INSTRUCTOR USE ONLY

| Section | Points Earned | Points Possible |
|---------|---------------|-----------------|
| Part A (T/F) | _____ | 24 |
| Part B (Multiple Choice) | _____ | 40 |
| Part C (Short Answer) | _____ | 36 |
| **TOTAL** | **_____** | **100** |

**Comments:**
