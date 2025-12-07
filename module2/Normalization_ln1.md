# Database Normalization: Class 1 – Foundations
## Building Better Database Schemas (1NF → 2NF)

### Class Overview (75 minutes)

**How to use this document:**
- **Before class:** Read through Key Concepts section, try the checkpoint questions
- **During class:** Follow along, add your own notes and examples in margins
- **After class:** Review checkpoints, complete practice problems, use for homework reference
- **Time allocations:** These show both in-class pacing and suggested study time for each section

| Segment | Topic                             | Time   |
|---------|-----------------------------------|--------|
| 1       | Introduction & Motivation         | 12 min |
| 2       | Key Concepts (with checkpoints)   | 25 min |
| 3       | First Normal Form (1NF)           | 10 min |
| 4       | Second Normal Form (2NF)          | 18 min |
| 5       | In-Class Practice (Examples 1-2)  | 25 min |
| 6       | Practice Review & Discussion      | 8 min  |
| 7       | Assignment Overview & Exit Ticket | 7 min  |

*Note: Class timing is approximate and will flex based on discussion and questions. Focus on understanding concepts rather than rushing through examples.*

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. **Identify** the three types of database anomalies (update, insertion, deletion) in unnormalized tables
2. **Define** functional dependencies and use the notation X → Y
3. **Determine** appropriate primary keys, including composite (multi-part) keys
4. **Recognize** violations of First Normal Form (1NF) and Second Normal Form (2NF)
5. **Decompose** tables into 2NF by eliminating partial dependencies
6. **Explain** how normalization prevents specific database problems

---

📖 **KEY TERMS FOR TODAY**
- **Atomic value**: A single value (not multiple values in one cell, like "555-1234, 555-5678")
- **Functional dependency**: If you know value A, you can look up value B (like StudentID → StudentName)
- **Primary key (PK)**: A column (or set of columns) that uniquely identifies each row in a table
- **Foreign key (FK)**: A column in one table that references the primary key of another table, creating a link between them
- **Composite key**: A primary key made from 2 or more columns working together
- **Partial dependency**: When data depends on only PART of a composite key (this causes problems!)
- **Decompose**: Break apart / split up a table into multiple smaller tables

---

## Introduction: Why Normalize Data?

You've learned to design ERDs showing entities and relationships. Today we learn how to organize data **within** those entities to prevent common database problems.

### The Problem: Database Anomalies

**Example: Unnormalized Student Registration Table**

| StudentID | StudentName | StudentEmail   | PhoneNumbers       | CourseID | CourseName        | Credits | Grade |
|-----------|-------------|----------------|--------------------|----------|-------------------|---------|-------|
| 101       | John Smith  | john@email.com | 555-1234, 555-5678 | CS101    | Intro Programming | 3       | A     |
| 101       | John Smith  | john@email.com | 555-1234, 555-5678 | MATH201  | Calculus I        | 4       | B     |
| 102       | Jane Doe    | jane@email.com | 555-9999           | CS101    | Intro Programming | 3       | A     |

**Three Critical Problems:**
1. **Update anomaly**: Changing John's email requires updating multiple rows
2. **Insertion anomaly**: Can't add a new course without a student enrollment
3. **Deletion anomaly**: If Jane drops CS101, we lose course information

➡️ **Solution: Normalization** – A systematic process to organize data efficiently

---

## Key Concepts

### Functional Dependencies

**Simple explanation:** When you know one piece of information (A), you can find another piece of information (B).

**Real-world analogy:** Think of a phone book:
- If you know someone's **name**, you can find their **phone number**
- The name DETERMINES the phone number you'll find
- We write this as: `Name → PhoneNumber`

**Formal notation**: `X → Y` means "X determines Y" or "If you know X, you can find Y"

**In our student registration example:**
- `StudentID → StudentName, StudentEmail`
  ↳ *If you know the StudentID (101), you can find the student's name (John Smith) and email*

- `CourseID → CourseName, Credits`
  ↳ *If you know the CourseID (CS101), you can find the course name and credit hours*

- `{StudentID, CourseID} → Grade`
  ↳ *You need BOTH StudentID AND CourseID together to find the grade (John's grade in CS101)*

**Key insight:** Functional dependencies help us understand what information "belongs together"

---

✋ **CHECKPOINT #1: Check Your Understanding**

Before moving on, make sure you can answer:
1. In the notation `CourseID → CourseName`, which value do you need to know first? (Answer: CourseID)
2. If `ISBN → BookTitle`, and you know the ISBN is "978-0-13-467626-6", what can you find? (Answer: The book title)
3. True or False: Functional dependencies are just about which columns relate to each other. (Answer: True!)

*Take 30 seconds to write one functional dependency from a database YOU use (social media, email, shopping, etc.)*

---

### Primary Keys
A **Primary Key (PK)** uniquely identifies each record. Let's think about our data:
- Can StudentID alone identify a row? No - one student has multiple rows (for different courses)
- Can CourseID alone identify a row? No - one course has multiple rows (for different students)
- What about StudentID + CourseID together? Yes! Each combination appears only once

This tells us our table **should have** a **composite primary key**: `{StudentID, CourseID}`

⚠️ **MISCONCEPTION ALERT:** Many students think primary keys must always be a single field. Not true! Composite keys (made from 2 or more fields) are very common, especially in tables that track relationships.

---

### Partial Dependencies

**Why this matters:** Once we have a composite key, we need to check if ALL data really needs the WHOLE key.

**Definition:** A **partial dependency** happens when an attribute depends on **only part** of a composite key (not the whole thing).

**Visual Example:** Let's look at our table with composite key `{StudentID, CourseID}`:

```
Question: Does StudentName need BOTH StudentID AND CourseID to be found?
Answer: No! StudentName only needs StudentID.
         ↳ This is a PARTIAL dependency (only uses part of the key)

Question: Does CourseName need BOTH StudentID AND CourseID to be found?
Answer: No! CourseName only needs CourseID.
         ↳ This is also a PARTIAL dependency

Question: Does Grade need BOTH StudentID AND CourseID to be found?
Answer: YES! You need to know which student AND which course to find the grade.
         ↳ This is a FULL dependency ✓ (uses the entire key)
```

**Summary for our table:**
- `StudentID → StudentName, StudentEmail` ← **partial** dependency (only uses part of key)
- `CourseID → CourseName, Credits` ← **partial** dependency (only uses part of key)
- `{StudentID, CourseID} → Grade` ← **full** dependency ✓ (uses entire key)

**The problem:** Partial dependencies cause data to repeat unnecessarily, creating all those anomalies we saw earlier!

**Important rule:** Partial dependencies can ONLY exist when you have a composite key. A table with a single-field primary key cannot have partial dependencies.

---

✋ **CHECKPOINT #2: Check Your Understanding**

Before moving on, make sure you can answer:
1. Can a table with a single-field primary key (like StudentID alone) have partial dependencies? (Answer: No! You need a composite key for partial dependencies to exist)
2. In a table with composite key `{OrderID, ProductID}`, if `ProductPrice` depends only on `ProductID`, is this a partial or full dependency? (Answer: Partial - it only needs part of the key)
3. Why are partial dependencies a problem? (Answer: They cause data to repeat unnecessarily, leading to anomalies)

⏸️ **Pause here.** Partial dependencies are tricky! Re-read lines 112-141 if needed before moving on.

---

## First Normal Form (1NF)

### Requirements
1. **Atomic values** – no multi-valued fields
2. **No repeating groups**
3. **Each row is unique**

### Converting to 1NF

**Before (Unnormalized):**
| StudentID | StudentName | StudentEmail   | PhoneNumbers       | CourseID | CourseName        | Credits | Grade |
|-----------|-------------|----------------|--------------------|----------|-------------------|---------|-------|
| 101       | John Smith  | john@email.com | 555-1234, 555-5678 | CS101    | Intro Programming | 3       | A     |
| 101       | John Smith  | john@email.com | 555-1234, 555-5678 | MATH201  | Calculus I        | 4       | B     |
| 102       | Jane Doe    | jane@email.com | 555-9999           | CS101    | Intro Programming | 3       | A     |

**Violation**: The PhoneNumbers column contains **multiple values** (non-atomic data)

**After (1NF) - Separating Phone Numbers:**
| StudentID | StudentName | StudentEmail   | PhoneNumber | CourseID | CourseName        | Credits | Grade |
|-----------|-------------|----------------|-------------|----------|-------------------|---------|-------|
| 101       | John Smith  | john@email.com | 555-1234    | CS101    | Intro Programming | 3       | A     |
| 101       | John Smith  | john@email.com | 555-1234    | MATH201  | Calculus I        | 4       | B     |
| 101       | John Smith  | john@email.com | 555-5678    | CS101    | Intro Programming | 3       | A     |
| 101       | John Smith  | john@email.com | 555-5678    | MATH201  | Calculus I        | 4       | B     |
| 102       | Jane Doe    | jane@email.com | 555-9999    | CS101    | Intro Programming | 3       | A     |

🔍 **Important Observation**: We've accomplished our 1NF goal - all values are now atomic!

**What 1NF fixed:** ✅
- ✅ No more multi-valued fields (phones are now individual rows)
- ✅ All values are atomic (single values only)
- ✅ We can now uniquely identify each row with `{StudentID, PhoneNumber, CourseID}`

**What we notice:**
- John's name/email appear 4 times instead of 2 (once per phone-course combination)
- Course info duplicates for each student phone number
- The composite key has three parts

**Is this a problem?** Yes - we still have redundancy! But that's exactly what the NEXT step (2NF) will fix.

**Understanding the process:** 🎯
- **1NF** = Make values atomic (we just did this!)
- **2NF** = Remove partial dependencies (coming up next - this will eliminate the redundancy!)
- **3NF** = Remove transitive dependencies (Class 2)

**Think of it like building a house:**
- 1NF = Foundation (structure is in place)
- 2NF = Framing (organize into proper rooms)
- 3NF = Finishing work (polish and optimize)

**Each step builds on the previous one.** Let's see how 2NF fixes our redundancy issues!

---

## Second Normal Form (2NF)

### Requirements
1. Already in 1NF
2. **No partial dependencies** – all non-key attributes depend on the **entire** primary key

### Analyzing Our 1NF Table

With composite key `{StudentID, PhoneNumber, CourseID}`, we have partial dependencies:
- `StudentID → StudentName, StudentEmail` (doesn't need PhoneNumber or CourseID)
- `CourseID → CourseName, Credits` (doesn't need StudentID or PhoneNumber)
- Only `Grade` depends on the student-course combination

### Solution: Decompose into Separate Tables

Break apart the data so each table has a clear, simple purpose:

#### 2NF Table Structure

**Visual Concept: One Big Messy Table → Four Small Clean Tables**

```
                    [Original Messy Table]
                     All data mixed together
                              |
                              | Decompose
                              ↓
        ┌──────────────┬──────────────┬──────────────┬──────────────┐
        ↓              ↓              ↓              ↓
    [STUDENT]    [STUDENT_PHONE]  [COURSE]     [ENROLLMENT]
  Student info    Phone numbers   Course info   Who takes what
```

**The Four Tables:**

| **STUDENT**    | **STUDENT_PHONE** | **COURSE**    | **ENROLLMENT** *(bridge table)* |
|----------------|-------------------|---------------|---------------------------------|
| StudentID (PK) | StudentID (FK)    | CourseID (PK) | StudentID (FK)                  |
| StudentName    | PhoneNumber       | CourseName    | CourseID (FK)                   |
| StudentEmail   |                   | Credits       | Grade                           |

**How the data flows:**
1. **STUDENT** stores info about students (name, email) - ONE row per student
2. **STUDENT_PHONE** stores phone numbers - MULTIPLE rows per student if they have multiple phones
3. **COURSE** stores info about courses (name, credits) - ONE row per course
4. **ENROLLMENT** connects students to courses and stores the grade - ONE row per student-course combination

**Note:** The ENROLLMENT table's primary key is `{StudentID, CourseID}` - the same composite key we identified earlier, but now it's in its own focused table! This is called a **bridge table** because it bridges the many-to-many relationship between students and courses.

### Relational Schema (Shorthand Notation)

**Legend:** `[PK]` = Primary Key | `[FK]` = Foreign Key | `→` = "references"

*Note: This notation is commonly used in textbooks and documentation. You don't need to memorize this format, but you should be able to read it.*

```
STUDENT(StudentID [PK], StudentName, StudentEmail)
STUDENT_PHONE(StudentID [FK], PhoneNumber)
COURSE(CourseID [PK], CourseName, Credits)
ENROLLMENT(StudentID [FK], CourseID [FK], Grade)
    Primary Key: {StudentID, CourseID}

FK STUDENT_PHONE.StudentID → STUDENT.StudentID
FK ENROLLMENT.StudentID → STUDENT.StudentID
FK ENROLLMENT.CourseID → COURSE.CourseID
```

**What this means in plain English:**
- The STUDENT table has StudentID as its primary key
- The STUDENT_PHONE table's StudentID is a foreign key that points back to the STUDENT table
- The ENROLLMENT table uses BOTH StudentID and CourseID together as its composite primary key
- Both fields in ENROLLMENT are also foreign keys linking to other tables

### Why This Works
✅ Each table represents **one concept**
✅ No more redundancy (John's name stored once)
✅ Can add students, courses, or phones independently
✅ Updates affect only one row
✅ The composite key lives where it belongs - in the relationship table

⚠️ **MISCONCEPTION ALERT:** Students sometimes think "More tables is always better." Not true! We stop at 2NF when we've eliminated partial dependencies. Over-normalizing can actually make databases harder to use. (We'll learn about 3NF and when to stop next class.)

---

## 🧩 In-Class Practice

### How to Approach Normalization Problems

**Follow these steps for each problem:**

```
STEP 1: Find the Composite Key
├─ Question: "What combination of fields makes each row unique?"
├─ Strategy: Look for what appears only once per row
└─ Test: Does this field combo appear more than once? If yes, keep adding fields

STEP 2: List All Functional Dependencies
├─ Question: "What determines what?"
├─ Strategy: For each field, ask: "Does knowing X let me find Y?"
└─ Write them as: X → Y

STEP 3: Identify Partial Dependencies
├─ Question: "Does this field need the WHOLE composite key or just part of it?"
├─ Strategy: Check each attribute against each part of the composite key
└─ Mark which dependencies are PARTIAL (use only part of key)

STEP 4: Create Tables
├─ Make one table for each PART of the composite key
├─ Move attributes that depend on only that part
├─ Keep fully-dependent attributes in a relationship table
└─ Don't forget: Each table needs a primary key!

STEP 5: Check Your Work
├─ Does each table represent ONE concept?
├─ Is data stored only ONCE (no redundancy)?
└─ Can you add/update/delete without anomalies?
```

**When You're Stuck:**
- 🔍 Not sure what the key is? Look for what combination appears only once
- 🔍 Can't find partial dependencies? Ask: "Does this field need ALL parts of the key?"
- 🔍 Don't know how many tables to create? Usually: one per key part + one relationship table

---

**Instructions**: Work in pairs. For each example:
1. Identify what the composite primary key should be
2. Find functional dependencies
3. Spot partial dependencies
4. Sketch the 2NF decomposition

### Example 1: Library Book Loans
```
Table: LIBRARY_LOANS
MemberID | MemberName | MemberPhone | BookID | BookTitle        | Author    | DueDate | Fine
201      | Alice Chen | 555-1010    | B01    | Database Systems | C.J. Date | 10/15   | 2.50
201      | Alice Chen | 555-1010    | B02    | SQL Basics       | Elmasri   | 10/22   | 0.00
202      | Ben Ortiz  | 555-2020    | B01    | Database Systems | C.J. Date | 10/18   | 1.00
```

**Guided Help:**
- **Finding the key:** Look at rows 1 and 3. Both have BookID = B01, but they're different loans (different members). Now look at rows 1 and 2. Both have MemberID = 201, but they're different loans (different books). So you need BOTH MemberID AND BookID together to identify a unique loan.
- **Partial dependencies:** Does MemberName need both MemberID and BookID? No, just MemberID! Does BookTitle need both? No, just BookID! These are partial dependencies.
- **Expected tables:** You should create 3 tables (MEMBER, BOOK, LOAN)

### Example 2: Employee Project Hours
```
Table: PROJECT_ASSIGNMENTS
EmpID | EmpName  | EmpDept | ProjectID | ProjectName | ProjectMgr | HoursWorked
501   | Dana Lee | HR      | P01       | Website     | Smith      | 10
501   | Dana Lee | HR      | P02       | Database    | Jones      | 5
502   | Omar Ali | Finance | P01       | Website     | Smith      | 8
```

**Guided Help:**
- **Finding the key:** Can you have the same employee on multiple projects? Yes (Dana is on P01 and P02). Can you have multiple employees on the same project? Yes (Dana and Omar both on P01). So the key must be: `{EmpID, ProjectID}`
- **Partial dependencies:** Think about EmpName and EmpDept - do they change based on which project? No! They only depend on EmpID. What about ProjectName and ProjectMgr? They only depend on ProjectID.
- **Expected tables:** You should create 3 tables (EMPLOYEE, PROJECT, ASSIGNMENT)

---

## Practice Review & Discussion

Let's review Example 1 together:
- **Composite Key Should Be**: `{MemberID, BookID}`
- **Partial Dependencies**: 
  - `MemberID → MemberName, MemberPhone`
  - `BookID → BookTitle, Author`
  - `{MemberID, BookID} → DueDate, Fine` (full dependency)
- **2NF Tables**: 
  - MEMBER(MemberID, MemberName, MemberPhone)
  - BOOK(BookID, BookTitle, Author)
  - LOAN(MemberID, BookID, DueDate, Fine)

---

## Assignment Overview

### Homework: Normalize StudentData.xlsx

**Part 1: Analysis (30 pts)**
- Identify what the primary key should be
- Find all functional dependencies
- Spot partial dependencies

**Part 2: Normalization (60 pts)**
- Convert to 1NF (20 pts)
- Convert to 2NF (40 pts)
- Show all primary/foreign keys

**Part 3: Reflection (10 pts)**
- What problems did 1NF solve?
- What problems did 2NF solve?
- What anomalies are prevented?

**Submission**: `LastName_FirstName_Normalization1.xlsx`
**Due**: Next class

---

## ✋ EXIT TICKET (Required - Turn in Before Leaving)

**Answer these 3 questions on an index card or paper:**

1. **Explain in your own words:** What's the difference between 1NF and 2NF? (2-3 sentences)

2. **Quick application:** In a table with composite key `{StudentID, ClubID}`, you find that `ClubMeetingRoom` depends only on `ClubID`. Is this a partial or full dependency?

3. **Reflection:** What's still confusing about normalization? What do you need to review before next class?

*Your instructor will review these before next class to address common confusion points.*

---

## Key Takeaways
- **1NF**: Makes values atomic, eliminates repeating groups
- **2NF**: Removes partial dependencies by decomposing tables
- **Composite keys** often indicate a need for decomposition
- **Each table = one concept**
- **Bridge tables** handle many-to-many relationships

## Next Class
**Third Normal Form (3NF)** – We'll tackle transitive dependencies and learn when to stop normalizing.

---

## Quick Reference Card

| Normal Form | Focus                | Key Question                                 |
|-------------|----------------------|----------------------------------------------|
| 1NF         | Atomic values        | "Are all values single?"                     |
| 2NF         | Partial dependencies | "Do all attributes depend on the WHOLE key?" |

**Remember:** First identify what your key SHOULD be, then check if all attributes depend on that entire key!