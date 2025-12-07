# Database Normalization: Class 2 – Third Normal Form
## Mastering 3NF: The Industry Standard

### Class Overview (75 minutes)

**How to use this document:**
- **Before class:** Review 1NF/2NF concepts from Class 1, read through transitive dependencies section
- **During class:** Follow along, work through examples, note the decision-making process
- **After class:** Use checkpoints to verify understanding, complete practice problems
- **Time allocations:** These show both in-class pacing and suggested study time for each section

| Segment | Topic                                    | Time   |
|---------|------------------------------------------|--------|
| 1       | 2NF Retrieval Quiz & Review              | 8 min  |
| 2       | Third Normal Form (3NF) Introduction     | 20 min |
| 3       | In-Class Practice (2 examples)           | 20 min |
| 4       | Practice Review & Discussion             | 8 min  |
| 5       | Looking Ahead: Beyond 3NF                | 8 min  |
| 6       | Practical Considerations & Trade-offs    | 6 min  |
| 7       | Assignment Introduction & Exit Ticket    | 5 min  |

*Note: Class timing is approximate and will flex based on discussion and questions. Focus on mastering 3NF - that's the industry standard!*

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. **Identify** transitive dependencies in 2NF tables
2. **Decompose** tables to achieve 3NF by eliminating transitive dependencies
3. **Recognize** when 3NF is sufficient for most applications
5. **Evaluate** trade-offs between normalization levels and query complexity
6. **Decide** when to stop normalizing based on practical considerations

---

📖 **KEY TERMS FOR TODAY**
- **Transitive dependency**: When A → B and B → C, then A → C indirectly (this causes problems!)
- **Determinant**: The left side of a functional dependency (the part before the →)
- **Denormalize**: Intentionally add redundancy back for performance (we'll discuss when this makes sense)

---

## Quick Review: Where We've Been

### 1NF Solved:
- ✅ Non-atomic values (multiple items in one field)
- ✅ Repeating groups

### 2NF Solved:
- ✅ Partial dependencies (non-key attributes depending on part of composite key)

### Still Need to Solve:
- ❌ **Transitive dependencies** - indirect relationships through other attributes
- ❌ **Complex key relationships** - when 3NF isn't quite enough

---

✋ **CHECKPOINT #0: 2NF Retrieval Practice** (5 minutes)

Before we build on 2NF, let's verify you remember the key concepts from Class 1:

**Quick Quiz** (No grades - just checking understanding):

1. **Identify the composite key:**
   | OrderID | ProductID | ProductName | Quantity |
   |---------|-----------|-------------|----------|
   | 1001    | P50       | Laptop      | 2        |
   | 1001    | P51       | Mouse       | 1        |

   Answer: `{OrderID, ProductID}` - need both to identify each row uniquely

2. **Is this a partial dependency?**
   - Table key: `{OrderID, ProductID}`
   - Dependency: `ProductID → ProductName`

   Answer: YES - ProductName depends on only PART of the composite key (ProductID), not the whole key

3. **How many tables after 2NF decomposition?**
   Answer: 3 tables (ORDER, PRODUCT, ORDER_DETAIL)

**If you struggled with any of these, review Class 1 notes before continuing!**

---

## Third Normal Form (3NF)

### The Problem: Transitive Dependencies

Even after achieving 2NF, we can still have problems. Let's extend our course table:

**Course Table (2NF, but has problems):**

| CourseID | CourseName        | Credits | InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|----------|-------------------|---------|--------------|----------------|------------------|-----------------|
| CS101    | Intro Programming | 3       | I001         | Dr. Johnson    | Room 101         | 555-1234        |
| MATH201  | Calculus I        | 4       | I002         | Dr. Williams   | Room 205         | 555-5678        |
| CS201    | Data Structures   | 4       | I001         | Dr. Johnson    | Room 101         | 555-1234        |

### Transitive Dependency Chain:

**Visual Diagram:**
```
[CourseID] ──→ [InstructorID] ──→ [InstructorName]
   DIRECT          BRIDGE            ENDPOINT

This is INDIRECT because to get from CourseID to InstructorName,
you have to "hop through" InstructorID as a bridge.
```

**The dependency chain:**
```
CourseID → InstructorID          (Course determines which instructor)
InstructorID → InstructorName     (Instructor ID determines name)
InstructorID → InstructorOffice   (Instructor ID determines office)

Therefore: CourseID → InstructorName (indirectly, through InstructorID)
```

**The key insight:** InstructorName doesn't depend directly on CourseID - it depends on InstructorID, which depends on CourseID. This is a **transitive dependency** (going through an intermediate attribute).

**Pattern to recognize:** "Information about the information"
- CourseID tells you the InstructorID (information about the course)
- InstructorName tells you about the instructor, NOT about the course
- If you have "info about info" → likely a transitive dependency!

### Problems This Creates:

1. **Update Anomaly**: If Dr. Johnson moves to Room 102, we must update multiple course records
2. **Insertion Anomaly**: Can't add new instructor information without assigning them to a course
3. **Deletion Anomaly**: If CS201 is cancelled, we lose Dr. Johnson's office information

⚠️ **Sound familiar?** These are the same three anomalies from Class 1! Transitive dependencies cause the same problems that partial dependencies did.

---

### 3NF Requirements:

1. ✅ Table is in 2NF
2. ✅ No transitive dependencies exist
3. ✅ Every non-key attribute depends **directly** on the primary key (not through other attributes)

**Simple test:** Can you say "A depends on B, and B depends on the primary key"? If yes, you have a transitive dependency!

---

### 3NF Solution: Separate the Entities

**Course Table (3NF):**

| CourseID | CourseName        | Credits | InstructorID |
|----------|-------------------|---------|--------------|
| CS101    | Intro Programming | 3       | I001         |
| MATH201  | Calculus I        | 4       | I002         |
| CS201    | Data Structures   | 4       | I001         |

**Instructor Table (New):**

| InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|--------------|----------------|------------------|-----------------|
| I001         | Dr. Johnson    | Room 101         | 555-1234        |
| I002         | Dr. Williams   | Room 205         | 555-5678        |

### Benefits:

✅ **Update once**: Change Dr. Johnson's office in one place
✅ **Add instructors**: Can add instructor info without courses
✅ **Delete safely**: Removing a course doesn't lose instructor data

---

### Complete 3NF Schema:

**Visual Concept: Four Clean Tables Working Together**

```
    [STUDENT] ----→ [ENROLLMENT] ←---- [COURSE] ----→ [INSTRUCTOR]
   Student info    Bridge table      Course info     Instructor info
```

**Student Table:**

| StudentID | StudentName | StudentEmail   |
|-----------|-------------|----------------|
| 101       | John Smith  | john@email.com |
| 102       | Jane Doe    | jane@email.com |

**Instructor Table:**

| InstructorID | InstructorName | InstructorOffice | InstructorPhone |
|--------------|----------------|------------------|-----------------|
| I001         | Dr. Johnson    | Room 101         | 555-1234        |
| I002         | Dr. Williams   | Room 205         | 555-5678        |

**Course Table:**

| CourseID | CourseName        | Credits | InstructorID |
|----------|-------------------|---------|--------------|
| CS101    | Intro Programming | 3       | I001         |
| MATH201  | Calculus I        | 4       | I002         |

**Enrollment Table:**

| StudentID | CourseID | Grade |
|-----------|----------|-------|
| 101       | CS101    | A     |
| 101       | MATH201  | B     |
| 102       | CS101    | A     |

**Key Relationships:**
- Course.InstructorID → Instructor.InstructorID (Foreign Key)
- Enrollment.StudentID → Student.StudentID (Foreign Key)
- Enrollment.CourseID → Course.CourseID (Foreign Key)

---

### How to Identify Transitive Dependencies

**Follow these steps for every table:**

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

STEP 4: Verify the Problem
├─ Ask: "If I change the intermediate value, do I have to update multiple rows?"
└─ If YES → this transitive dependency is causing anomalies
```

**When You're Stuck:**
- 🔍 Can't find chains? Look for attributes that describe OTHER attributes (not the primary key)
- 🔍 Not sure if it's transitive? Ask: "Does this field tell me about the key, or about another field?"
- 🔍 Confused about what's wrong? Remember: Every non-key field should depend ONLY on the primary key

---

### Worked Example: Course Table Analysis

Let's apply the 4-step process to our Course table (Primary Key = CourseID):

**STEP 1: List ALL Functional Dependencies**

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

**STEP 2: Look for Dependency Chains**

```
Chain 1: CourseID → InstructorID → InstructorName ✗ FOUND ONE!
Chain 2: CourseID → InstructorID → InstructorOffice ✗ FOUND ANOTHER!
Chain 3: CourseID → InstructorID → InstructorPhone ✗ AND ANOTHER!
```

**STEP 3: Check Non-Key Dependencies**

```
InstructorName (non-key) depends on InstructorID (non-key) ✗ PROBLEM!
InstructorOffice (non-key) depends on InstructorID (non-key) ✗ PROBLEM!
InstructorPhone (non-key) depends on InstructorID (non-key) ✗ PROBLEM!

CourseName (non-key) depends on CourseID (key) ✓ OK
Credits (non-key) depends on CourseID (key) ✓ OK
```

**STEP 4: Verify the Problem**

If Dr. Johnson (I001) moves to Room 102:
- Must update CS101 row
- Must update CS201 row
- Two updates for one fact = UPDATE ANOMALY ✗

**Conclusion:** We have transitive dependencies that need fixing with 3NF!

**Original Dependencies:**
- `CourseID → CourseName` ✓ (Direct dependency - OK)
- `CourseID → Credits` ✓ (Direct dependency - OK)
- `CourseID → InstructorID` ✓ (Direct dependency - OK)
- `CourseID → InstructorName` ✗ (Transitive through InstructorID)
- `CourseID → InstructorOffice` ✗ (Transitive through InstructorID)
- `CourseID → InstructorPhone` ✗ (Transitive through InstructorID)

**Solution:** Move transitively dependent attributes (InstructorName, InstructorOffice, InstructorPhone) to a separate INSTRUCTOR table.

---

✋ **CHECKPOINT #1: Check Your Understanding**

Consider this table:

| OrderID | ProductID | ProductName | CategoryID | CategoryName |
|---------|-----------|-------------|------------|--------------|
| 1001    | P50       | Laptop      | C10        | Electronics  |
| 1002    | P51       | Mouse       | C10        | Electronics  |

**Use the 4-step process to analyze this table (Primary Key = OrderID):**

**STEP 1: List all functional dependencies**

```
OrderID → ProductID
OrderID → ProductName
OrderID → CategoryID
OrderID → CategoryName
ProductID → ProductName
ProductID → CategoryID
CategoryID → CategoryName
```

**STEP 2: Look for dependency chains**

```
Chain 1: OrderID → ProductID → ProductName ✗ Found!
Chain 2: OrderID → ProductID → CategoryID ✗ Found!
Chain 3: OrderID → CategoryID → CategoryName ✗ Found!
```

**STEP 3: Check non-key dependencies**

```
ProductName (non-key) depends on ProductID (non-key) ✗
CategoryID (non-key) depends on ProductID (non-key) ✗
CategoryName (non-key) depends on CategoryID (non-key) ✗
```

**STEP 4: Verify the problem**

If "Electronics" category name changes to "Electronic Devices":
- Must update every order with CategoryID C10
- Multiple updates = UPDATE ANOMALY ✗

**Questions:**
1. Is this table in 2NF? (Assume OrderID is the primary key)
2. Identify the transitive dependency chains
3. How many tables would you create for 3NF?

**Answers:**
1. Yes, it's in 2NF (single-field primary key, so no partial dependencies possible)
2. Three chains:
   - `OrderID → ProductID → ProductName`
   - `OrderID → ProductID → CategoryID`
   - `OrderID → CategoryID → CategoryName`
3. Four tables: ORDER (OrderID, ProductID), PRODUCT (ProductID, ProductName, CategoryID), CATEGORY (CategoryID, CategoryName), and possibly ORDER_DETAIL if needed

*Take 3 minutes to work through this with a partner before checking the answers.*

---

## 🧩 In-Class Practice: Applying 3NF

### How to Approach These Problems

**Follow the same 4-step process:**
1. List ALL functional dependencies
2. Look for dependency chains (A → B → C)
3. Check if non-key attributes depend on other non-key attributes
4. Decompose: Create separate tables to eliminate transitive dependencies

---

### Example 1: Employee Department System

**Instructions**: Work in pairs (8 minutes)

**Current Table:**

| EmpID | EmpName | DeptID | DeptName | DeptLocation | Salary |
|-------|---------|--------|----------|--------------|--------|
| E01   | Alice   | D10    | Sales    | Building A   | 50000  |
| E02   | Bob     | D10    | Sales    | Building A   | 55000  |
| E03   | Carol   | D20    | IT       | Building B   | 60000  |

Primary Key: EmpID

**Tasks:**
1. List all functional dependencies
2. Identify transitive dependency chains
3. Decompose into 3NF tables
4. Show primary/foreign keys

**Guided Help:**
- **Finding chains:** Does DeptName depend on EmpID directly, or through DeptID?
- **Pattern:** DeptName and DeptLocation describe the DEPARTMENT, not the EMPLOYEE
- **Expected tables:** 2 tables (EMPLOYEE, DEPARTMENT)

---

### Example 2: Product Supplier System

**Instructions**: Work in pairs (8 minutes)

**Current Table:**

| ProductID | ProductName | SupplierID | SupplierName | SupplierCity | Price |
|-----------|-------------|------------|--------------|--------------|-------|
| P100      | Widget      | S01        | Acme Corp    | New York     | 10.50 |
| P101      | Gadget      | S01        | Acme Corp    | New York     | 15.00 |
| P102      | Doohickey   | S02        | Tech Supply  | Boston       | 8.75  |

Primary Key: ProductID

**Tasks:**
1. Apply the 4-step process
2. Identify ALL transitive dependencies
3. Create 3NF decomposition
4. Explain what anomalies are prevented

**Guided Help:**
- **Step 1:** Write down dependencies - don't forget SupplierID → SupplierName and SupplierID → SupplierCity
- **Step 2:** Look for chains through SupplierID
- **Step 3:** SupplierName and SupplierCity tell you about the SUPPLIER, not the PRODUCT
- **Expected tables:** 2 tables (PRODUCT, SUPPLIER)

---

### Practice Review & Discussion (5 minutes)

**Example 1 Solution:**

**EMPLOYEE Table:**

| EmpID | EmpName | DeptID | Salary |
|-------|---------|--------|--------|
| E01   | Alice   | D10    | 50000  |
| E02   | Bob     | D10    | 55000  |
| E03   | Carol   | D20    | 60000  |

**DEPARTMENT Table:**

| DeptID | DeptName | DeptLocation |
|--------|----------|--------------|
| D10    | Sales    | Building A   |
| D20    | IT       | Building B   |

**Transitive dependencies eliminated:**
- EmpID → DeptID → DeptName ✓ Fixed
- EmpID → DeptID → DeptLocation ✓ Fixed

**Anomalies prevented:**
- Update: Change "Sales" name in ONE place (not two)
- Insert: Can add departments without employees
- Delete: Removing employees doesn't lose department info

---

**Example 2 Solution:**

**PRODUCT Table:**

| ProductID | ProductName | SupplierID | Price |
|-----------|-------------|------------|-------|
| P100      | Widget      | S01        | 10.50 |
| P101      | Gadget      | S01        | 15.00 |
| P102      | Doohickey   | S02        | 8.75  |

**SUPPLIER Table:**

| SupplierID | SupplierName | SupplierCity |
|------------|--------------|--------------|
| S01        | Acme Corp    | New York     |
| S02        | Tech Supply  | Boston       |

**Key insight:** Notice Acme Corp appears only ONCE now (was in 2 rows before)

---

## Looking Ahead: Beyond 3NF

### You've Mastered the Industry Standard!

**Congratulations!** With 3NF, you now know the normalization level used in most professional databases.

**What about higher normal forms?**

There are advanced normal forms beyond 3NF:
- **4NF**: Eliminates multi-valued dependencies
- **5NF**: Handles complex join dependencies
- These handle rare edge cases in specialized situations

**Good news:** We'll explore these in detail in **Class 3**!

**For now:** Focus on mastering 3NF - it's what you'll use 95% of the time in real applications.

---

✋ **CHECKPOINT #2: Check Your Understanding**

**Question:** Why is 3NF considered the "industry standard"?

**Answer:**
- ✅ Eliminates most common anomalies (update, insert, delete)
- ✅ Balances data integrity with query performance
- ✅ Easier to understand and maintain than higher forms
- ✅ Sufficient for the vast majority of real-world applications
- ✅ Higher normal forms (4NF, 5NF) are rarely needed in practice

**Takeaway:** If you can normalize to 3NF confidently, you have a valuable professional skill!

---

## Practical Considerations

### When to Stop Normalizing:

#### 3NF is Usually Enough:

- ✅ Eliminates most common anomalies
- ✅ Balances data integrity with query performance
- ✅ Easier to understand and maintain
- ✅ Industry standard for most applications

#### When to Consider Higher Forms (4NF, 5NF):

- You have rare edge cases that 3NF doesn't handle (we'll learn to recognize these in Class 3)
- 3NF still shows anomalies in your specific domain
- Data integrity is more important than query complexity
- The specific constraints of your domain require it

---

### Real-World Trade-offs:

**Benefits of Higher Normalization:**

- ✅ Better data integrity
- ✅ Reduced redundancy
- ✅ Easier to maintain consistency
- ✅ Prevents update/insert/delete anomalies

**Costs of Higher Normalization:**

- ❌ More complex queries (more JOINs)
- ❌ Potentially slower performance
- ❌ More complex application logic
- ❌ Harder for non-technical users to understand

---

### Example Query Complexity:

**Task:** Finding all students and their instructor names

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

**The Trade-off:** More JOINs but much better data integrity.

💡 **Key Insight:** The unnormalized query is simpler, but if Dr. Johnson's name is misspelled in 50 different rows, you have 50 problems. In 3NF, you fix it once.

---

## Class 2 Assignment: Advanced Normalization

### Objective

Apply 3NF concepts to eliminate transitive dependencies.

### Instructions

**Part 1: Review and Extend (20 points)**

**Step-by-step instructions:**
1. Open your `LastName_FirstName_Normalization1.xlsx` from Class 1
2. Download `Class2_ExtendedData.xlsx` from Canvas
3. Copy the instructor and department data into a new tab called "Extended Data"
4. Use the 4-step process (from lines 223-242) to identify transitive dependencies
5. Create a new tab called "Transitive Dependencies Found"
6. List all transitive dependency chains in this format:
   - `Table: COURSE`
   - `Chain: CourseID → InstructorID → InstructorName`

**Part 2: 3NF Normalization (60 points)** ← *Main focus of assignment*

**Step-by-step instructions:**
1. For each transitive dependency you found, create a new table
2. Follow the pattern from in-class examples (Employee/Department, Product/Supplier)
3. In a new tab called "3NF Tables", show:
   - All tables in 3NF format
   - Primary keys marked clearly (highlight or [PK] notation)
   - Foreign keys marked clearly (different color or [FK] notation)
4. In a new tab called "3NF Analysis", document:
   - What transitive dependencies were eliminated
   - What anomalies are now prevented (update, insert, delete)

**Grading criteria:**
- All transitive dependencies identified and eliminated (40 pts)
- Correct primary/foreign key relationships (15 pts)
- Clear documentation of improvements (5 pts)

**Part 3: Extended Analysis (10 points)**

**Document your normalization decisions:**

1. For each transitive dependency you eliminated, explain:
   - What was the problem?
   - How does your 3NF solution fix it?
2. List at least 3 specific anomalies your design prevents
3. Draw a simple diagram showing how your tables connect (can be hand-drawn and scanned)

**Part 4: Reflection on Trade-offs (10 points)**

Answer these questions in a new tab called "Reflection":
1. How many tables did you start with? How many do you have now in 3NF?
2. If you had to find all students and their instructors:
   - How many tables would you need to connect (JOIN)?
   - Is this more complex than the original design?
3. In your own words: Why is the extra complexity worth it?
4. Give ONE example from your design where 3NF prevents an anomaly

### Submission Format

Excel file with tabs:

- **Tab 1:** Extended Data (from Class2_ExtendedData.xlsx)
- **Tab 2:** Transitive Dependencies Found (list of chains)
- **Tab 3:** 3NF Tables (your decomposed tables)
- **Tab 4:** 3NF Analysis (what you fixed and why)
- **Tab 5:** Extended Analysis (decisions and diagram)
- **Tab 6:** Reflection (trade-off questions)

**File name:** `LastName_FirstName_Normalization2.xlsx`
**Due:** Next class

---

### Assessment Rubric

| Criteria                      | Points | Excellent (90-100%)                     | Good (80-89%)                         | Needs Work (<80%)                |
|-------------------------------|--------|-----------------------------------------|---------------------------------------|-----------------------------------|
| Transitive Dependency ID      | 20     | Found all 5+ transitive dependencies   | Found 3-4 dependencies                | Found fewer than 3                |
| 3NF Decomposition             | 40     | Perfect table structure, all keys correct| Minor issues with 1-2 relationships | Incorrect structure or missing tables |
| Primary/Foreign Key Notation  | 15     | All keys clearly marked and correct     | Most keys correct, minor notation issues | Many keys missing or incorrect  |
| Extended Analysis             | 10     | Clear decisions, good diagram, anomalies listed | Good analysis with minor gaps | Poor or missing analysis |
| Documentation & Analysis      | 5      | Clear explanation of all improvements   | Good explanation with minor gaps      | Poor or missing analysis          |
| Reflection on Trade-offs      | 10     | Thoughtful answers showing understanding| Adequate answers with minor issues    | Superficial or missing responses  |

---

### Extended Dataset

`Class2_ExtendedData.xlsx` includes:

- Original student/course data from Class 1
- Instructor information with departments
- Department information with locations
- Additional complexity for transitive dependencies

---

### Tips for Success

- 📊 **Draw dependency diagrams** - Visual representations help identify chains
- 🔍 **Check every non-key attribute** - Does it depend directly on the primary key?
- 💡 **Look for "information about information"** - Often signals transitive dependencies
- ✅ **Test your design** - Can you add/update/delete without anomalies?

---

## Next Class Preview

Class 3 will cover advanced normal forms (BCNF, 4NF, 5NF) and modern database considerations including NoSQL, performance optimization, and when to denormalize.

---

## ✋ EXIT TICKET (Required - Turn in Before Leaving)

**Answer these 3 questions on an index card or paper:**

1. **Confidence Check:** On a scale of 1-5, how confident are you identifying transitive dependencies?
   - 1 = Very confused
   - 3 = Getting it but need more practice
   - 5 = Very confident

2. **Quick Application:** In this table with Primary Key = StudentID:
   ```
   StudentID → AdvisorID → AdvisorOffice
   ```
   Is AdvisorOffice directly or transitively dependent on StudentID? ____________________

3. **Reflection:** What's ONE thing that's still confusing about 3NF or normalization in general? (Or write "Nothing - I'm good!" if you feel confident)

*Your instructor will review these before next class to address common confusion points.*

---

## Key Takeaways

- **3NF eliminates transitive dependencies** - no non-key attribute should depend on another non-key attribute
- **Most real-world databases stop at 3NF** for practical reasons
- **Higher normalization trades query complexity for data integrity**
- **Always consider your specific use case** when choosing normal form level
- **3NF is the industry standard** - sufficient for 95% of applications

---

## Quick Reference: 3NF Checklist

### Requirements for 3NF:

- ✓ Already in 2NF
- ✓ No transitive dependencies
- ✓ All non-key attributes directly depend on primary key
- ✓ No non-key attribute depends on another non-key attribute

---

## Common 3NF Violations to Watch For:

Look for these patterns - they often indicate transitive dependencies:

- `Employee → Department → DepartmentLocation`
- `Order → Customer → CustomerCreditRating`
- `Product → Category → CategoryDescription`
- `Course → Instructor → InstructorOffice`

**Pattern to recognize:** "Information about the information"
- If you have InstructorID, and then InstructorOffice tells you about the instructor (not the course), that's transitive!

---

**Remember:** The goal is to eliminate anomalies while maintaining practical usability!
