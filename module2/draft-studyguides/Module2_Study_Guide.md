# CSCI 101: Module 2 Study Guide
## Database Design, ERD, Normalization, and Relationships

---

## 📚 How to Use This Study Guide

This guide is designed to help you prepare efficiently for the Module 2 exam based on how much time you have available.

### Study Plan Options:

- **🚨 Last-Minute (3 Hours Before Exam):** Focus on the "3-Hour Crash Course" section
- **⏰ Prepared (48 Hours Before Exam):** Follow the "48-Hour Study Plan" for deeper understanding
- **💪 Well-Prepared (1 Week Before):** Complete all sections including practice problems

**Important:** This guide reviews concepts - it does NOT give away exam questions. Use your class notes, textbook, and assignments alongside this guide.

---

## 🚨 3-HOUR CRASH COURSE (Last-Minute Review)

*If you only have 3 hours before the exam, follow this streamlined review.*

### Hour 1: Core Concepts Review (60 minutes)

#### ⏱️ Minutes 1-15: ERD & Relationship Fundamentals

**Entity Relationship Diagrams (ERDs):**
- **Rectangle** = Entity (like STUDENT, COURSE)
- **Oval** = Attribute (like StudentName, CourseID)
- **Diamond** = Relationship (connects entities)
- **Lines** = Show connections between entities

**Crow's Feet Notation - THE MOST IMPORTANT SYMBOLS:**

Learn these four patterns:

1. **Mandatory One (|—):**
   - Perpendicular line + single line
   - Means: "exactly one, required"
   - Example: Every order MUST have exactly one customer

2. **Optional One (o—):**
   - Circle + single line
   - Means: "zero or one"
   - Example: A person MAY have zero or one driver's license

3. **Mandatory Many (|≺):**
   - Perpendicular line + crow's foot
   - Means: "one or more, required"
   - Example: A department MUST have at least one employee

4. **Optional Many (o≺):**
   - Circle + crow's foot
   - Means: "zero or more"
   - Example: A customer MAY have zero or more orders

**Quick Memory Trick:**
- **Circle (o)** = "Optional" (starts with O)
- **Perpendicular line (|)** = "Mandatory" (stands firm like a wall)
- **Single line** = "One"
- **Crow's foot (≺)** = "Many" (three toes = many)

**Relationship Types:**
- **One-to-One (1:1):** One person has one passport
- **One-to-Many (1:M):** One customer has many orders
- **Many-to-Many (M:N):** Many students take many courses

**Key Rule:** Many-to-many relationships REQUIRE a bridge table (also called junction table or associative entity)

---

#### ⏱️ Minutes 16-30: Primary Keys & Foreign Keys

**Primary Key (PK):**
- Uniquely identifies each row in a table
- Cannot be NULL
- Can be single column (StudentID) or composite (OrderID + ProductID)
- Example: StudentID in STUDENT table

**Foreign Key (FK):**
- Column in one table that points to a primary key in another table
- Creates the relationship between tables
- CAN be NULL (if relationship is optional)
- Example: StudentID in ENROLLMENT table (points to STUDENT table)

**Composite Key:**
- Primary key made of 2+ columns working together
- Example: {StudentID, CourseID} in ENROLLMENT table
- Need BOTH values to uniquely identify a row

**Quick Test:** Can you tell them apart?
- STUDENT(StudentID, Name, Email) ← StudentID is PK
- ENROLLMENT(StudentID, CourseID, Grade) ← {StudentID, CourseID} is composite PK, each is also FK

---

#### ⏱️ Minutes 31-45: Functional Dependencies

**What is a Functional Dependency?**
- Notation: `X → Y` means "if you know X, you can determine Y"
- Read as: "X determines Y" or "Y depends on X"

**Examples:**
- `StudentID → StudentName` (know ID, can find name)
- `ISBN → BookTitle` (know ISBN, can find book title)
- `{StudentID, CourseID} → Grade` (need both to find grade)

**Three Types to Know:**

1. **Full Dependency:**
   - Attribute depends on the ENTIRE primary key
   - `{OrderID, ProductID} → Quantity` ✓ Good!

2. **Partial Dependency:**
   - Attribute depends on only PART of a composite key
   - `{OrderID, ProductID} → ProductName` ✗ Problem! (ProductName only needs ProductID)
   - **This violates 2NF**

3. **Transitive Dependency:**
   - A → B and B → C, so A → C indirectly
   - `EmpID → DeptID → DeptName` ✗ Problem!
   - **This violates 3NF**

**Key Terms:**
- **Determinant** = left side of arrow (X in X → Y)
- **Dependent** = right side of arrow (Y in X → Y)

---

#### ⏱️ Minutes 46-60: Database Anomalies

**Three Anomalies Normalization Prevents:**

1. **Update Anomaly:**
   - Same data appears in multiple rows
   - Changing it requires updating many places
   - Risk: Miss some rows, database becomes inconsistent
   - Example: Customer address repeated in every order row

2. **Insertion Anomaly:**
   - Can't add data without adding other unrelated data
   - Example: Can't add a new department without first hiring an employee

3. **Deletion Anomaly:**
   - Deleting one piece of data loses other important data
   - Example: Delete last employee in a department, lose all department info

**Memory Trick:**
- **UID** = Update, Insertion, Deletion (the three anomalies)

---

### Hour 2: Normal Forms Mastery (60 minutes)

#### ⏱️ Minutes 1-20: First Normal Form (1NF)

**Rule:** Every cell must contain a single atomic value (no lists, no repeating groups)

**Two Violations to Recognize:**

**Violation #1: Non-Atomic Values**
```
❌ BAD:
PhoneNumber: "555-1234, 555-5678"  (multiple values in one cell)

✓ GOOD:
Row 1: PhoneNumber: "555-1234"
Row 2: PhoneNumber: "555-5678"
```

**Violation #2: Repeating Groups**
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

---

#### ⏱️ Minutes 21-40: Second Normal Form (2NF)

**Rule:** Must be in 1NF AND have no partial dependencies

**What's a Partial Dependency?**
- Non-key attribute depends on only PART of a composite primary key
- Only applies to tables with composite keys!

**Example Problem:**
```
ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName)
Primary Key: {OrderID, ProductID}

Problem: ProductName → ProductID (only part of the key!)
```

**How to Fix:**
1. Identify what depends on only part of the composite key
2. Move those attributes to a new table
3. Use the partial key as the new table's primary key

**Solution:**
```
ORDER_DETAIL(OrderID, ProductID, Quantity)
  PK: {OrderID, ProductID}

PRODUCT(ProductID, ProductName)
  PK: ProductID
```

**Quick Check:**
- Does the table have a composite key? If NO, skip to 3NF (no partial dependencies possible)
- If YES, does every non-key attribute depend on the ENTIRE key? If YES, you're in 2NF!

---

#### ⏱️ Minutes 41-60: Third Normal Form (3NF)

**Rule:** Must be in 2NF AND have no transitive dependencies

**What's a Transitive Dependency?**
- A → B and B → C, so A → C indirectly
- Non-key attribute depends on another non-key attribute

**Example Problem:**
```
EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)
Primary Key: EmpID

Problem: EmpID → DeptID → DeptName, DeptLocation
(Department info depends on DeptID, not directly on EmpID)
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

---

### Hour 3: Practice & Memorization (60 minutes)

#### ⏱️ Minutes 1-20: Bridge Tables (Junction Tables)

**When Do You Need a Bridge Table?**
- **ONLY for Many-to-Many (M:N) relationships**
- Examples: Students ↔ Courses, Actors ↔ Movies, Authors ↔ Books

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

---

#### ⏱️ Minutes 21-40: Denormalization (When to Break the Rules)

**What is Denormalization?**
- Intentionally adding redundancy back into a normalized database
- Trade-off: Better performance for worse data integrity

**When to Denormalize:**

1. **Read-Heavy Reporting:**
   - Reports that join 5+ tables and run too slowly
   - Data warehouses and business intelligence
   - Example: Store customer name in order table to avoid joining

2. **Performance-Critical Queries:**
   - High-traffic queries that cause bottlenecks
   - E-commerce product pages viewed millions of times
   - Example: Cache category name in product table

3. **Calculated Fields:**
   - Pre-calculate expensive aggregations
   - Example: Store total in ORDER table instead of summing ORDER_DETAIL

4. **Historical Snapshots:**
   - Preserve data as it was at a point in time
   - Example: Store customer address in order (even if customer moves later)

**Important:** Always normalize FIRST, then denormalize strategically based on real performance data!

---

#### ⏱️ Minutes 41-60: Cardinality Quick Reference

**Cardinality** = The number of entity instances that can participate in a relationship

**Reading Crow's Feet Notation:**

Always read from one entity toward another:

```
CUSTOMER ——|—————o≺—— ORDER

Read left to right: "One customer has zero or many orders"
Read right to left: "One order belongs to exactly one customer"
```

**Common Patterns:**

1. **One-to-Many (Most Common):**
   ```
   CUSTOMER ——|—————o≺—— ORDER
   One customer → Many orders
   ```

2. **Many-to-Many (Needs Bridge Table):**
   ```
   STUDENT ——o≺—— ENROLLMENT ——≺o—— COURSE
   Many students ↔ Many courses (through ENROLLMENT)
   ```

3. **One-to-One (Rare):**
   ```
   PERSON ——|—————|—— PASSPORT
   One person → One passport
   ```

**Mandatory vs. Optional:**
- **Mandatory (|):** Must exist (every order MUST have a customer)
- **Optional (o):** May or may not exist (customer MAY have orders)

---

## ⏰ 48-HOUR STUDY PLAN (Comprehensive Preparation)

*If you have 48 hours (2 days) before the exam, use this detailed study plan.*

---

### Day 1, Morning Session (2 hours): ERD & Relationships

#### Hour 1: Entity Relationship Diagrams Deep Dive

**What You're Modeling:**
- **Entities:** Things in the real world (nouns)
  - Examples: STUDENT, COURSE, INSTRUCTOR, DEPARTMENT
  - Represented as rectangles in ERDs

- **Attributes:** Properties of entities (descriptive information)
  - Examples: StudentName, CourseTitle, InstructorEmail
  - Represented as ovals in ERDs
  - Connected to their entity with lines

- **Relationships:** How entities connect (verbs)
  - Examples: "enrolls in," "teaches," "belongs to"
  - Represented as diamonds or labeled lines

**Types of Attributes:**

1. **Simple Attributes:**
   - Single, atomic value
   - Example: Age, Email, Price

2. **Composite Attributes:**
   - Can be broken into sub-parts
   - Example: Address = (Street, City, State, Zip)
   - Example: FullName = (FirstName, MiddleName, LastName)

3. **Derived Attributes:**
   - Calculated from other attributes
   - Example: Age derived from DateOfBirth
   - Example: OrderTotal derived from sum of line items
   - Usually shown with dashed oval

4. **Multivalued Attributes:**
   - Can have multiple values
   - Example: PhoneNumbers (person may have multiple)
   - Usually shown with double oval
   - **Note:** These should be normalized into separate tables!

**Identifying Entities vs. Attributes:**

Ask yourself: "Can this thing have its own attributes?"

- **Entity:** Can have multiple attributes
  - INSTRUCTOR (has name, email, office, phone)

- **Attribute:** Single piece of data
  - InstructorName (just one piece of info)

**Common Mistakes:**
- Making everything an entity (leads to too many tables)
- Making complex things attributes (loses important details)

**Practice Exercise:**

Model a library system. Which are entities? Which are attributes?
- Book (Entity - has ISBN, title, author, publication date)
- ISBN (Attribute of Book)
- Author (Could be entity if tracking multiple books per author)
- PatronName (Attribute of Patron entity)
- CheckoutDate (Attribute of Checkout relationship)

---

#### Hour 2: Cardinality & Crow's Feet Notation Mastery

**Understanding Cardinality:**

Cardinality answers: "How many of Entity A can relate to how many of Entity B?"

**The Three Main Types:**

1. **One-to-One (1:1):**
   - Relatively rare
   - One instance of A relates to exactly one instance of B
   - Examples:
     - PERSON ↔ PASSPORT (one person, one passport)
     - EMPLOYEE ↔ DESK (one employee, one assigned desk)
     - COUNTRY ↔ CAPITAL_CITY (one country, one capital)

   **Implementation:** Put FK in either table (usually in the table accessed more often)

2. **One-to-Many (1:M):**
   - Most common relationship type
   - One instance of A relates to many instances of B
   - Examples:
     - CUSTOMER ↔ ORDER (one customer, many orders)
     - DEPARTMENT ↔ EMPLOYEE (one department, many employees)
     - BLOG_POST ↔ COMMENT (one post, many comments)

   **Implementation:** Put FK in the "many" side table
   ```
   CUSTOMER(CustomerID, Name)
   ORDER(OrderID, CustomerID, OrderDate)
            ↑ FK to CUSTOMER
   ```

3. **Many-to-Many (M:N):**
   - Cannot be directly implemented in relational databases
   - Requires a bridge table to decompose into two 1:M relationships
   - Examples:
     - STUDENT ↔ COURSE (students take many courses, courses have many students)
     - ACTOR ↔ MOVIE (actors in many movies, movies have many actors)
     - PRODUCT ↔ SUPPLIER (products from many suppliers, suppliers provide many products)

   **Implementation:** Create bridge table
   ```
   STUDENT(StudentID, Name)
   COURSE(CourseID, Title)
   ENROLLMENT(StudentID, CourseID, Grade)
     PK: {StudentID, CourseID}
     FKs: StudentID → STUDENT, CourseID → COURSE
   ```

**Crow's Feet Notation - Detailed Breakdown:**

Each relationship end has TWO indicators:

**Component 1 - Mandatory vs. Optional:**
- **Perpendicular line (|):** Mandatory (at least one required)
- **Circle (o):** Optional (zero allowed)

**Component 2 - One vs. Many:**
- **Single line (—):** One (exactly one or at most one)
- **Crow's foot (≺):** Many (one or more, or zero or more)

**Four Common Combinations:**

1. **|—** (Mandatory One): Exactly one, required
   - Example: ORDER → CUSTOMER (every order must have exactly one customer)

2. **o—** (Optional One): Zero or one
   - Example: EMPLOYEE → COMPANY_CAR (employee may have 0 or 1 company car)

3. **|≺** (Mandatory Many): One or more, required
   - Example: DEPARTMENT → EMPLOYEE (department must have at least one employee)

4. **o≺** (Optional Many): Zero or more
   - Example: CUSTOMER → ORDER (customer may have 0, 1, or many orders)

**How to Read Relationship Lines:**

Always read from one entity TOWARD the other entity's notation:

```
CUSTOMER ——|—————o≺—— ORDER

Left to right:
- Start at CUSTOMER
- Look at ORDER end: o≺ = zero or many
- Read: "One customer has zero or many orders"

Right to left:
- Start at ORDER
- Look at CUSTOMER end: |— = exactly one
- Read: "One order belongs to exactly one customer"
```

**Practice: Determine the Cardinality**

For each scenario, identify the relationship type:

1. A person has one Social Security Number (**1:1**)
2. A professor teaches many courses (**1:M**)
3. Students enroll in many courses, courses have many students (**M:N**)
4. A book has one primary author (**1:M** - one author, many books)
5. An order contains many products, products appear in many orders (**M:N**)

**Common Confusion:**

"Which end is which?"
- Think about the REAL WORLD logic first
- One CUSTOMER can place many ORDERS
- Each ORDER belongs to one CUSTOMER
- This is 1:M (Customer is "one" side, Order is "many" side)

---

### Day 1, Afternoon Session (2 hours): Keys & Dependencies

#### Hour 1: Keys in Depth

**Primary Keys (PK) - Deep Understanding**

**Purpose:**
- Uniquely identifies each row in a table
- Ensures no duplicate records
- Serves as the main reference point for relationships

**Characteristics:**
1. **Unique:** No two rows can have the same PK value
2. **Not NULL:** Every row must have a PK value
3. **Unchanging:** PK values should rarely/never change
4. **Minimal:** Use fewest columns necessary

**Types of Primary Keys:**

1. **Natural Key:**
   - Based on real-world data
   - Examples: ISBN, SSN, VIN, Email
   - **Pros:** Meaningful, already exists in data
   - **Cons:** May change, privacy concerns, complexity

2. **Surrogate Key:**
   - Artificial identifier created by database
   - Examples: Auto-incrementing ID (1, 2, 3...)
   - **Pros:** Guaranteed unique, simple, stable
   - **Cons:** No business meaning, extra column

3. **Composite Key:**
   - Multiple columns working together
   - Examples: {StudentID, CourseID}, {OrderID, ProductID}
   - **Pros:** Natural for many-to-many relationships
   - **Cons:** More complex, harder to reference

**Choosing a Primary Key:**

Ask these questions:
1. Is it guaranteed unique?
2. Will it ever change?
3. Is it easy to reference in foreign keys?
4. Does it make logical sense?

**Examples:**

Good PK choices:
- ✓ StudentID (surrogate, simple)
- ✓ ISBN (natural, guaranteed unique)
- ✓ {StudentID, CourseID} (composite for bridge table)

Poor PK choices:
- ✗ StudentName (not unique, can change)
- ✗ Email (can change, may be null)
- ✗ Address (definitely can change)

---

**Foreign Keys (FK) - Deep Understanding**

**Purpose:**
- Creates relationships between tables
- Enforces referential integrity
- Implements the "links" from your ERD

**Characteristics:**
1. **References a PK:** FK value must exist in referenced table (or be NULL if allowed)
2. **Can be NULL:** If relationship is optional
3. **Can have duplicates:** Many orders can belong to same customer
4. **Can be part of composite key:** Often true in bridge tables

**Referential Integrity Rules:**

1. **Insert rule:** Can't insert FK value that doesn't exist in parent table
   ```
   ✗ Can't create order for CustomerID = 999 if customer 999 doesn't exist
   ```

2. **Update rule:** If PK changes, FK must update or prevent change
   ```
   If CustomerID 5 → 500, all orders must update
   OR database prevents the change
   ```

3. **Delete rule:** If parent row deleted, what happens to child rows?
   - **CASCADE:** Delete child rows too
   - **SET NULL:** Set FK to NULL
   - **RESTRICT:** Prevent deletion if children exist

**Example with Multiple FKs:**
```
ENROLLMENT(EnrollmentID, StudentID, CourseID, InstructorID, Grade)
  PK: EnrollmentID
  FK: StudentID → STUDENT(StudentID)
  FK: CourseID → COURSE(CourseID)
  FK: InstructorID → INSTRUCTOR(InstructorID)
```

One table can have multiple foreign keys pointing to different tables!

---

#### Hour 2: Functional Dependencies Mastery

**What are Functional Dependencies?**

A functional dependency exists when one attribute uniquely determines another attribute.

**Formal Definition:** X → Y means:
- If two rows have the same value for X, they MUST have the same value for Y
- X functionally determines Y
- Y is functionally dependent on X

**Real-World Examples:**

1. **StudentID → StudentName**
   - If two rows have same StudentID, they must have same StudentName
   - One student ID = one name

2. **ISBN → BookTitle**
   - One ISBN = one book title
   - ISBN uniquely determines the title

3. **{StudentID, CourseID} → Grade**
   - A specific student in a specific course = one grade
   - Need BOTH to determine the grade

**Types of Functional Dependencies:**

1. **Trivial Dependency:**
   - X → Y where Y is a subset of X
   - Example: {StudentID, StudentName} → StudentID
   - Not useful for database design

2. **Non-Trivial Dependency:**
   - X → Y where Y is not part of X
   - Example: StudentID → StudentName
   - These matter for normalization!

3. **Full Functional Dependency:**
   - Y depends on ALL of X (when X is composite)
   - Example: {OrderID, ProductID} → Quantity
   - Quantity needs both OrderID AND ProductID

4. **Partial Dependency:**
   - Y depends on only PART of X (when X is composite)
   - Example: {OrderID, ProductID} → ProductName
   - ProductName only needs ProductID, not OrderID
   - **Violates 2NF!**

5. **Transitive Dependency:**
   - X → Y and Y → Z, so X → Z indirectly
   - Example: StudentID → MajorCode → MajorName
   - StudentID determines MajorName through MajorCode
   - **Violates 3NF!**

**Identifying Functional Dependencies:**

Ask: "If I know [X], can I look up exactly one value of [Y]?"

Examples from a COURSE table:

```
COURSE(CourseID, CourseName, InstructorID, InstructorName, RoomNumber)

Dependencies:
- CourseID → CourseName ✓ (one course ID = one name)
- CourseID → InstructorID ✓ (course has one instructor)
- InstructorID → InstructorName ✓ (one instructor ID = one name)
- CourseID → RoomNumber ? (depends: if course always in same room, yes)
```

**Dependency Diagrams:**

Visual way to show functional dependencies:

```
CourseID → CourseName
        → InstructorID → InstructorName
                      → InstructorOffice

This shows:
- CourseID directly determines CourseName and InstructorID
- InstructorID determines InstructorName and InstructorOffice
- Therefore CourseID transitively determines InstructorName (3NF violation!)
```

**Practice Exercise:**

Given: ORDER(OrderID, CustomerID, CustomerName, OrderDate, ShipCity)

Identify all functional dependencies:
1. OrderID → CustomerID, OrderDate, ShipCity ✓
2. CustomerID → CustomerName ✓
3. OrderID → CustomerName ? (Yes, but transitively through CustomerID)

Which dependencies cause normalization problems?
- CustomerID → CustomerName is transitive (violates 3NF)

---

### Day 1, Evening Session (2 hours): Normalization Deep Dive

#### Hour 1: First & Second Normal Forms

**First Normal Form (1NF) - Detailed Rules**

**Goal:** Eliminate repeating groups and ensure atomic values

**Rule 1: Atomic Values (No Lists in Cells)**

Every cell must contain a single, indivisible value.

**Violations:**
```
❌ PhoneNumber: "555-1234, 555-5678, 555-9999"
❌ Colors: "Red, Blue, Green"
❌ Skills: "Java; Python; SQL"
```

**Fixes:**
```
✓ Create separate rows:
   | PersonID | PhoneNumber |
   | 1        | 555-1234    |
   | 1        | 555-5678    |
   | 1        | 555-9999    |

OR

✓ Create separate table:
   PERSON(PersonID, Name)
   PHONE(PersonID, PhoneNumber, PhoneType)
```

**Rule 2: No Repeating Groups (No Repeated Columns)**

Don't create columns like Item1, Item2, Item3...

**Violation:**
```
❌ ORDER
| OrderID | Item1  | Price1 | Item2  | Price2 | Item3  | Price3 |
| 1001    | Laptop | 899    | Mouse  | 25     | NULL   | NULL   |
```

Problems:
- What if customer orders 4 items?
- Wasted space if only 1 item
- Can't easily count items or sum prices

**Fix:**
```
✓ ORDER_DETAIL
| OrderID | ProductID | Quantity | Price |
| 1001    | P100      | 1        | 899   |
| 1001    | P101      | 1        | 25    |
```

**Complete 1NF Checklist:**
- [ ] Each cell contains exactly one value (no commas, no lists)
- [ ] No repeating columns (Item1, Item2, etc.)
- [ ] Each row is unique (has a primary key)
- [ ] Column order doesn't matter
- [ ] Row order doesn't matter

---

**Second Normal Form (2NF) - Detailed Rules**

**Goal:** Eliminate partial dependencies (only matters for composite keys)

**Rule:** Must be in 1NF AND every non-key attribute must depend on the ENTIRE primary key

**When does 2NF apply?**
- ONLY when you have a composite primary key
- If single-column PK, you're automatically in 2NF (no "partial" key to depend on)

**Classic Example:**

```
❌ ORDER_DETAIL(OrderID, ProductID, Quantity, ProductName, ProductPrice, OrderDate)
   Primary Key: {OrderID, ProductID}

Functional dependencies:
- {OrderID, ProductID} → Quantity ✓ (needs both - OK!)
- ProductID → ProductName ✗ (only needs ProductID - PROBLEM!)
- ProductID → ProductPrice ✗ (only needs ProductID - PROBLEM!)
- OrderID → OrderDate ✗ (only needs OrderID - PROBLEM!)

Problems this causes:
- ProductName repeated for every order (update anomaly)
- Can't add product without an order (insertion anomaly)
- Delete last order, lose product info (deletion anomaly)
```

**How to Fix - Decomposition:**

1. **Identify partial dependencies:**
   - ProductName depends only on ProductID
   - ProductPrice depends only on ProductID
   - OrderDate depends only on OrderID

2. **Create new tables:**
```
✓ ORDER(OrderID, OrderDate, CustomerID, ...)
   PK: OrderID

✓ PRODUCT(ProductID, ProductName, ProductPrice, ...)
   PK: ProductID

✓ ORDER_DETAIL(OrderID, ProductID, Quantity)
   PK: {OrderID, ProductID}
   FK: OrderID → ORDER
   FK: ProductID → PRODUCT
```

3. **Result:**
   - Each attribute now depends on entire PK
   - No more partial dependencies
   - Achieved 2NF!

**2NF Verification Checklist:**
- [ ] Table is in 1NF
- [ ] If single-column PK: automatically in 2NF ✓
- [ ] If composite PK: check each non-key attribute
  - [ ] Does it need ALL parts of the composite key?
  - [ ] If NO, move it to a separate table

---

#### Hour 2: Third Normal Form (The Industry Standard)

**Third Normal Form (3NF) - Detailed Rules**

**Goal:** Eliminate transitive dependencies

**Rule:** Must be in 2NF AND no non-key attribute depends on another non-key attribute

**What's a Transitive Dependency?**

A depends on B, and B depends on C, so A depends on C indirectly.

Format: A → B → C (meaning A transitively determines C)

**Classic Example:**

```
❌ EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation, DeptPhone)
   Primary Key: EmpID

Functional dependencies:
- EmpID → EmpName ✓ (direct - OK!)
- EmpID → DeptID ✓ (direct - OK!)
- DeptID → DeptName ✗ (transitive - PROBLEM!)
- DeptID → DeptLocation ✗ (transitive - PROBLEM!)
- DeptID → DeptPhone ✗ (transitive - PROBLEM!)

Chain: EmpID → DeptID → DeptName (transitive!)

Problems this causes:
- Department info repeated for every employee in that dept (redundancy)
- Update dept name, must change many rows (update anomaly)
- Delete all employees, lose department info (deletion anomaly)
- Can't add department without employee (insertion anomaly)
```

**How to Recognize Transitive Dependencies:**

Look for "non-key → non-key" dependencies:
- DeptID is not the primary key of EMPLOYEE
- DeptName is not part of any key
- But DeptID → DeptName exists
- This is transitive!

**How to Fix - Decomposition:**

1. **Identify the transitive chain:**
   - EmpID → DeptID → DeptName, DeptLocation, DeptPhone

2. **Create separate table for the dependent attributes:**
```
✓ EMPLOYEE(EmpID, EmpName, DeptID)
   PK: EmpID
   FK: DeptID → DEPARTMENT

✓ DEPARTMENT(DeptID, DeptName, DeptLocation, DeptPhone)
   PK: DeptID
```

3. **Result:**
   - Department info stored once
   - No transitive dependencies
   - Achieved 3NF!

**Another Example - Course System:**

```
❌ COURSE(CourseID, CourseName, InstructorID, InstructorName, InstructorOffice)
   PK: CourseID

Dependencies:
- CourseID → InstructorID ✓
- InstructorID → InstructorName ✗ (transitive!)
- InstructorID → InstructorOffice ✗ (transitive!)

Fix:
✓ COURSE(CourseID, CourseName, InstructorID)
   FK: InstructorID → INSTRUCTOR

✓ INSTRUCTOR(InstructorID, InstructorName, InstructorOffice)
   PK: InstructorID
```

**3NF Verification Checklist:**
- [ ] Table is in 2NF
- [ ] Check each non-key attribute:
  - [ ] Does it depend DIRECTLY on the PK?
  - [ ] Or does it depend on another non-key attribute?
- [ ] If transitive dependencies exist, decompose

**Why Stop at 3NF?**

3NF is the industry standard because:
1. Eliminates most redundancy problems
2. Provides excellent data integrity
3. Doesn't overcomplicate the design
4. Good balance of normalization vs. query complexity

Higher forms (BCNF, 4NF, 5NF) exist but are rarely needed in practice.

---

### Day 2, Morning Session (2 hours): Advanced Topics

#### Hour 1: Bridge Tables & Many-to-Many Relationships

**Deep Dive: Why Bridge Tables?**

Relational databases can only implement one-to-many relationships directly. Many-to-many relationships must be decomposed.

**The Problem:**

```
Scenario: Students take Courses

❌ Can't do this:
STUDENT(StudentID, Name, CourseID)  ← What if student takes 3 courses?
COURSE(CourseID, Title, StudentID)  ← What if course has 50 students?
```

**The Solution: Bridge Table**

Break M:N into two 1:M relationships:
```
✓ STUDENT(StudentID, Name)
   One student...

✓ ENROLLMENT(StudentID, CourseID, Grade, Semester)
   ...has many enrollments

✓ COURSE(CourseID, Title, Credits)
   One course has many enrollments
```

**Bridge Table Characteristics:**

1. **Primary Key:**
   - Usually composite of both foreign keys
   - Example: {StudentID, CourseID}
   - Ensures student can't enroll in same course twice

2. **Foreign Keys:**
   - References both parent entities
   - Example: StudentID → STUDENT, CourseID → COURSE

3. **Additional Attributes:**
   - Store relationship-specific data
   - Example: Grade, Semester, EnrollmentDate
   - These belong to the RELATIONSHIP, not to Student or Course

4. **Naming:**
   - Use verb or action: ENROLLMENT, REGISTRATION, ASSIGNMENT
   - Or combine names: STUDENT_COURSE, ACTOR_MOVIE
   - Make it meaningful!

**More Examples:**

**Authors & Books:**
```
AUTHOR(AuthorID, Name)
BOOK(BookID, Title)
AUTHORSHIP(AuthorID, BookID, AuthorOrder)
  ← AuthorOrder: 1st author, 2nd author, etc.
```

**Actors & Movies:**
```
ACTOR(ActorID, Name)
MOVIE(MovieID, Title)
CASTING(ActorID, MovieID, CharacterName, BillingOrder)
  ← Store character played and billing order
```

**Products & Suppliers:**
```
PRODUCT(ProductID, ProductName)
SUPPLIER(SupplierID, CompanyName)
SUPPLY(SupplierID, ProductID, UnitPrice, LeadTimeDays)
  ← Price and lead time are relationship-specific
```

**When NOT to Use Bridge Table:**

One-to-Many relationships don't need bridge tables:
```
✓ CUSTOMER(CustomerID, Name)
✓ ORDER(OrderID, CustomerID, OrderDate)
           ↑ FK is enough - no bridge needed!
```

---

#### Hour 2: Denormalization & Practical Tradeoffs

**Understanding Denormalization**

**Key Principle:** Always normalize first, then strategically denormalize based on real performance data.

**What is Denormalization?**
- Intentionally introducing redundancy into a normalized database
- Trade data integrity for query performance
- Common in high-traffic systems and data warehouses

**When to Consider Denormalization:**

1. **Scenario: Slow Reporting Queries**
   ```
   Problem: Monthly sales report joins 8 tables, takes 5 minutes

   Normalized (slow):
   SELECT c.CustomerName, SUM(od.Quantity * od.Price)
   FROM CUSTOMER c
   JOIN ORDER o ON c.CustomerID = o.CustomerID
   JOIN ORDER_DETAIL od ON o.OrderID = od.OrderID
   JOIN PRODUCT p ON od.ProductID = p.ProductID
   ... (4 more joins)
   GROUP BY c.CustomerName

   Denormalized (fast):
   SELECT CustomerName, MonthlySales
   FROM SALES_SUMMARY
   -- Pre-computed summary table, no joins!
   ```

   **Solution:** Create a summary table, update it nightly

2. **Scenario: High-Traffic Web Pages**
   ```
   Problem: Product page needs 5 joins, viewed 1 million times/day

   Denormalized approach:
   PRODUCT(ProductID, Name, CategoryName, SupplierName, ...)
     ↑ Store category/supplier names directly (redundant but fast)

   Why it works:
   - Read 1M times, updated rarely
   - 1M fast reads worth occasional update complexity
   ```

3. **Scenario: Historical Data Preservation**
   ```
   Problem: Customer moves, but old orders should show old address

   Denormalized approach:
   ORDER(OrderID, CustomerID, ShipName, ShipAddress, ...)
     ↑ Store customer info at time of order (redundant but necessary)

   Why it's necessary:
   - Order is a historical snapshot
   - If customer updates profile, orders shouldn't change
   ```

4. **Scenario: Calculated Fields**
   ```
   Problem: Calculating order total on every query is expensive

   Denormalized approach:
   ORDER(OrderID, CustomerID, OrderTotal, ...)
     ↑ Store pre-calculated total

   Update strategy:
   - Calculate on insert
   - Recalculate if line items change
   - Use database triggers to maintain
   ```

**Denormalization Strategies:**

1. **Materialized Views:**
   - Database automatically maintains denormalized view
   - Refreshed on schedule or on-demand
   - Best of both worlds (when available)

2. **Caching Layers:**
   - Keep database normalized
   - Cache denormalized results in application layer
   - Example: Redis cache for product details

3. **Read Replicas:**
   - Normalized master database for writes
   - Denormalized replica for reads
   - Eventual consistency model

4. **Star Schema (Data Warehouses):**
   - Fact table (measures) + Dimension tables (denormalized)
   - Optimized for analytical queries
   - Separate from transactional database

**The Golden Rules:**

1. ✓ Always start with a fully normalized design
2. ✓ Profile to identify actual performance bottlenecks
3. ✓ Denormalize strategically, document decisions
4. ✓ Maintain data integrity through triggers/application logic
5. ✗ Don't denormalize prematurely ("premature optimization")
6. ✗ Don't denormalize to avoid learning joins

---

### Day 2, Afternoon Session (2 hours): Practice & Review

#### Hour 1: Worked Examples

**Example 1: Library System**

**Requirements:**
- Track books (ISBN, title, author)
- Track patrons (card number, name, email)
- Track checkouts (which patron checked out which book, when)
- Books can have multiple authors
- Patrons can check out multiple books
- Books can be checked out multiple times (over time)

**Step 1: Identify Entities**
- BOOK
- AUTHOR
- PATRON
- CHECKOUT (the action/transaction)

**Step 2: Identify Relationships**
- AUTHOR ↔ BOOK (many-to-many: books can have multiple authors, authors write multiple books)
- PATRON ↔ BOOK (many-to-many: patrons check out many books, books checked out by many patrons over time)

**Step 3: Design Tables**

```
AUTHOR(AuthorID, AuthorName, Bio)
  PK: AuthorID

BOOK(ISBN, Title, PublicationYear, Publisher)
  PK: ISBN

AUTHORSHIP(AuthorID, ISBN, AuthorOrder)
  PK: {AuthorID, ISBN}
  FK: AuthorID → AUTHOR
  FK: ISBN → BOOK
  ← Bridge table for Author-Book M:N

PATRON(PatronID, Name, Email, JoinDate)
  PK: PatronID

CHECKOUT(CheckoutID, PatronID, ISBN, CheckoutDate, DueDate, ReturnDate)
  PK: CheckoutID
  FK: PatronID → PATRON
  FK: ISBN → BOOK
  ← Note: Not a composite PK because same patron can check out same book multiple times
```

**Step 4: Verify Normalization**

Check CHECKOUT table:
- 1NF: ✓ All atomic values
- 2NF: ✓ Single-column PK (CheckoutID), automatically in 2NF
- 3NF: Check for transitive dependencies
  - CheckoutID → PatronID → PatronName?
  - No! PatronName is in PATRON table, not CHECKOUT
  - ✓ No transitive dependencies in CHECKOUT

All tables are in 3NF ✓

---

**Example 2: University Database**

**Requirements:**
- Students enroll in courses
- Professors teach courses
- Departments offer courses
- Track student grades
- One course has one professor (simplified)
- One course belongs to one department

**Step 1: Identify Entities**
- STUDENT
- COURSE
- PROFESSOR
- DEPARTMENT

**Step 2: Identify Relationships**
- STUDENT ↔ COURSE (M:N - students take multiple courses, courses have multiple students)
- PROFESSOR → COURSE (1:M - professor teaches many courses, course has one professor)
- DEPARTMENT → COURSE (1:M - department offers many courses, course belongs to one department)

**Step 3: Initial Design**

```
DEPARTMENT(DeptID, DeptName, Building, Phone)
  PK: DeptID

PROFESSOR(ProfID, ProfName, DeptID, Office, Email)
  PK: ProfID
  FK: DeptID → DEPARTMENT

COURSE(CourseID, CourseName, Credits, DeptID, ProfID)
  PK: CourseID
  FK: DeptID → DEPARTMENT
  FK: ProfID → PROFESSOR

STUDENT(StudentID, StudentName, Email, Major)
  PK: StudentID

ENROLLMENT(StudentID, CourseID, Semester, Grade)
  PK: {StudentID, CourseID, Semester}
    ← Composite includes Semester so student can retake course
  FK: StudentID → STUDENT
  FK: CourseID → COURSE
```

**Step 4: Check for Problems**

Potential issue in COURSE table:
```
COURSE(CourseID, CourseName, Credits, DeptID, ProfID)

If: DeptID → Building, Phone (from DEPARTMENT)
Then: CourseID → DeptID → Building (transitive!)
```

Is this a problem?
- Actually NO, because Building and Phone are NOT in the COURSE table
- They're properly stored in DEPARTMENT table
- COURSE only has DeptID (the FK), not the dependent attributes
- ✓ This is correct design!

**The key insight:** Having a FK doesn't violate 3NF. Storing the transitively dependent attributes WOULD violate 3NF.

---

#### Hour 2: Self-Assessment & Final Review

**Practice Quiz: Test Your Knowledge**

**Section 1: ERD & Relationships (10 questions)**

1. What shape represents an entity in an ERD?
   - Answer: Rectangle

2. What does the symbol "o≺" mean in crow's feet notation?
   - Answer: Zero or many (optional many)

3. TRUE or FALSE: A one-to-many relationship requires a bridge table.
   - Answer: FALSE (only M:N needs bridge table)

4. Where do you place the foreign key in a one-to-many relationship?
   - Answer: In the "many" side table

5. What is the primary key of a typical bridge table?
   - Answer: Composite key of the two foreign keys

6. Student takes Courses, Course has Students. What type of relationship?
   - Answer: Many-to-many (M:N)

7. In notation "CUSTOMER ——|—————o≺—— ORDER", how many orders can a customer have?
   - Answer: Zero or many

8. What makes a primary key "composite"?
   - Answer: Made of 2+ columns working together

9. Can a foreign key be NULL?
   - Answer: Yes, if the relationship is optional

10. TRUE or FALSE: A table can have multiple foreign keys.
    - Answer: TRUE

---

**Section 2: Functional Dependencies (10 questions)**

11. What does "X → Y" mean?
    - Answer: If you know X, you can determine Y (X determines Y)

12. In "StudentID → StudentName", what is the determinant?
    - Answer: StudentID (left side)

13. What is a partial dependency?
    - Answer: When an attribute depends on only PART of a composite key

14. What is a transitive dependency?
    - Answer: When A → B and B → C, so A → C indirectly

15. Given PK: {OrderID, ProductID}, is "ProductID → ProductName" a partial dependency?
    - Answer: YES (depends on only ProductID, not full key)

16. TRUE or FALSE: Partial dependencies violate 3NF.
    - Answer: FALSE (they violate 2NF)

17. Given PK: EmpID, and "EmpID → DeptID → DeptName", what violates 3NF?
    - Answer: The transitive dependency (DeptID → DeptName)

18. Can a table with a single-column primary key have partial dependencies?
    - Answer: NO (no "part" of key to depend on)

19. What's the difference between full and partial dependency?
    - Answer: Full needs entire composite key, partial needs only part

20. TRUE or FALSE: All transitive dependencies involve non-key attributes.
    - Answer: TRUE (key attributes determine others, not vice versa)

---

**Section 3: Normal Forms (15 questions)**

21. What does 1NF require?
    - Answer: Atomic values, no repeating groups

22. Is "PhoneNumbers: 555-1234, 555-5678" in 1NF?
    - Answer: NO (multiple values in one cell)

23. What does 2NF eliminate?
    - Answer: Partial dependencies

24. If a table has single-column PK and is in 1NF, is it automatically in 2NF?
    - Answer: YES (no composite key = no partial dependencies)

25. What does 3NF eliminate?
    - Answer: Transitive dependencies

26. Why is 3NF considered the industry standard?
    - Answer: Balances data integrity with reasonable complexity

27. What are the three database anomalies?
    - Answer: Update, Insertion, Deletion anomalies

28. What is an update anomaly?
    - Answer: Same data in multiple rows, changing requires updating many rows

29. What is an insertion anomaly?
    - Answer: Can't add data without adding other unrelated data

30. What is a deletion anomaly?
    - Answer: Deleting one piece of data causes loss of other important data

31. To fix a 2NF violation, what do you do?
    - Answer: Move partially dependent attributes to a new table

32. To fix a 3NF violation, what do you do?
    - Answer: Move transitively dependent attributes to a new table

33. TRUE or FALSE: All tables in 3NF are also in 2NF and 1NF.
    - Answer: TRUE (each form builds on previous)

34. What's the main purpose of normalization?
    - Answer: Reduce data redundancy and prevent anomalies

35. When might you intentionally denormalize a database?
    - Answer: For performance reasons in read-heavy systems

---

**Final Checklist: Am I Ready for the Exam?**

**Concepts I Should Know:**
- [ ] Can identify entities, attributes, relationships in ERD
- [ ] Can read and draw crow's feet notation
- [ ] Can determine relationship types (1:1, 1:M, M:N)
- [ ] Understand when bridge tables are needed
- [ ] Can identify primary keys (simple, composite)
- [ ] Can identify foreign keys and their purpose
- [ ] Understand functional dependency notation (X → Y)
- [ ] Can identify partial dependencies
- [ ] Can identify transitive dependencies
- [ ] Know the requirements for 1NF, 2NF, 3NF
- [ ] Can decompose tables to achieve higher normal forms
- [ ] Understand the three types of database anomalies
- [ ] Know when and why to denormalize

**Skills I Should Have:**
- [ ] Given a scenario, can design an ERD with proper relationships
- [ ] Can determine appropriate cardinality for relationships
- [ ] Can identify normalization violations in a table
- [ ] Can decompose unnormalized tables step-by-step
- [ ] Can explain WHY a design violates a normal form
- [ ] Can draw crow's feet notation symbols from memory

**If you can check most of these boxes, you're ready! 🎓**

---

## 📝 Quick Reference Sheet (Print This!)

**Crow's Feet Notation:**
- |— = Mandatory One
- o— = Optional One
- |≺ = Mandatory Many
- o≺ = Optional Many

**Normal Forms Quick Check:**
- **1NF:** Atomic values? No repeating groups? ✓
- **2NF:** 1NF + No partial dependencies? ✓
- **3NF:** 2NF + No transitive dependencies? ✓

**Functional Dependencies:**
- X → Y = "X determines Y"
- Partial = depends on PART of composite key (violates 2NF)
- Transitive = A → B → C (violates 3NF)

**Relationship Types:**
- **1:1** = One person, one passport
- **1:M** = One customer, many orders (FK in "many" side)
- **M:N** = Many students, many courses (NEEDS bridge table)

**Three Anomalies:**
1. **Update:** Same data in multiple rows
2. **Insertion:** Can't add without other data
3. **Deletion:** Lose data when deleting

**Keys:**
- **PK:** Uniquely identifies row, not NULL, minimal
- **FK:** References PK in another table, creates relationship
- **Composite:** PK made of 2+ columns

---

## 🎯 Final Exam Tips

**Time Management:**
- Read ALL questions first
- Answer easy questions first to build confidence
- Budget time based on point values
- Save 5-10 minutes for review

**For Diagram Questions:**
- Draw clearly (instructor needs to read it)
- Label everything (entities, relationships, notation)
- Show your work even if not perfect
- Partial credit is common on diagrams

**For Short Answer:**
- Define terms clearly
- Give examples when asked
- Explain your reasoning
- Show work on decomposition problems

**Common Mistakes to Avoid:**
- Don't confuse partial and transitive dependencies
- Don't forget the circle (o) for optional relationships
- Don't create bridge tables for 1:M relationships
- Don't skip stating what normal form is violated

**The Night Before:**
- Review this study guide
- Get good sleep (seriously!)
- Have materials ready (pencils, eraser, notes)
- Eat a good breakfast
- Arrive early to reduce stress

---

## Good Luck! 🍀

Remember: Understanding the concepts is more important than memorizing. Think about the "why" behind each rule, and you'll do great!

**You've got this!** 💪

---

*Study guide created for CSCI 101 Module 2 Exam*
*Topics: Database Design, ERD, Normalization, and Relationships*
