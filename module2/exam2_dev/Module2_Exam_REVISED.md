# CSCI 101: Module 2 Exam - REVISED VERSION
## Database Design, ERD, Normalization, and Relationships

**Name:** _________________________________ **Date:** _____________

**Time Limit:** 85 minutes
**Total Points:** 100 points
**Exam Type:** Open book, open notes, NO AI tools permitted
**Format:** Canvas exam - you may hand-draw diagrams and upload images

---

## Instructions

- This exam consists of **37 questions** divided into three sections:
  - **Part A: True/False** (13 questions, 1.5 points each = 19.5 points)
  - **Part B: Multiple Choice** (17 questions, 2.5 points each = 42.5 points)
  - **Part C: Short Answer** (7 questions, varies = 38 points)
- Write all answers clearly and legibly
- For diagram questions (Q36, Q38), you may hand-draw and upload a photo/scan
- You may use your notes, textbook, and course materials
- **You may NOT use AI tools (ChatGPT, Claude, etc.) or communicate with others**
- Time management suggestion:
  - Part A: 10 minutes
  - Part B: 30 minutes
  - Part C: 38 minutes
  - Review: 7 minutes

---

## PART A: TRUE/FALSE (19.5 points total)

**Instructions:** Select True or False. Each question is worth 1.5 points.

1. In an Entity Relationship Diagram (ERD), a rectangle represents an entity and an oval represents an attribute.

2. A primary key can be composed of multiple columns working together (a composite key).

3. In crow's feet notation, a "crow's foot" symbol indicates the "many" side of a relationship.

4. First Normal Form (1NF) requires eliminating transitive dependencies.

5. A functional dependency X → Y means "if you know X, you can determine Y."

6. Bridge tables (junction tables) are used to resolve one-to-one relationships.

7. A partial dependency occurs when a non-key attribute depends on only part of a composite primary key.

9. Second Normal Form (2NF) requires that the table must first be in 1NF and have no partial dependencies.

10. A foreign key in one table references the primary key of another table, creating a relationship between them.

11. In a many-to-many relationship, you can directly connect two tables without a bridge entity.

12. Third Normal Form (3NF) is considered the industry standard for most database applications.

13. Cardinality refers to the number of instances of one entity that can be associated with instances of another entity.

15. Update anomalies, insertion anomalies, and deletion anomalies are problems that normalization helps prevent.

---

## PART B: MULTIPLE CHOICE (42.5 points total)

**Instructions:** Select the BEST answer for each question. Each question is worth 2.5 points.

16. Which of the following is an example of a **non-atomic value** that violates 1NF?
    - a) StudentID: 12345
    - b) PhoneNumber: "555-1234, 555-5678"
    - c) LastName: "Smith"
    - d) GPA: 3.75

17. In crow's feet notation, which symbol combination represents a **one-to-many** relationship?
    - a) Single line on both ends
    - b) Single line on one end, crow's foot on the other
    - c) Crow's foot on both ends
    - d) Double line on both ends

18. Consider a table ORDER_DETAIL with **Primary Key: {OrderID, ProductID}**. Given the functional dependency `{OrderID, ProductID} → Quantity`, what type of key is `{OrderID, ProductID}`?
    - a) Foreign key
    - b) Simple primary key
    - c) Composite primary key
    - d) Candidate key

19. Which normal form specifically addresses the elimination of **partial dependencies**?
    - a) First Normal Form (1NF)
    - b) Second Normal Form (2NF)
    - c) Third Normal Form (3NF)
    - d) Boyce-Codd Normal Form (BCNF)

20. What is a **transitive dependency**?
    - a) When an attribute depends on the entire composite key
    - b) When A → B and B → C, so A → C indirectly
    - c) When an attribute depends on only part of the primary key
    - d) When two attributes depend on each other

21. In an ERD, what does a **bridge entity** (associative entity) represent?
    - a) A weak entity that cannot exist independently
    - b) An entity that resolves a many-to-many relationship
    - c) An entity with no attributes
    - d) The primary entity in a one-to-one relationship

22. Consider this table: **COURSE(CourseID, CourseName, InstructorID, InstructorName, InstructorOffice)**

    If `CourseID → InstructorID` and `InstructorID → InstructorName, InstructorOffice`, which normal form is violated?
    - a) 1NF
    - b) 2NF
    - c) 3NF
    - d) None - this is properly normalized

23. What is the primary purpose of **normalization**?
    - a) To make queries run faster
    - b) To reduce data redundancy and prevent anomalies
    - c) To combine multiple tables into one
    - d) To create more complex database structures

24. In the functional dependency notation `ISBN → BookTitle`, which term describes ISBN?
    - a) Dependent
    - b) Determinant
    - c) Composite key
    - d) Foreign key

25. Which of the following scenarios would most likely benefit from **denormalization**?
    - a) A frequently-run report that requires joining 8 tables and is too slow
    - b) A brand new database with no performance issues
    - c) A table with update anomalies
    - d) A table that violates 1NF

26. Consider: **ENROLLMENT(StudentID, CourseID, StudentName, Grade)**

    Primary Key: `{StudentID, CourseID}`

    Dependency: `StudentID → StudentName`

    What type of dependency problem exists?
    - a) Full dependency
    - b) Partial dependency
    - c) Transitive dependency
    - d) No problem exists

27. In crow's feet notation, what does a **perpendicular line** (|) on a relationship line indicate?
    - a) Optional participation (zero allowed)
    - b) Mandatory participation (at least one required)
    - c) Many instances
    - d) Exactly one instance

28. Which normal form requires that **every determinant must be a candidate key**?
    - a) 1NF
    - b) 2NF
    - c) 3NF
    - d) BCNF

29. What is the relationship between STUDENT and COURSE entities if:
    - One student can enroll in many courses
    - One course can have many students enrolled
    - a) One-to-one
    - b) One-to-many
    - c) Many-to-one
    - d) Many-to-many

30. Given: **ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName)**

    Primary Key: `{OrderID, ProductID}`

    If `ProductID → ProductName`, to achieve 2NF you should:
    - a) Remove ProductName entirely
    - b) Create a separate PRODUCT table with ProductID and ProductName
    - c) Add ProductName to the primary key
    - d) Leave it as is - it's already in 2NF

31. Which of the following best describes **cardinality constraints**?
    - a) The data types allowed in a column
    - b) The number of rows in a table
    - c) The number of entity instances that can participate in a relationship
    - d) The number of attributes an entity has

32. Why is 3NF considered sufficient for most real-world applications?
    - a) It's the easiest to understand
    - b) It balances data integrity with reasonable complexity
    - c) Higher normal forms don't exist
    - d) It requires the fewest number of tables

---

## PART C: SHORT ANSWER (38 points total)

**Instructions:** Answer each question clearly and completely. Show your work where applicable.

---

**Question 34 (4 points):** Explain the difference between a **primary key** and a **foreign key**. Provide an example of each.

*Answer:*

<br><br><br><br><br>

---

**Question 35 (5 points):** Consider this unnormalized table:

**LIBRARY_CHECKOUT**
| CardNumber | PatronName | BookISBN1 | BookTitle1 | BookISBN2 | BookTitle2 | CheckoutDate |
|------------|------------|-----------|------------|-----------|------------|--------------|
| C001 | Alice Brown | 978-01 | Database Design | 978-02 | Data Mining | 2024-01-15 |

Identify **TWO specific violations of First Normal Form (1NF)** in this table schema and explain why each is a problem.

*Answer:*

<br><br><br><br><br>

---

**Question 36 (6 points):** Draw the crow's feet notation symbols for the following. You may hand-draw and upload an image.

a) **One and only one** (mandatory one) - 2 points

b) **Zero or many** (optional many) - 2 points

c) **One or many** (mandatory many) - 2 points

**Note:** Each symbol should clearly show BOTH the mandatory/optional indicator AND the one/many indicator.

*Answer:* (Draw or upload image)

<br><br><br><br><br><br>

---

**Question 37 (7 points):** Given this table in 1NF:

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

**Question 38 (6 points):** A university database needs to track students and courses.

- A student can enroll in many courses
- A course can have many students
- For each enrollment, we need to track the grade and semester

Draw a simple ERD showing these three entities (STUDENT, COURSE, and the appropriate bridge entity) with their relationships using crow's feet notation. Label the entities and show the relationship lines with proper notation. Clearly indicate where Grade and Semester are stored. You may hand-draw and upload an image.

**Grading breakdown:**
- STUDENT entity: 1 point
- COURSE entity: 1 point
- ENROLLMENT bridge entity: 1.5 points
- Correct crow's feet notation on relationships: 1.5 points
- Grade and Semester shown in ENROLLMENT: 1 point

*Answer:* (Draw or upload image)

<br><br><br><br><br><br><br><br>

---

**Question 39 (4 points):** List the three types of database anomalies that normalization helps prevent and provide a one-sentence description of each.

*Answer:*

1.

2.

3.

<br><br>

---

**Question 40 (6 points):** When might a database designer choose to **denormalize** a properly normalized database? Give TWO specific scenarios where denormalization would be appropriate and explain WHY denormalization helps in each case.

**Grading:** 3 points per scenario (1.5 for scenario description, 1.5 for explanation of why it helps)

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
- ✓ Have you uploaded your hand-drawn diagrams for Q36 and Q38?
- ✓ Have you shown your work for short answer questions?
- ✓ Is your name on the exam?
- ✓ Have you reviewed your answers?

---

## FOR INSTRUCTOR USE ONLY

| Section | Points Earned | Points Possible |
|---------|---------------|-----------------|
| Part A (T/F) | _____ | 19.5 |
| Part B (Multiple Choice) | _____ | 42.5 |
| Part C (Short Answer) | _____ | 38 |
| **TOTAL** | **_____** | **100** |

**Comments:**
