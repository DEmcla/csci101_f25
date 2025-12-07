# CSCI 101: Module 2 Study Guide (Enhanced Edition)
## Database Design, ERD, Normalization, and Relationships

---

## 🎯 START HERE: Which Study Path Is Right for You?

**Answer these questions to find your path:**

### ✅ Are you prepared for this exam?

**Path A: Well-Prepared Student**
- ✓ Completed all assigned readings (Normalization_ln1, ln2, ln3)
- ✓ Attended all classes and took notes
- ✓ Completed homework assignments
- ✓ Understand most concepts, just need review

👉 **Use: "Quick Review Track" (30-60 minutes)** then target specific weak areas

---

**Path B: Average Student**
- ✓ Did most readings and assignments
- ✓ Attended most classes
- ⚠️ Some concepts are fuzzy
- ⚠️ Need structured review

👉 **Use: "3-Hour Crash Course"** (recommended)

---

**Path C: Struggling Student**
- ✗ Missed several classes or readings
- ✗ Didn't complete all assignments
- ✗ Many concepts unclear
- ✗ Need to learn from scratch

👉 **Use: "Emergency Rescue Guide"** (Start below, then move to 3-Hour Crash Course)

---

## 🆘 EMERGENCY RESCUE GUIDE (For Path C Students)

*Start here if you missed most of the coursework. This gives you the absolute basics.*

### What You MUST Know to Pass (30 minutes)

#### Concept #1: What is a Database Table?
Think of it like a spreadsheet with rows and columns.
- **Rows** = individual records (like one student, one order)
- **Columns** = properties (like name, date, price)
- **Primary Key** = unique identifier (like Student ID)

#### Concept #2: Relationships Between Tables
Tables can be connected:
- **One-to-Many:** One customer has many orders
- **Many-to-Many:** Many students take many courses (need bridge table)

#### Concept #3: The Three Normal Forms (Super Simplified)
- **1NF:** No lists in cells (split "555-1234, 555-5678" into separate rows)
- **2NF:** Everything depends on the FULL key (not just part of it)
- **3NF:** No chains (A→B→C is bad)

#### Concept #4: Crow's Feet Symbols (MEMORIZE THESE)
```
|—  = exactly one (required)
o—  = zero or one (optional)
|≺  = one or more (required, many)
o≺  = zero or more (optional, many)
```

#### Concept #5: When You Need a Bridge Table
**ONLY for Many-to-Many relationships!**
Example: Students ↔ Courses needs ENROLLMENT bridge table

---

### Can You Answer These 5 Basic Questions?

❓ **Q1:** What uniquely identifies each row in a table?
<details><summary>Click for answer</summary>
Primary Key (PK)
</details>

❓ **Q2:** "PhoneNumber: 555-1234, 555-5678" - What's wrong?
<details><summary>Click for answer</summary>
Multiple values in one cell - violates 1NF (not atomic)
</details>

❓ **Q3:** Do One-to-Many relationships need a bridge table?
<details><summary>Click for answer</summary>
NO - only Many-to-Many needs bridge tables
</details>

❓ **Q4:** In EMPLOYEE table, EmpID → DeptID → DeptName. What's the problem?
<details><summary>Click for answer</summary>
Transitive dependency - violates 3NF
</details>

❓ **Q5:** What does this mean: CUSTOMER ——|—————o≺—— ORDER?
<details><summary>Click for answer</summary>
One customer has zero or more orders; one order has exactly one customer
</details>

**If you got 3+ correct:** Proceed to 3-Hour Crash Course
**If you got 0-2 correct:** Read this section again, then watch [suggest YouTube video or office hours]

---

## ⚡ QUICK REVIEW TRACK (For Path A: Well-Prepared Students)

*You've done the work. Here's a 30-minute refresher.*

### Top 5 Concepts Students Get Wrong (Focus Here!)

#### ⚠️ **COMMON MISTAKE #1: Confusing Partial vs. Transitive Dependencies**

**Partial Dependency (violates 2NF):**
- Happens with COMPOSITE keys only
- Attribute depends on PART of the key
- Example: `{OrderID, ProductID} → ProductName` (ProductName only needs ProductID)

**Transitive Dependency (violates 3NF):**
- Can happen with any key
- Non-key attribute depends on another non-key attribute
- Example: `EmpID → DeptID → DeptName` (goes through DeptID)

📖 **Review:** Normalization_ln1.md (Section 4), Normalization_ln2.md (Section 2)

**Memory trick:**
- **Partial** = "Part" of the key
- **Transitive** = "Through" another attribute

---

#### ⚠️ **COMMON MISTAKE #2: When Bridge Tables Are Needed**

**Bridge tables are ONLY for Many-to-Many (M:N) relationships!**

❌ **Wrong:** "CUSTOMER → ORDER is many-to-many, needs bridge table"
- NO! One customer has many orders = One-to-Many (1:M)
- Just add CustomerID foreign key to ORDER table

✓ **Right:** "STUDENT ↔ COURSE is many-to-many, needs ENROLLMENT bridge"
- Students take many courses AND courses have many students = M:N
- Need ENROLLMENT(StudentID, CourseID, Grade, Semester)

📖 **Review:** Normalization_ln1.md (Section 5), In-class Exercise 3

---

#### ⚠️ **COMMON MISTAKE #3: Reading Crow's Feet Notation Direction**

Read from one entity TOWARD the other entity's symbols!

```
CUSTOMER ——|—————o≺—— ORDER
```

**Left to Right:** Start at CUSTOMER, look at ORDER end (o≺)
- "One customer can have zero or many orders"

**Right to Left:** Start at ORDER, look at CUSTOMER end (|—)
- "One order must belong to exactly one customer"

📖 **Review:** Normalization_ln1.md (Section 2)

**Tip:** The symbols you're looking at describe the OTHER entity!

---

#### ⚠️ **COMMON MISTAKE #4: Thinking 2NF Applies to Single-Column Keys**

**2NF only matters when you have a COMPOSITE primary key!**

✓ **Correct:**
- Table: STUDENT(StudentID, Name, Email) with PK: StudentID
- Single-column PK = automatically in 2NF (no "part" to depend on)

📖 **Review:** Homework 2 feedback, Normalization_ln1.md (Section 4)

**Quick Check:** Does the table have {Column1, Column2} as PK? If NO, skip 2NF check!

---

#### ⚠️ **COMMON MISTAKE #5: Forgetting Foreign Keys Make Relationships**

**Primary keys uniquely identify rows. Foreign keys CREATE relationships.**

```
STUDENT(StudentID, Name)     ← StudentID is PK
         ↑
         |
ENROLLMENT(StudentID, CourseID, Grade)  ← StudentID is FK pointing to STUDENT
         ↑
         |  Both are also part of composite PK!
```

📖 **Review:** Normalization_ln1.md (Section 3)

**Key insight:** A column can be BOTH a foreign key AND part of the primary key (common in bridge tables)!

---

### 10-Minute Memory Refresh

**Crow's Feet Notation:**
- Circle (o) = Optional
- Perpendicular (|) = Mandatory
- Single line = One
- Crow's foot (≺) = Many

**Normal Forms:**
- 1NF: Atomic, no repeating groups
- 2NF: 1NF + no partial dependencies (composite key issue)
- 3NF: 2NF + no transitive dependencies (chain issue)

**Anomalies (UID):**
- Update: Same data in many rows
- Insertion: Can't add without other data
- Deletion: Lose data when deleting

**Bridge Tables:**
- ONLY for M:N relationships
- PK = composite of both FKs
- Can have extra attributes (Grade, Date, etc.)

**You're Ready!** ✓

---

## 🚨 3-HOUR CRASH COURSE (For Path B: Average Students)

*Structured review of all key concepts with examples*

### Hour 1: Core Concepts Review (60 minutes)

#### ⏱️ Minutes 1-15: ERD & Relationship Fundamentals

**Entity Relationship Diagrams (ERDs):**
- **Rectangle** = Entity (like STUDENT, COURSE)
- **Oval** = Attribute (like StudentName, CourseID)
- **Diamond** = Relationship (connects entities)
- **Lines** = Show connections between entities

📖 **See Also:** Normalization_ln1.md (Introduction section)

---

**Crow's Feet Notation - THE MOST IMPORTANT SYMBOLS:**

Learn these four patterns:

1. **|— (Mandatory One):**
   - Perpendicular line + single line
   - Means: "exactly one, required"
   - Example: Every order MUST have exactly one customer
   - ⭐ **Difficulty: BASIC**

2. **o— (Optional One):**
   - Circle + single line
   - Means: "zero or one"
   - Example: A person MAY have zero or one driver's license
   - ⭐ **Difficulty: BASIC**

3. **|≺ (Mandatory Many):**
   - Perpendicular line + crow's foot
   - Means: "one or more, required"
   - Example: A department MUST have at least one employee
   - ⭐⭐ **Difficulty: MODERATE**

4. **o≺ (Optional Many):**
   - Circle + crow's foot
   - Means: "zero or more"
   - Example: A customer MAY have zero or more orders
   - ⭐⭐ **Difficulty: MODERATE**

**Quick Memory Trick:**
- **Circle (o)** = "Optional" (starts with O)
- **Perpendicular line (|)** = "Mandatory" (stands firm like a wall)
- **Single line** = "One"
- **Crow's foot (≺)** = "Many" (three toes = many)

---

**Relationship Types:**
- **One-to-One (1:1):** One person has one passport
- **One-to-Many (1:M):** One customer has many orders ⭐ **Most common**
- **Many-to-Many (M:N):** Many students take many courses ⭐⭐ **Needs bridge table**

**Key Rule:** Many-to-many relationships REQUIRE a bridge table (also called junction table or associative entity)

⚠️ **COMMON MISTAKE:** Students try to use bridge tables for 1:M relationships. Don't! Just add FK to the "many" side.

📖 **See Also:** In-class Exercise 2 (Student-Course ERD)

---

#### ⏱️ Minutes 16-30: Primary Keys & Foreign Keys

**Primary Key (PK):**
- Uniquely identifies each row in a table
- Cannot be NULL
- Can be single column (StudentID) or composite (OrderID + ProductID)
- Example: StudentID in STUDENT table
- ⭐ **Difficulty: BASIC**

**Foreign Key (FK):**
- Column in one table that points to a primary key in another table
- Creates the relationship between tables
- CAN be NULL (if relationship is optional)
- Example: StudentID in ENROLLMENT table (points to STUDENT table)
- ⭐⭐ **Difficulty: MODERATE**

**Composite Key:**
- Primary key made of 2+ columns working together
- Example: {StudentID, CourseID} in ENROLLMENT table
- Need BOTH values to uniquely identify a row
- ⭐⭐ **Difficulty: MODERATE**

**Quick Test:** Can you tell them apart?
- STUDENT(StudentID, Name, Email) ← StudentID is PK
- ENROLLMENT(StudentID, CourseID, Grade) ← {StudentID, CourseID} is composite PK, each is also FK

⚠️ **COMMON MISTAKE:** Thinking a column can't be BOTH a FK and part of a PK. It can! Bridge tables do this all the time.

📖 **See Also:** Normalization_ln1.md (Section 3: Keys), Homework 1 (Question 3)

---

#### ⏱️ Minutes 31-45: Functional Dependencies

**What is a Functional Dependency?**
- Notation: `X → Y` means "if you know X, you can determine Y"
- Read as: "X determines Y" or "Y depends on X"
- ⭐⭐ **Difficulty: MODERATE**

**Examples:**
- `StudentID → StudentName` (know ID, can find name)
- `ISBN → BookTitle` (know ISBN, can find book title)
- `{StudentID, CourseID} → Grade` (need both to find grade)

---

**Three Types to Know:**

1. **Full Dependency:** ⭐⭐
   - Attribute depends on the ENTIRE primary key
   - `{OrderID, ProductID} → Quantity` ✓ Good!
   - This is what you WANT

2. **Partial Dependency:** ⭐⭐⭐ **Most commonly confused**
   - Attribute depends on only PART of a composite key
   - `{OrderID, ProductID} → ProductName` ✗ Problem! (ProductName only needs ProductID)
   - **This violates 2NF**
   - ONLY possible with composite keys!

3. **Transitive Dependency:** ⭐⭐⭐ **Most commonly confused**
   - A → B and B → C, so A → C indirectly
   - `EmpID → DeptID → DeptName` ✗ Problem!
   - **This violates 3NF**
   - Can happen with any key (single or composite)

⚠️ **COMMON MISTAKE:** Confusing partial and transitive dependencies! They're BOTH "indirect" but in different ways:
- **Partial:** Depends on only PART of key (composite key problem)
- **Transitive:** Depends THROUGH another attribute (chain problem)

**Key Terms:**
- **Determinant** = left side of arrow (X in X → Y)
- **Dependent** = right side of arrow (Y in X → Y)

📖 **See Also:** Normalization_ln1.md (Section 4), Normalization_ln2.md (Introduction)

---

#### ⏱️ Minutes 46-60: Database Anomalies

**Three Anomalies Normalization Prevents:**

1. **Update Anomaly:** ⭐⭐
   - Same data appears in multiple rows
   - Changing it requires updating many places
   - Risk: Miss some rows, database becomes inconsistent
   - Example: Customer address repeated in every order row

2. **Insertion Anomaly:** ⭐⭐
   - Can't add data without adding other unrelated data
   - Example: Can't add a new department without first hiring an employee

3. **Deletion Anomaly:** ⭐⭐
   - Deleting one piece of data loses other important data
   - Example: Delete last employee in a department, lose all department info

**Memory Trick:**
- **UID** = Update, Insertion, Deletion (the three anomalies)

📖 **See Also:** Normalization_ln1.md (Introduction: The Problem), In-class discussion on why normalization matters

---

### Hour 2: Normal Forms Mastery (60 minutes)

#### ⏱️ Minutes 1-20: First Normal Form (1NF)

**Rule:** Every cell must contain a single atomic value (no lists, no repeating groups)
- ⭐ **Difficulty: BASIC - Easiest to recognize**

**Two Violations to Recognize:**

**Violation #1: Non-Atomic Values** ⭐
```
❌ BAD:
PhoneNumber: "555-1234, 555-5678"  (multiple values in one cell)

✓ GOOD:
Row 1: PhoneNumber: "555-1234"
Row 2: PhoneNumber: "555-5678"
```

**Violation #2: Repeating Groups** ⭐
```
❌ BAD:
| StudentID | Name | Course1 | Course2 | Course3 |

✓ GOOD:
| StudentID | Name | CourseID |
(Multiple rows per student, one course each)
```

**How to Fix 1NF Violations:**
1. Identify the repeating data
2. Create separate rows for each value
3. Consider creating a new table if needed

**Quick Check:** Does each cell contain exactly ONE value? If yes, you're in 1NF!

📖 **See Also:** Normalization_ln1.md (Section 3: 1NF), Example 1 in class

---

#### ⏱️ Minutes 21-40: Second Normal Form (2NF)

**Rule:** Must be in 1NF AND have no partial dependencies
- ⭐⭐⭐ **Difficulty: MODERATE-CHALLENGING**

**What's a Partial Dependency?**
- Non-key attribute depends on only PART of a composite primary key
- **ONLY applies to tables with composite keys!**
- If single-column PK → automatically in 2NF

⚠️ **COMMON MISTAKE:** Trying to find partial dependencies in single-column PK tables. There can't be any! No "part" to depend on!

**Example Problem:**
```
ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName)
Primary Key: {OrderID, ProductID}

Problem: ProductName → ProductID (only part of the key!)
This is a partial dependency!
```

**How to Fix:**
1. Identify what depends on only part of the composite key
2. Move those attributes to a new table
3. Use the partial key as the new table's primary key

**Solution:**
```
ORDER_DETAIL(OrderID, ProductID, Quantity)
  PK: {OrderID, ProductID}
  FK: ProductID → PRODUCT

PRODUCT(ProductID, ProductName)
  PK: ProductID
```

**Quick Check:**
- Does the table have a composite key? If NO, skip to 3NF (automatically in 2NF)
- If YES, does every non-key attribute depend on the ENTIRE key? If YES, you're in 2NF!

📖 **See Also:** Normalization_ln1.md (Section 4: 2NF), Homework 2 (Question 2)

---

#### ⏱️ Minutes 41-60: Third Normal Form (3NF)

**Rule:** Must be in 2NF AND have no transitive dependencies
- ⭐⭐⭐ **Difficulty: CHALLENGING - Most tested concept**

**What's a Transitive Dependency?**
- A → B and B → C, so A → C indirectly
- Non-key attribute depends on another non-key attribute
- Think of it as a "chain" of dependencies

⚠️ **COMMON MISTAKE:** Confusing transitive with partial!
- Partial = depends on PART of key (2NF)
- Transitive = depends THROUGH another attribute (3NF)

**Example Problem:**
```
EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)
Primary Key: EmpID

Problem: EmpID → DeptID → DeptName, DeptLocation
(Department info depends on DeptID, not directly on EmpID)

This is a transitive dependency chain!
```

**How to Fix:**
1. Identify the transitive dependency chain
2. Create a new table for the indirectly dependent attributes
3. Keep only the intermediate attribute (DeptID) in original table as FK

**Solution:**
```
EMPLOYEE(EmpID, EmpName, DeptID)
  PK: EmpID
  FK: DeptID → DEPARTMENT

DEPARTMENT(DeptID, DeptName, DeptLocation)
  PK: DeptID
```

**Why 3NF Matters:**
- **Industry standard** for most databases
- Balances data integrity with reasonable complexity
- Eliminates most redundancy problems

**Quick Check:**
- Are there any non-key attributes that depend on other non-key attributes? If NO, you're in 3NF!

📖 **See Also:** Normalization_ln2.md (entire lesson on 3NF), In-class Example 2, Homework 2 (Question 3)

---

### Hour 3: Practice & Application (60 minutes)

#### ⏱️ Minutes 1-20: Bridge Tables (Junction Tables)

**When Do You Need a Bridge Table?**
- **ONLY for Many-to-Many (M:N) relationships**
- Examples: Students ↔ Courses, Actors ↔ Movies, Authors ↔ Books
- ⭐⭐ **Difficulty: MODERATE**

⚠️ **COMMON MISTAKE #1:** Using bridge tables for 1:M relationships. DON'T!
⚠️ **COMMON MISTAKE #2:** Trying to create M:N without a bridge table. CAN'T!

**Why Bridge Tables?**
- Relational databases can't directly represent M:N relationships
- Bridge table breaks it into two 1:M relationships

**Example: Students and Courses**
```
STUDENT(StudentID, StudentName)
COURSE(CourseID, CourseName)

Bridge table:
ENROLLMENT(StudentID, CourseID, Grade, Semester)
  PK: {StudentID, CourseID}
  FK: StudentID → STUDENT
  FK: CourseID → COURSE
```

**Bridge Table Characteristics:**
- Primary key is usually a composite of the two foreign keys
- Can have additional attributes (Grade, Semester, EnrollmentDate)
- Connects the "many" sides of two entities

**Key Rule:** One-to-Many does NOT need a bridge table (just add FK to the "many" side)

📖 **See Also:** Normalization_ln1.md (Section 5: Bridge Tables), In-class Exercise 3

---

#### ⏱️ Minutes 21-40: Step-by-Step Decomposition Practice

**Example: Decompose to 3NF** ⭐⭐⭐

Given this unnormalized table:
```
COURSE_REGISTRATION(StudentID, StudentName, StudentMajor,
                    CourseID, CourseName, InstructorID, InstructorName)
PK: {StudentID, CourseID}
```

**Step 1: Check 1NF**
- ✓ All atomic values (no lists)
- ✓ No repeating groups
- ✓ Has primary key
- **Result: In 1NF**

**Step 2: Check 2NF** (look for partial dependencies)
- PK is composite: {StudentID, CourseID}
- StudentName depends on only StudentID (PARTIAL!)
- StudentMajor depends on only StudentID (PARTIAL!)
- CourseName depends on only CourseID (PARTIAL!)
- InstructorID depends on only CourseID (PARTIAL!)
- InstructorName depends on only CourseID (PARTIAL!)
- **Result: Violates 2NF - has partial dependencies**

**Fix for 2NF:** Create separate tables
```
STUDENT(StudentID, StudentName, StudentMajor)
  PK: StudentID

COURSE(CourseID, CourseName, InstructorID, InstructorName)
  PK: CourseID

ENROLLMENT(StudentID, CourseID)
  PK: {StudentID, CourseID}
  FK: StudentID → STUDENT
  FK: CourseID → COURSE
```

**Step 3: Check 3NF** (look for transitive dependencies)
- Look at COURSE table: CourseID → InstructorID → InstructorName
- This is transitive! InstructorName depends on InstructorID, not directly on CourseID
- **Result: COURSE table violates 3NF**

**Fix for 3NF:**
```
STUDENT(StudentID, StudentName, StudentMajor)
  PK: StudentID

COURSE(CourseID, CourseName, InstructorID)
  PK: CourseID
  FK: InstructorID → INSTRUCTOR

INSTRUCTOR(InstructorID, InstructorName)
  PK: InstructorID

ENROLLMENT(StudentID, CourseID)
  PK: {StudentID, CourseID}
  FK: StudentID → STUDENT
  FK: CourseID → COURSE
```

**Final Result:** All tables in 3NF! ✓

📖 **See Also:** This mirrors the process from Homework 2, Question 4

---

#### ⏱️ Minutes 41-60: Denormalization & Real-World Tradeoffs

**What is Denormalization?** ⭐⭐
- Intentionally adding redundancy back into a normalized database
- Trade-off: Better performance for worse data integrity
- ⚠️ Always normalize FIRST, then denormalize strategically!

**When to Denormalize:**

1. **Read-Heavy Reporting:**
   - Reports that join 5+ tables and run too slowly
   - Example: Store customer name in order table to avoid joining

2. **Performance-Critical Queries:**
   - High-traffic queries viewed millions of times
   - Example: Cache category name in product table

3. **Calculated Fields:**
   - Pre-calculate expensive aggregations
   - Example: Store total in ORDER table instead of summing ORDER_DETAIL

4. **Historical Snapshots:**
   - Preserve data as it was at a point in time
   - Example: Store customer address in order (even if customer moves later)

📖 **See Also:** Normalization_ln3.md (modern applications section)

---

## 📝 PRACTICE QUIZ (With Difficulty Ratings)

### Basic Questions ⭐ (Should get 100% correct)

1. What shape represents an entity in an ERD?
   - **Answer:** Rectangle

2. What does the symbol "o≺" mean in crow's feet notation?
   - **Answer:** Zero or many (optional many)

3. TRUE or FALSE: A primary key can be NULL.
   - **Answer:** FALSE

4. What does 1NF require?
   - **Answer:** Atomic values, no repeating groups

5. Is "PhoneNumbers: 555-1234, 555-5678" in 1NF?
   - **Answer:** NO (multiple values in one cell)

---

### Moderate Questions ⭐⭐ (Should get 70%+ correct)

6. TRUE or FALSE: A one-to-many relationship requires a bridge table.
   - **Answer:** FALSE (only M:N needs bridge table)

7. Where do you place the foreign key in a one-to-many relationship?
   - **Answer:** In the "many" side table

8. What is the primary key of a typical bridge table?
   - **Answer:** Composite key of the two foreign keys

9. If a table has single-column PK and is in 1NF, is it automatically in 2NF?
   - **Answer:** YES (no composite key = no partial dependencies)

10. What does 2NF eliminate?
    - **Answer:** Partial dependencies

11. What does 3NF eliminate?
    - **Answer:** Transitive dependencies

12. Why is 3NF considered the industry standard?
    - **Answer:** Balances data integrity with reasonable complexity

---

### Challenging Questions ⭐⭐⭐ (Target 50%+ correct)

13. Given PK: {OrderID, ProductID}, is "ProductID → ProductName" a partial dependency?
    - **Answer:** YES (depends on only ProductID, not full key)

14. TRUE or FALSE: Partial dependencies violate 3NF.
    - **Answer:** FALSE (they violate 2NF)

15. Given PK: EmpID, and "EmpID → DeptID → DeptName", what violates 3NF?
    - **Answer:** The transitive dependency (DeptID → DeptName)

16. Can a table with a single-column primary key have partial dependencies?
    - **Answer:** NO (no "part" of key to depend on)

17. Consider: ENROLLMENT(StudentID, CourseID, StudentName, Grade)
    Primary Key: {StudentID, CourseID}
    Dependency: StudentID → StudentName
    What type of dependency problem exists?
    - **Answer:** Partial dependency (StudentName depends on only part of composite key)

18. In COURSE(CourseID, CourseName, InstructorID, InstructorName, InstructorOffice), if CourseID → InstructorID and InstructorID → InstructorName, which normal form is violated?
    - **Answer:** 3NF (transitive dependency exists)

---

## 🎯 FINAL CHECKLIST: Am I Ready?

Rate your confidence (1-5) for each skill:

**Concepts:**
- ___ Can identify entities, attributes, relationships in ERD
- ___ Can read and draw crow's feet notation
- ___ Can determine relationship types (1:1, 1:M, M:N)
- ___ Understand when bridge tables are needed
- ___ Can identify primary keys (simple, composite)
- ___ Can identify foreign keys and their purpose
- ___ Understand functional dependency notation (X → Y)
- ___ Can identify partial dependencies
- ___ Can identify transitive dependencies
- ___ Know the requirements for 1NF, 2NF, 3NF
- ___ Can decompose tables to achieve higher normal forms
- ___ Understand the three types of database anomalies

**Skills:**
- ___ Given a scenario, can design an ERD with proper relationships
- ___ Can determine appropriate cardinality for relationships
- ___ Can identify normalization violations in a table
- ___ Can decompose unnormalized tables step-by-step
- ___ Can explain WHY a design violates a normal form
- ___ Can draw crow's feet notation symbols from memory

**If most ratings are 3+, you're ready!** 🎓
**If many ratings are 1-2, focus on those specific topics.**

---

## 📋 QUICK REFERENCE SHEET (Print This!)

**Crow's Feet Notation:**
- |— = Mandatory One
- o— = Optional One
- |≺ = Mandatory Many
- o≺ = Optional Many

**Normal Forms Quick Check:**
- **1NF:** Atomic values? No repeating groups? ✓
- **2NF:** 1NF + No partial dependencies? ✓ (only check if composite PK)
- **3NF:** 2NF + No transitive dependencies? ✓

**Functional Dependencies:**
- X → Y = "X determines Y"
- Partial = depends on PART of composite key (violates 2NF)
- Transitive = A → B → C (violates 3NF)

**Relationship Types:**
- **1:1** = One person, one passport (rare)
- **1:M** = One customer, many orders (FK in "many" side) ⭐ Most common
- **M:N** = Many students, many courses (NEEDS bridge table)

**Three Anomalies (UID):**
1. **Update:** Same data in multiple rows
2. **Insertion:** Can't add without other data
3. **Deletion:** Lose data when deleting

**Keys:**
- **PK:** Uniquely identifies row, not NULL, minimal
- **FK:** References PK in another table, creates relationship
- **Composite:** PK made of 2+ columns

---

## 💡 EXAM STRATEGY

**Time Management:**
- Read ALL questions first
- Answer easy questions first (⭐) to build confidence
- Budget time based on point values:
  - 2-point questions: ~2 minutes
  - 4-point questions: ~4 minutes
  - 6-7 point questions: ~8 minutes
- Save 5-10 minutes for review

**For True/False Questions (Part A):**
- Look for absolute words: "always," "never," "all," "none" (often false)
- Look for qualifier words: "usually," "often," "may" (often true)
- If unsure, think of a counterexample

**For Multiple Choice Questions (Part B):**
- Eliminate obviously wrong answers first
- Watch for "all of the above" or "none of the above" - test each option
- If two answers seem right, look for the BEST answer

**For Short Answer Questions (Part C):**
- Define terms clearly before using them
- Give examples when asked
- Explain your reasoning (show work on decomposition)
- Label your tables clearly (mark PKs and FKs)
- Even partial answers get partial credit - write something!

**For Diagram Questions:**
- Draw clearly (instructor needs to read it)
- Label everything (entities, relationships, notation)
- Use a ruler or straight edge if available
- Include a legend if notation might be unclear
- Show both mandatory/optional AND one/many indicators

**Common Mistakes to Avoid:**
- ❌ Don't confuse partial (2NF) and transitive (3NF) dependencies
- ❌ Don't forget the circle (o) for optional relationships
- ❌ Don't create bridge tables for 1:M relationships
- ❌ Don't skip stating what normal form is violated (name it explicitly!)
- ❌ Don't leave short answer questions blank (partial credit possible)

---

## 🆘 Still Confused? Get Help!

**Office Hours:** [Insert schedule]
**Tutoring Center:** [Insert location/hours]
**Study Groups:** [Insert information]
**Review Session:** [Insert date/time if applicable]

**Tonight Before Exam:**
- Review this study guide (focus on ⚠️ COMMON MISTAKES)
- Do the practice quiz (aim for 70%+)
- Get good sleep (seriously - sleep > cramming)
- Have materials ready (pencils, eraser, notes if allowed)

**Day of Exam:**
- Eat a good breakfast
- Arrive 10 minutes early
- Bring water if allowed
- Take deep breaths - you've got this!

---

## 🍀 Good Luck!

Remember: Understanding the "why" behind each rule is more important than memorizing. Think through the logic, and you'll do great!

**You've got this!** 💪

---

## 📚 Cross-References to Course Materials

**For deeper understanding, review:**

- **ERD & Cardinality:** Normalization_ln1.md (Section 1-2)
- **Keys & Relationships:** Normalization_ln1.md (Section 3)
- **1NF & 2NF:** Normalization_ln1.md (Section 4)
- **3NF & Transitive Dependencies:** Normalization_ln2.md (full lesson)
- **Bridge Tables:** Normalization_ln1.md (Section 5)
- **Advanced Topics:** Normalization_ln3.md (BCNF, 4NF, denormalization)
- **In-Class Examples:** Exercise 2 (Student-Course ERD), Exercise 3 (Library System)
- **Homework:** HW2 Questions 2-4 (normalization practice)

---

*Study guide created for CSCI 101 Module 2 Exam*
*Enhanced Edition with pathways for all student preparation levels*
*Topics: Database Design, ERD, Normalization, and Relationships*
