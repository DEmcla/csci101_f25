# Database Normalization: Self-Paced Tutorial
## Third Normal Form (3NF) - The Industry Standard

---

### 📚 **Welcome to Your Self-Paced Learning Experience!**

This tutorial replaces today's class session. You'll learn about Third Normal Form (3NF) - the normalization level used in most professional databases.

**Prerequisites:** You should have completed Class 1 on 1NF and 2NF before starting this tutorial. This lesson builds directly on those concepts.

**Total Time: Approximately 90 minutes**

**What You'll Need:**
- ✏️ Paper and pencil for working through examples
- 📓 Your notes from Class 1 (for reference if needed)
- ⏰ 90 minutes of focused time

**How to Use This Tutorial:**
- Work through each section in order
- Don't skip the practice problems - they're essential!
- Check your answers immediately using the provided solutions
- If something is confusing, review that section before moving on
- Take short breaks between major sections

---

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:

1. **Identify** transitive dependencies in 2NF tables
2. **Decompose** tables to achieve 3NF by eliminating transitive dependencies
3. **Recognize** when 3NF is sufficient versus when higher forms are needed
4. **Evaluate** trade-offs between normalization levels and query complexity

---

## 📋 Tutorial Roadmap

| Section | Topic | Time | Progress |
|---------|-------|------|----------|
| 1 | Quick Review & Warm-Up | 10 min | ⬜ |
| 2 | Understanding Transitive Dependencies | 15 min | ⬜ |
| 3 | The 4-Step Process for 3NF | 15 min | ⬜ |
| 4 | Guided Practice Problem #1 | 20 min | ⬜ |
| 5 | Guided Practice Problem #2 | 20 min | ⬜ |
| 6 | When to Stop: 3NF vs Higher Forms | 10 min | ⬜ |

**Check off each section as you complete it!**

---

# Section 1: Quick Review & Warm-Up
⏱️ **Estimated Time: 10 minutes**

Before diving into 3NF, let's make sure you remember the key concepts from Class 1.

## What We've Learned So Far

### 1NF (First Normal Form) Solved:
- ✅ Non-atomic values (multiple items in one field)
- ✅ Repeating groups

### 2NF (Second Normal Form) Solved:
- ✅ Partial dependencies (non-key attributes depending on part of composite key)

### Still Need to Solve:
- ❌ **Transitive dependencies** - indirect relationships through other attributes
- ❌ **Complex key relationships** - edge cases that 3NF doesn't handle

---

## 🧪 Warm-Up Quiz (5 minutes)

**Test your memory from Class 1:**

**Question 1:** What is the composite key in this table?

| OrderID | ProductID | ProductName | Quantity |
|---------|-----------|-------------|----------|
| 1001    | P50       | Laptop      | 2        |
| 1001    | P51       | Mouse       | 1        |

<details>
<summary>Click to reveal answer</summary>

**Answer:** `{OrderID, ProductID}` - you need both fields together to uniquely identify each row.

- OrderID alone doesn't work (1001 appears twice)
- ProductID alone doesn't work (different orders can have the same product)
- Together they uniquely identify each row
</details>

---

**Question 2:** Is this a partial dependency?

- Table key: `{OrderID, ProductID}`
- Dependency: `ProductID → ProductName`

<details>
<summary>Click to reveal answer</summary>

**Answer:** YES - this is a partial dependency.

**Why?** ProductName depends on only PART of the composite key (just ProductID), not the whole key {OrderID, ProductID}.

**How to fix:** Move ProductName to a separate PRODUCT table where ProductID is the primary key.
</details>

---

**Question 3:** After fixing the partial dependency above, how many tables would you have?

<details>
<summary>Click to reveal answer</summary>

**Answer:** 3 tables

1. **ORDER** table (OrderID, order-specific info)
2. **PRODUCT** table (ProductID, ProductName)
3. **ORDER_DETAIL** table (OrderID, ProductID, Quantity) - the bridge table

**Why 3 tables?** The bridge table (ORDER_DETAIL) connects orders to products and stores the quantity for each order-product combination.
</details>

---

## ⚠️ Before You Continue

**If you struggled with these warm-up questions:**
- Review your notes from Class 1
- Re-read the 1NF and 2NF sections
- Ask questions on the class forum before continuing

**If you got all three correct:** Great! You're ready to move on to 3NF! ✅

---

**✅ Section 1 Complete! Check it off in the roadmap above.**

---

# Section 2: Understanding Transitive Dependencies
⏱️ **Estimated Time: 15 minutes**

## The Problem We're Solving

Even after achieving 2NF, we can still have serious data integrity problems. Let's look at an example.

### Real-World Example: Course Registration System

**Course Table (in 2NF, but still has problems):**

| CourseID | CourseName        | Credits | InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|----------|-------------------|---------|--------------|----------------|------------------|-----------------|
| CS101    | Intro Programming | 3       | I001         | Dr. Johnson    | Room 101         | 555-1234        |
| MATH201  | Calculus I        | 4       | I002         | Dr. Williams   | Room 205         | 555-5678        |
| CS201    | Data Structures   | 4       | I001         | Dr. Johnson    | Room 101         | 555-1234        |

**Stop and Think (2 minutes):**
- What problems do you see in this table?
- What happens if Dr. Johnson moves to Room 102?
- What if Dr. Johnson's phone number changes?

<details>
<summary>Click to see the problems</summary>

### Problems with This Table:

1. **Update Anomaly**: If Dr. Johnson moves to Room 102, we must update:
   - The CS101 row
   - The CS201 row
   - Any other course Dr. Johnson teaches
   - Two updates for one real-world fact!

2. **Insertion Anomaly**: We can't add a new instructor to the system until they're assigned to teach a course.

3. **Deletion Anomaly**: If CS201 is cancelled and deleted, we lose information about Dr. Johnson (assuming CS101 is also deleted).

**Sound familiar?** These are the SAME three anomalies from 1NF and 2NF! That's because we still have a structural problem.
</details>

---

## What Is a Transitive Dependency?

### The Dependency Chain

Let's trace how information flows in the Course table:

```
[CourseID] ──────→ [InstructorID] ──────→ [InstructorName]
   PRIMARY          INTERMEDIATE              ENDPOINT
     KEY              BRIDGE

CourseID determines InstructorID (direct)
InstructorID determines InstructorName (direct)
CourseID determines InstructorName (INDIRECT - through InstructorID)
```

**This indirect relationship is called a TRANSITIVE DEPENDENCY.**

---

### The Formal Definition

**Transitive Dependency:** When `A → B` and `B → C`, then `A → C` indirectly.

In our example:
- `CourseID → InstructorID` (A → B)
- `InstructorID → InstructorName` (B → C)
- Therefore: `CourseID → InstructorName` (A → C) **transitively**

---

### The Pattern to Recognize

🔍 **"Information about the information"**

Ask yourself: Does this field describe:
- ✅ The primary key (CourseID)?
- ❌ Another field in the table?

**Examples:**
- `InstructorName` describes the **instructor**, NOT the course → Transitive dependency!
- `InstructorOffice` describes the **instructor**, NOT the course → Transitive dependency!
- `CourseName` describes the **course** directly → OK!
- `Credits` describes the **course** directly → OK!

---

## 🧪 Check Your Understanding (3 minutes)

Look at this table:

| EmployeeID | EmployeeName | DeptID | DeptName | DeptLocation |
|------------|--------------|--------|----------|--------------|
| E01        | Alice        | D10    | Sales    | Building A   |
| E02        | Bob          | D10    | Sales    | Building A   |
| E03        | Carol        | D20    | IT       | Building B   |

Primary Key: EmployeeID

**Question 1:** What field creates a transitive dependency chain?

<details>
<summary>Click to reveal answer</summary>

**Answer:** DeptID is the intermediate field that creates transitive dependencies.

**The chains:**
```
EmployeeID → DeptID → DeptName
EmployeeID → DeptID → DeptLocation
```

DeptName and DeptLocation describe the DEPARTMENT, not the EMPLOYEE.
</details>

---

**Question 2:** What would happen if the Sales department moves to Building C?

<details>
<summary>Click to reveal answer</summary>

**Answer:** You'd have to update TWO rows (E01 and E02).

This is an **UPDATE ANOMALY** - changing one fact (department location) requires multiple row updates. This is inefficient and error-prone (what if you miss one?).
</details>

---

**✅ Section 2 Complete! Check it off in the roadmap.**

---

# Section 3: The 4-Step Process for 3NF
⏱️ **Estimated Time: 15 minutes**

Now you'll learn a systematic process to identify and fix transitive dependencies.

## The 4-Step Process

```
STEP 1: List ALL Functional Dependencies
├─ Write down every dependency in the table
├─ Include both direct and potential indirect ones
└─ Format: FieldA → FieldB

STEP 2: Look for Dependency Chains
├─ Find patterns: A → B → C
├─ Ask: "Does the primary key determine B, and then B determines C?"
└─ If YES → you found a transitive dependency

STEP 3: Check Non-Key Dependencies
├─ For each non-key attribute, ask: "Does it depend on another non-key attribute?"
├─ Example: Does InstructorName depend on InstructorID (both non-key)?
└─ If YES → transitive dependency exists

STEP 4: Decompose into Separate Tables
├─ Create a new table for the transitively dependent attributes
├─ Use the intermediate field (B) as the primary key in the new table
└─ Keep a foreign key in the original table to maintain the relationship
```

---

## Worked Example: Course Table

Let's apply all 4 steps to the Course table we saw earlier.

**Original Table:**

| CourseID | CourseName        | Credits | InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|----------|-------------------|---------|--------------|----------------|------------------|-----------------|
| CS101    | Intro Programming | 3       | I001         | Dr. Johnson    | Room 101         | 555-1234        |
| MATH201  | Calculus I        | 4       | I002         | Dr. Williams   | Room 205         | 555-5678        |
| CS201    | Data Structures   | 4       | I001         | Dr. Johnson    | Room 101         | 555-1234        |

Primary Key: CourseID

---

### STEP 1: List ALL Functional Dependencies

**Your Turn (3 minutes):** Before looking at the answer, try to list all the functional dependencies in this table.

<details>
<summary>Click to see all dependencies</summary>

```
CourseID → CourseName
CourseID → Credits
CourseID → InstructorID
CourseID → InstructorName
CourseID → InstructorOffice
CourseID → InstructorPhone
InstructorID → InstructorName
InstructorID → InstructorOffice
InstructorID → InstructorPhone
```

**Notice:** Some dependencies start with CourseID (the key), others start with InstructorID (non-key).
</details>

---

### STEP 2: Look for Dependency Chains

**Your Turn (2 minutes):** Can you spot the chains? Look for A → B → C patterns.

<details>
<summary>Click to see the chains</summary>

```
Chain 1: CourseID → InstructorID → InstructorName ✗ PROBLEM!
Chain 2: CourseID → InstructorID → InstructorOffice ✗ PROBLEM!
Chain 3: CourseID → InstructorID → InstructorPhone ✗ PROBLEM!
```

**Pattern:** InstructorID is the "bridge" that creates all three transitive dependencies.
</details>

---

### STEP 3: Check Non-Key Dependencies

**Your Turn (2 minutes):** Which non-key attributes depend on other non-key attributes?

<details>
<summary>Click to see non-key dependencies</summary>

```
InstructorName (non-key) depends on InstructorID (non-key) ✗ PROBLEM!
InstructorOffice (non-key) depends on InstructorID (non-key) ✗ PROBLEM!
InstructorPhone (non-key) depends on InstructorID (non-key) ✗ PROBLEM!

CourseName (non-key) depends on CourseID (key) ✓ OK
Credits (non-key) depends on CourseID (key) ✓ OK
```

**The rule:** Non-key attributes should depend ONLY on the primary key, not on other non-key attributes.
</details>

---

### STEP 4: Decompose into Separate Tables

**Solution:**

**COURSE Table (3NF):**

| CourseID | CourseName        | Credits | InstructorID |
|----------|-------------------|---------|--------------|
| CS101    | Intro Programming | 3       | I001         |
| MATH201  | Calculus I        | 4       | I002         |
| CS201    | Data Structures   | 4       | I001         |

**INSTRUCTOR Table (New - 3NF):**

| InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|--------------|----------------|------------------|-----------------|
| I001         | Dr. Johnson    | Room 101         | 555-1234        |
| I002         | Dr. Williams   | Room 205         | 555-5678        |

**Key Relationships:**
- COURSE.InstructorID is a foreign key referencing INSTRUCTOR.InstructorID
- Now Dr. Johnson's info appears ONCE (not twice!)

---

### Benefits of This Decomposition

✅ **Update Anomaly Fixed:** Change Dr. Johnson's office in ONE place
✅ **Insertion Anomaly Fixed:** Can add instructors without courses
✅ **Deletion Anomaly Fixed:** Deleting a course doesn't lose instructor data

---

## 🧪 Self-Check Quiz (3 minutes)

**Question:** Why did we put InstructorName, InstructorOffice, and InstructorPhone in the INSTRUCTOR table?

<details>
<summary>Click to reveal answer</summary>

**Answer:** Because all three of these fields describe the INSTRUCTOR, not the COURSE.

They depend on InstructorID, not on CourseID. By moving them to their own table with InstructorID as the primary key, we eliminate the transitive dependencies.

**The rule:** Group attributes that describe the same entity (thing) together in a table.
</details>

---

**✅ Section 3 Complete! Check it off in the roadmap.**

---

# Section 4: Guided Practice Problem #1
⏱️ **Estimated Time: 15 minutes**

Now it's your turn to apply the 4-step process! Work through this problem completely before checking the solution.

## Problem: Employee Department System

**Current Table:**

| EmpID | EmpName | DeptID | DeptName | DeptLocation | Salary |
|-------|---------|--------|----------|--------------|--------|
| E01   | Alice   | D10    | Sales    | Building A   | 50000  |
| E02   | Bob     | D10    | Sales    | Building A   | 55000  |
| E03   | Carol   | D20    | IT       | Building B   | 60000  |

Primary Key: EmpID

---

## Your Task

**Work through the 4-step process on your own (10 minutes):**

### STEP 1: List ALL Functional Dependencies

Write them down on paper in the format: `FieldA → FieldB`

<details>
<summary>Hint if you're stuck</summary>

Start with the primary key (EmpID) and think about what it determines. Then look for dependencies between non-key fields.
</details>

---

### STEP 2: Look for Dependency Chains

Find patterns like: `A → B → C`

<details>
<summary>Hint if you're stuck</summary>

Look at DeptID - does it serve as a "bridge" between other fields?
</details>

---

### STEP 3: Check Non-Key Dependencies

Which non-key attributes depend on other non-key attributes?

<details>
<summary>Hint if you're stuck</summary>

DeptName and DeptLocation - do they depend on EmpID or on something else?
</details>

---

### STEP 4: Decompose into 3NF Tables

Draw the new table structure on paper.

<details>
<summary>Hint if you're stuck</summary>

You should create TWO tables: one for employees and one for departments.
</details>

---

## Complete Solution

**Only look at this after you've attempted all 4 steps!**

<details>
<summary>Click to reveal complete solution</summary>

### STEP 1: All Functional Dependencies

```
EmpID → EmpName
EmpID → DeptID
EmpID → DeptName
EmpID → DeptLocation
EmpID → Salary
DeptID → DeptName
DeptID → DeptLocation
```

---

### STEP 2: Dependency Chains Found

```
Chain 1: EmpID → DeptID → DeptName ✗ TRANSITIVE!
Chain 2: EmpID → DeptID → DeptLocation ✗ TRANSITIVE!
```

**Explanation:** DeptName and DeptLocation depend on DeptID, which depends on EmpID. This creates an indirect (transitive) dependency.

---

### STEP 3: Non-Key Dependencies

```
DeptName (non-key) depends on DeptID (non-key) ✗ PROBLEM!
DeptLocation (non-key) depends on DeptID (non-key) ✗ PROBLEM!

EmpName (non-key) depends on EmpID (key) ✓ OK
Salary (non-key) depends on EmpID (key) ✓ OK
```

---

### STEP 4: 3NF Decomposition

**EMPLOYEE Table:**

| EmpID | EmpName | DeptID | Salary |
|-------|---------|--------|--------|
| E01   | Alice   | D10    | 50000  |
| E02   | Bob     | D10    | 55000  |
| E03   | Carol   | D20    | 60000  |

Primary Key: EmpID
Foreign Key: DeptID (references DEPARTMENT)

**DEPARTMENT Table:**

| DeptID | DeptName | DeptLocation |
|--------|----------|--------------|
| D10    | Sales    | Building A   |
| D20    | IT       | Building B   |

Primary Key: DeptID

---

### What We Fixed:

1. **Update Anomaly:** Change "Sales" to "Business Development" in ONE place (not two)
2. **Insertion Anomaly:** Can add new departments without hiring employees
3. **Deletion Anomaly:** Deleting all employees in a department doesn't lose department info

**Key Insight:** Notice "Sales" now appears only ONCE (was in 2 rows before). This is the hallmark of good normalization!

</details>

---

## Reflection Questions (3 minutes)

Answer these to solidify your understanding:

1. Why did we create two tables instead of one?
2. Which table would you update if the Sales department moves to Building C?
3. How does this design prevent data inconsistency?

<details>
<summary>Click to see answers</summary>

1. **Why two tables?** Because we have two distinct entities: EMPLOYEE (people) and DEPARTMENT (organizational units). Each should have its own table.

2. **Which table to update?** Only the DEPARTMENT table - change DeptLocation for DeptID D10. This updates ALL employees in Sales automatically (via the foreign key relationship).

3. **How it prevents inconsistency:** Since department information exists in only ONE place, you can't have situations where "Sales" is in Building A in one row and Building C in another row. Single point of truth = no inconsistency!
</details>

---

**✅ Section 4 Complete! Check it off in the roadmap.**

---

# Section 5: Guided Practice Problem #2
⏱️ **Estimated Time: 15 minutes**

Let's practice again with a more complex example. This time, try to work more independently.

## Problem: Product Supplier System

**Current Table:**

| ProductID | ProductName | SupplierID | SupplierName | SupplierCity | Price |
|-----------|-------------|------------|--------------|--------------|-------|
| P100      | Widget      | S01        | Acme Corp    | New York     | 10.50 |
| P101      | Gadget      | S01        | Acme Corp    | New York     | 15.00 |
| P102      | Doohickey   | S02        | Tech Supply  | Boston       | 8.75  |

Primary Key: ProductID

---

## Your Independent Work (12 minutes)

**Apply all 4 steps on your own. Write your work on paper before checking the solution.**

Some questions to guide you:
- What information describes the product?
- What information describes the supplier?
- If Acme Corp moves from New York to Chicago, how many rows need updating?
- Can you add a new supplier without adding a product?

---

## Complete Solution

**Only look after completing your work!**

<details>
<summary>Click to reveal complete solution</summary>

### STEP 1: All Functional Dependencies

```
ProductID → ProductName
ProductID → SupplierID
ProductID → SupplierName
ProductID → SupplierCity
ProductID → Price
SupplierID → SupplierName
SupplierID → SupplierCity
```

---

### STEP 2: Dependency Chains

```
Chain 1: ProductID → SupplierID → SupplierName ✗ TRANSITIVE!
Chain 2: ProductID → SupplierID → SupplierCity ✗ TRANSITIVE!
```

**The pattern:** SupplierName and SupplierCity tell us about the SUPPLIER, not the PRODUCT.

---

### STEP 3: Non-Key Dependencies

```
SupplierName (non-key) depends on SupplierID (non-key) ✗ PROBLEM!
SupplierCity (non-key) depends on SupplierID (non-key) ✗ PROBLEM!

ProductName (non-key) depends on ProductID (key) ✓ OK
Price (non-key) depends on ProductID (key) ✓ OK
```

---

### STEP 4: 3NF Decomposition

**PRODUCT Table:**

| ProductID | ProductName | SupplierID | Price |
|-----------|-------------|------------|-------|
| P100      | Widget      | S01        | 10.50 |
| P101      | Gadget      | S01        | 15.00 |
| P102      | Doohickey   | S02        | 8.75  |

Primary Key: ProductID
Foreign Key: SupplierID (references SUPPLIER)

**SUPPLIER Table:**

| SupplierID | SupplierName | SupplierCity |
|------------|--------------|--------------|
| S01        | Acme Corp    | New York     |
| S02        | Tech Supply  | Boston       |

Primary Key: SupplierID

---

### Key Observations:

1. **Acme Corp appears only ONCE** (was in 2 rows before)
2. **SupplierID links the tables** (foreign key relationship)
3. **Update Acme's city in ONE place** (SUPPLIER table)
4. **Can add suppliers without products** (no insertion anomaly)

</details>

---

## Self-Assessment (3 minutes)

**Rate your confidence:**

- ☐ I can identify transitive dependencies confidently
- ☐ I can apply the 4-step process independently
- ☐ I understand why we separate entities into different tables
- ☐ I'm ready to work on the assignment

**If you didn't check all boxes:**
- Review the sections that are unclear
- Work through the examples again
- Ask questions on the class forum

---

**✅ Section 5 Complete! Check it off in the roadmap.**

---

# Section 6: When to Stop - 3NF vs Higher Forms
⏱️ **Estimated Time: 10 minutes**

## You've Mastered the Industry Standard!

**Congratulations!** 3NF is the normalization level used in most professional databases.

---

## Why 3NF is Usually Enough

### Benefits of 3NF:

- ✅ Eliminates most common anomalies (update, insert, delete)
- ✅ Balances data integrity with query performance
- ✅ Easier to understand and maintain than higher forms
- ✅ Sufficient for 95% of real-world applications

---

## What About Higher Normal Forms?

**Beyond 3NF:**
- There are higher normal forms (4NF, 5NF, etc.)
- They handle very specialized situations
- Rarely needed in practice
- You'll learn about these in Class 3

---

## The Trade-Off: Complexity vs Integrity

### Example Query: Finding Students and Their Instructors

**Unnormalized (1 table):**
```sql
SELECT StudentName, InstructorName
FROM BigTable;
```

**3NF (4 tables):**
```sql
SELECT s.StudentName, i.InstructorName
FROM Student s
JOIN Enrollment e ON s.StudentID = e.StudentID
JOIN Course c ON e.CourseID = c.CourseID
JOIN Instructor i ON c.InstructorID = i.InstructorID;
```

---

### The Question: Is the Complexity Worth It?

**Unnormalized Approach:**
- ✅ Simpler query (1 table, no JOINs)
- ❌ Dr. Johnson's name might be misspelled in 50 different rows
- ❌ Changing office requires 50 updates
- ❌ Data inconsistency is almost guaranteed

**3NF Approach:**
- ✅ Dr. Johnson's info in ONE place - fix typo once
- ✅ Update office in ONE place
- ✅ Guaranteed consistency
- ❌ More complex query (3 JOINs)

---

## The Professional Perspective

💡 **Key Insight:** The extra query complexity is a small price to pay for data integrity.

**In the real world:**
- Queries are written once, run many times
- Data errors are expensive and embarrassing
- Fixing inconsistent data is time-consuming
- Modern databases handle JOINs efficiently

**The verdict:** 3NF is worth it for almost all applications!

---

## When to Stop at 3NF

**Stop at 3NF when:**
- ✅ No anomalies exist (test by trying to update, insert, delete)
- ✅ Queries are still manageable (3-4 JOINs is normal)
- ✅ Performance is acceptable
- ✅ The team understands the design

**Consider higher forms only when:**
- ❌ 3NF still shows anomalies in your specific domain
- ❌ You have overlapping candidate keys (rare!)
- ❌ Data integrity requirements are extreme

---

**✅ Section 6 Complete! Check it off in the roadmap.**

---

# 🎉 Tutorial Complete!

## What You've Accomplished

You've learned:

✅ How to identify transitive dependencies
✅ The 4-step process for achieving 3NF
✅ How to decompose tables to eliminate anomalies
✅ When 3NF is sufficient vs when higher forms are needed
✅ The trade-offs between normalization and query complexity

---

## Next Steps

1. **Take a 10-minute break** - you've earned it!
2. **Review any sections** where you struggled
3. **Practice with your own examples** - find tables that need normalization
4. **Ask questions** on the class forum if needed
5. **Prepare for Class 3** where we'll cover advanced normal forms and complete a hands-on assignment

---

## Key Takeaways

💡 **3NF eliminates transitive dependencies** - no non-key attribute should depend on another non-key attribute

💡 **Most real-world databases stop at 3NF** for practical reasons

💡 **Higher normalization trades query complexity for data integrity** - usually worth it!

💡 **The 4-step process is your friend** - use it systematically on every table

---

## Quick Reference Card

### How to Achieve 3NF:

**Step 1: Check if you're in 2NF**
- Table must have a primary key
- No partial dependencies (all attributes depend on the WHOLE key, not part of it)

**Step 2: Find transitive dependencies**
- Look for chains: Primary Key → Field A → Field B
- Ask: "Does this non-key field depend on another non-key field?"
- Pattern: "Information about information" (Field B describes Field A, not the primary key)

**Step 3: Decompose**
- Create a new table for the transitively dependent attributes
- Use the intermediate field as the new table's primary key
- Keep a foreign key in the original table

### Common Transitive Dependency Examples:

| Pattern | Problem | Solution |
|---------|---------|----------|
| `Employee → DeptID → DeptName` | Department info stored with every employee | Create DEPARTMENT table |
| `Order → CustomerID → CustomerCity` | Customer info repeated in every order | Create CUSTOMER table |
| `Product → CategoryID → CategoryName` | Category info duplicated across products | Create CATEGORY table |
| `Course → InstructorID → InstructorOffice` | Instructor info stored with every course | Create INSTRUCTOR table |

### Quick Test:
✅ **Your table is in 3NF if:**
- Every non-key field depends ONLY on the primary key
- No non-key field depends on another non-key field
- Changing one fact requires updating only ONE row

---

## Questions or Concerns?

- 📧 Email your instructor
- 💬 Post on the class discussion forum
- 👥 Form a study group with classmates
- 📅 Attend office hours

---

**Good luck with your assignment! You've got this!** 🚀

---

*This self-paced tutorial was adapted from the Class 2 lecture materials for independent learning.*
