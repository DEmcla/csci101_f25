# CSCI 101: Module 2 Exam - REVISED ANSWER KEY
## Database Design, ERD, Normalization, and Relationships

**Total Points:** 100 points
**Time Limit:** 85 minutes

---

## CHANGES FROM ORIGINAL VERSION

### Questions Removed (to improve time management):
- Original Q8 (Denormalization definition - redundant with Q25 and Q40)
- Original Q14 (BCNF/4NF/5NF commonality - less critical concept)
- Original Q33 (DateOfBirth attribute type - least important concept)

### Questions Modified:
- **Q18 (now same number):** Added explicit "Primary Key:" statement to remove ambiguity
- **Q35 (now same number):** Revised table to show clear repeating groups (BookISBN1, BookISBN2, etc.)
- **Q36 (now same number):** Increased from 5 to 6 points (2 points each symbol for clearer grading)
- **Q37 (now same number):** Increased from 6 to 7 points (3 points for part c, 1.5 per table)
- **Q38 (now same number):** Increased from 5 to 6 points with detailed grading breakdown shown
- **Q40 (now same number):** Increased from 4 to 6 points with explicit grading breakdown

### Result:
- **37 questions** (down from 40)
- **85 minutes** (up from 75)
- **100 points** (maintained)
- More time per question, reduced rushing
- Better grading granularity on complex questions

---

## PART A: TRUE/FALSE (19.5 points total)

**1. TRUE** (1.5 points)
- Rectangles = entities, ovals = attributes (standard ERD notation)

**2. TRUE** (1.5 points)
- Composite keys are made of 2+ columns (e.g., {StudentID, CourseID})

**3. TRUE** (1.5 points)
- Crow's foot (≺) indicates the "many" side

**4. FALSE** (1.5 points)
- 1NF eliminates non-atomic values and repeating groups
- 3NF eliminates transitive dependencies

**5. TRUE** (1.5 points)
- This is the definition of functional dependency

**6. FALSE** (1.5 points)
- Bridge tables resolve **many-to-many** relationships, not one-to-one

**7. TRUE** (1.5 points)
- This is the definition of partial dependency (violates 2NF)

**9. TRUE** (1.5 points)
- This is the definition of 2NF

**10. TRUE** (1.5 points)
- This is the definition and purpose of foreign keys

**11. FALSE** (1.5 points)
- Many-to-many requires a bridge entity/table in between

**12. TRUE** (1.5 points)
- 3NF is the industry standard for most applications

**13. TRUE** (1.5 points)
- This is the definition of cardinality

**15. TRUE** (1.5 points)
- These are the three anomalies normalization prevents

---

## PART B: MULTIPLE CHOICE (42.5 points total)

**16. ANSWER: b)** PhoneNumber: "555-1234, 555-5678" (2.5 points)
- Multiple values in one cell violates atomicity (1NF)

**17. ANSWER: b)** Single line on one end, crow's foot on the other (2.5 points)
- One side = single, many side = crow's foot

**18. ANSWER: c)** Composite primary key (2.5 points)
- Made of two columns working together
- **NOTE:** Question now explicitly states "Primary Key: {OrderID, ProductID}" to remove ambiguity

**19. ANSWER: b)** Second Normal Form (2NF) (2.5 points)
- 2NF specifically eliminates partial dependencies

**20. ANSWER: b)** When A → B and B → C, so A → C indirectly (2.5 points)
- This is the definition of transitive dependency

**21. ANSWER: b)** An entity that resolves a many-to-many relationship (2.5 points)
- Bridge/associative entities break M:N into two 1:M relationships

**22. ANSWER: c)** 3NF (2.5 points)
- Transitive dependency exists: CourseID → InstructorID → InstructorName/Office
- Table is in 2NF (no partial dependencies with single-column PK) but violates 3NF

**23. ANSWER: b)** To reduce data redundancy and prevent anomalies (2.5 points)
- This is the primary purpose of normalization

**24. ANSWER: b)** Determinant (2.5 points)
- The left side of X → Y is the determinant

**25. ANSWER: a)** A frequently-run report that requires joining 8 tables and is too slow (2.5 points)
- Performance issues are the main reason to denormalize

**26. ANSWER: b)** Partial dependency (2.5 points)
- StudentName depends on only part of the composite key {StudentID, CourseID}

**27. ANSWER: b)** Mandatory participation (at least one required) (2.5 points)
- Perpendicular line = mandatory, circle = optional

**28. ANSWER: d)** BCNF (2.5 points)
- BCNF requires all determinants to be candidate keys

**29. ANSWER: d)** Many-to-many (2.5 points)
- Many students can take many courses (M:N relationship)

**30. ANSWER: b)** Create a separate PRODUCT table with ProductID and ProductName (2.5 points)
- This removes the partial dependency (ProductID → ProductName)

**31. ANSWER: c)** The number of entity instances that can participate in a relationship (2.5 points)
- Cardinality defines relationship quantities (1:1, 1:M, M:N)

**32. ANSWER: b)** It balances data integrity with reasonable complexity (2.5 points)
- 3NF provides good integrity without excessive complexity

---

## PART C: SHORT ANSWER (38 points total)

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
| CardNumber | PatronName | BookISBN1 | BookTitle1 | BookISBN2 | BookTitle2 | CheckoutDate |
|------------|------------|-----------|------------|-----------|------------|--------------|
| C001 | Alice Brown | 978-01 | Database Design | 978-02 | Data Mining | 2024-01-15 |

Identify **TWO specific violations of First Normal Form (1NF)** in this table schema and explain why each is a problem.

**ANSWER:**

**Violation #1: Repeating groups (BookISBN1, BookISBN2, BookTitle1, BookTitle2)** (2.5 points)
- The table has repeating columns for books (Book1, Book2, etc.)
- This violates 1NF which requires no repeating groups
- Problems:
  - What if a patron checks out 3 books? Need to add more columns
  - Wasted space if patron checks out only 1 book
  - Difficult to query (need to search Book1, Book2, Book3, etc. separately)
  - Cannot easily determine how many books are checked out

**Violation #2: The repeating groups create non-atomic structure** (2.5 points)
- The "set of books" is conceptually split across multiple column pairs
- Each row contains multiple book facts (Book1 data, Book2 data)
- Proper 1NF would have one book per row
- Problems:
  - Adding or removing a book requires restructuring
  - Partial NULL values if fewer than max books checked out
  - Cannot enforce integrity constraints easily

**Alternative acceptable partial answers:**
- If student mentions that each book should be in its own row (separation approach)
- If student identifies that this creates update/insertion/deletion anomalies

**Grading:**
- 1.25 points per violation clearly identified
- 1.25 points per explanation of why it's a problem
- Must identify TWO distinct 1NF violations related to repeating groups

**NOTE:** This question was revised from the original to make violations clearly visible in the schema.

---

**Question 36 (6 points):** Draw the crow's feet notation symbols for the following:

a) **One and only one** (mandatory one)
b) **Zero or many** (optional many)
c) **One or many** (mandatory many)

**ANSWER:**

**a) One and only one (mandatory one): |—** (2 points)
- Perpendicular line (mandatory) + single line (one)
- Visual representation:
```
——|—
  or
——⊣—
```
- The perpendicular bar indicates "mandatory" (at least one required)
- The single line indicates "exactly one"
- Together: exactly one, required

**Grading for (a):**
- 2 points if both elements present and correct
- 1 point if one element correct but second missing/wrong
- 0.5 points if attempt shows understanding but execution poor

**b) Zero or many (optional many): o≺** (2 points)
- Circle (optional) + crow's foot (many)
- Visual representation:
```
——o≺
  or
——○<
```
- The circle indicates "optional" (zero allowed)
- The crow's foot indicates "many"
- Together: zero or more (optional participation, many allowed)

**Grading for (b):**
- 2 points if both elements present and correct
- 1 point if one element correct but second missing/wrong
- 0.5 points if attempt shows understanding but execution poor

**c) One or many (mandatory many): |≺** (2 points)
- Perpendicular line (mandatory) + crow's foot (many)
- Visual representation:
```
——|≺
  or
——⊣<
```
- The perpendicular bar indicates "mandatory" (at least one required)
- The crow's foot indicates "many"
- Together: one or more (mandatory participation, many allowed)

**Grading for (c):**
- 2 points if both elements present and correct
- 1 point if one element correct but second missing/wrong
- 0.5 points if attempt shows understanding but execution poor

**General Grading Notes:**
- Accept hand-drawn symbols that clearly show the two components
- Symbols don't need to be perfect, but meaning must be clear
- Common student errors to watch for:
  - Forgetting the circle for "optional"
  - Using wrong symbol for mandatory (dash instead of perpendicular line)
  - Drawing crow's foot incorrectly (should have 3 lines)

**Visual Guide for Instructor Reference:**
```
Mandatory indicators:  |  or  ⊣  (perpendicular line)
Optional indicators:   o  or  ○  (circle)
One indicators:        —  (single line)
Many indicators:       ≺  or  <  (crow's foot - three lines)
```

---

**Question 37 (7 points):** Given this table in 1NF:

**EMPLOYEE(EmpID, EmpName, DeptID, DeptName, DeptLocation)**

- Primary Key: EmpID
- Functional Dependencies:
  - `EmpID → EmpName, DeptID`
  - `DeptID → DeptName, DeptLocation`

a) What normal form violation exists in this table?
b) Explain why this is a problem (what anomaly could occur?).
c) Decompose this table to fix the problem. Show the resulting table structures with their primary keys clearly marked.

**ANSWER:**

**a) Transitive dependency / Violates 3NF** (2 points)
- EmpID → DeptID → DeptName, DeptLocation
- This is a transitive dependency (goes through intermediate non-key attribute)
- The table is in 2NF (single-column PK, so no partial dependencies possible)
- But violates 3NF (has transitive dependency)

**Grading for (a):**
- 2 points for "transitive dependency" OR "violates 3NF"
- 1 point for partial answer (e.g., "dependency problem" without specifying type)
- 0 points if answer indicates 1NF or 2NF violation

**b) Anomalies that could occur:** (2 points - must mention at least one specific anomaly with clear example)

Acceptable answers (any ONE is sufficient for full credit):

- **Update anomaly:** If a department changes name or location, must update multiple employee records (every employee in that department). Risk of inconsistency if some rows updated but not others.

- **Deletion anomaly:** If the last employee in a department is deleted, we lose all information about that department (DeptName and DeptLocation are lost even though the department still exists).

- **Insertion anomaly:** Cannot add a new department to the database without first hiring an employee in that department (can't have DeptID without an EmpID).

**Grading for (b):**
- 2 points for correct anomaly with clear explanation
- 1.5 points for correct anomaly with weak explanation
- 1 point for identifying correct anomaly without clear explanation
- 0.5 points for vague answer like "causes problems" without specificity
- 0 points if no anomaly mentioned or anomaly is incorrect

**c) Decomposed tables:** (3 points)

**EMPLOYEE Table:** (1.5 points)
- EmpID (PK)
- EmpName
- DeptID (FK)

**DEPARTMENT Table:** (1.5 points)
- DeptID (PK)
- DeptName
- DeptLocation

**Grading for (c):**
- 1.5 points per table if structure is correct
- Deduct 0.25 points per table if PK not clearly marked
- Deduct 0.25 points if FK not indicated (but don't double-penalize)
- Award 1 point per table for mostly correct structure even if minor errors
- Award 0.5 points per table if shows understanding but significant errors

**Alternative acceptable answers for (c):**
- Different table names (e.g., EMP, DEPT) are fine
- Different notation for PK (underlining, asterisk, etc.) as long as clear
- Listing attributes vertically or horizontally both acceptable

**Common student errors to watch for:**
- Leaving DeptName and DeptLocation in EMPLOYEE table (no decomposition)
- Forgetting to include DeptID in EMPLOYEE as foreign key
- Creating more than 2 tables (over-decomposition)
- Not marking primary keys

---

**Question 38 (6 points):** A university database needs to track students and courses.

- A student can enroll in many courses
- A course can have many students
- For each enrollment, we need to track the grade and semester

Draw a simple ERD showing these three entities (STUDENT, COURSE, and the appropriate bridge entity) with their relationships using crow's feet notation. Label the entities and show the relationship lines with proper notation. Clearly indicate where Grade and Semester are stored.

**ANSWER:**

**Visual representation (instructor reference):**

```
     One student, many enrollments          One course, many enrollments
              (1:M)                                    (1:M)

STUDENT ——|—————o≺—— ENROLLMENT ——≺o—————|—— COURSE

┌─────────┐          ┌────────────┐          ┌─────────┐
│ STUDENT │          │ ENROLLMENT │          │ COURSE  │
├─────────┤          ├────────────┤          ├─────────┤
│StudentID│          │StudentID(FK)│         │CourseID │
│  (PK)   │          │CourseID(FK)│          │  (PK)   │
│Name     │          │ {PK}       │          │Name     │
│...      │          │Grade       │          │Credits  │
│         │          │Semester    │          │...      │
└─────────┘          └────────────┘          └─────────┘
```

**Text description of correct answer:**
- STUDENT entity box on left (can include StudentID and other attributes)
- COURSE entity box on right (can include CourseID and other attributes)
- ENROLLMENT bridge entity in the middle
- ENROLLMENT contains: StudentID (FK), CourseID (FK), Grade, Semester
- ENROLLMENT has composite PK: {StudentID, CourseID}
- Relationship line from STUDENT to ENROLLMENT with crow's feet notation showing 1:M
  - Notation should show: one student, many enrollments (—|———o≺)
- Relationship line from COURSE to ENROLLMENT with crow's feet notation showing 1:M
  - Notation should show: one course, many enrollments (—|———o≺)

**Grading breakdown:**

**STUDENT entity: 1 point**
- 1 point if entity clearly labeled and drawn as box/rectangle
- 0.5 points if present but poorly labeled
- Can include or omit attributes (both acceptable)

**COURSE entity: 1 point**
- 1 point if entity clearly labeled and drawn as box/rectangle
- 0.5 points if present but poorly labeled
- Can include or omit attributes (both acceptable)

**ENROLLMENT bridge entity: 1.5 points**
- 1 point if entity clearly labeled and drawn as box/rectangle
- 0.5 points if shows as bridge/middle entity connecting the other two
- Deduct 0.25 if poorly positioned or unclear it's the bridge

**Correct crow's feet notation on relationships: 1.5 points**
- 0.75 points for correct STUDENT-to-ENROLLMENT relationship line with proper notation
  - Should show "one" on STUDENT side, "many" on ENROLLMENT side
  - Accept reasonable variations: |—o≺ or ⊣—○< etc.
- 0.75 points for correct COURSE-to-ENROLLMENT relationship line with proper notation
  - Should show "one" on COURSE side, "many" on ENROLLMENT side
- Deduct 0.25 per relationship if notation is present but incorrect
- Deduct 0.5 per relationship if no notation shown (just plain lines)

**Grade and Semester shown in ENROLLMENT: 1 point**
- 1 point if both Grade and Semester clearly indicated as being in ENROLLMENT
- 0.5 points if only one shown or if placement ambiguous
- 0 points if both placed in wrong entity or missing entirely

**Accept reasonable variations as long as relationships are correct:**
- Box shapes can vary (rounded rectangles, plain rectangles, etc.)
- Horizontal or vertical layout both acceptable
- Attributes can be listed inside boxes or omitted (as long as Grade/Semester placement clear)
- Different crow's feet notation styles (three lines vs. arrow vs. < symbol) all acceptable
- Optional vs. mandatory notation may vary (accept either o≺ or |≺ as long as "many" is clear)

**Common student errors to watch for:**
- Showing direct M:N relationship between STUDENT and COURSE without bridge entity (major error)
- Putting Grade/Semester in STUDENT or COURSE instead of ENROLLMENT
- Drawing relationship lines but forgetting crow's feet notation
- Creating unnecessary additional entities
- Using wrong cardinality (e.g., 1:1 instead of 1:M)
- Crow's feet pointing wrong direction

**Partial credit guidelines:**
- If student shows understanding of bridge entity concept but has notation errors, award at least 50%
- If student attempts crow's feet but gets direction wrong, deduct only 0.25 per relationship
- If overall structure correct but messy, be generous with grading
- Hand-drawn diagrams will have imperfections—focus on conceptual correctness

---

**Question 39 (4 points):** List the three types of database anomalies that normalization helps prevent and provide a one-sentence description of each.

**ANSWER:**

**1. Update Anomaly** (~1.33 points)
- When you have to update the same information in multiple places, creating risk of inconsistency
- OR: Changing one fact requires updating multiple rows, and you might miss some

**2. Insertion Anomaly** (~1.33 points)
- When you cannot add data without also adding other unrelated data
- OR: Cannot add a new record because other required information is missing or not applicable

**3. Deletion Anomaly** (~1.34 points)
- When deleting one piece of information unintentionally causes loss of other important information
- OR: Removing a record causes loss of other unrelated data that you wanted to keep

**Grading:**
- ~1.33 points per anomaly (4 points total ÷ 3 anomalies)
- **For each anomaly:**
  - 0.67 points for correctly naming the anomaly
  - 0.67 points for providing accurate description
- Must provide all THREE anomalies for full credit
- Deduct proportionally if anomalies missing or incorrect

**Detailed grading guidance:**

**Naming (0.67 points each):**
- Full credit: Exactly correct name ("Update Anomaly" or "Modification Anomaly")
- Partial credit: Close approximation (e.g., "Change Anomaly" for Update Anomaly)
- No credit: Wrong name or missing

**Description (0.67 points each):**
- Full credit: Clear, accurate explanation that captures the essence
- Partial credit (0.35 points): Vague or partially correct explanation
- No credit: Incorrect explanation or missing

**Examples of student answers that deserve full credit:**

*Update Anomaly:*
- "Same data appears in multiple rows, so updating requires changing many rows"
- "Redundant data must be updated everywhere or database becomes inconsistent"
- "If information repeats, you have to update it in all places"

*Insertion Anomaly:*
- "Can't add a record without unrelated information being present"
- "Cannot insert a fact independently of another fact"
- "Forced to add irrelevant data to add the data you want"

*Deletion Anomaly:*
- "Deleting one fact unintentionally deletes other important facts"
- "Removing a row loses information you wanted to keep"
- "Deletion of one piece of data causes loss of unrelated data"

**Common student mistakes:**
- Confusing update anomaly with insertion anomaly
- Giving examples instead of definitions (give partial credit if examples demonstrate understanding)
- Describing symptoms instead of the anomaly itself

---

**Question 40 (6 points):** When might a database designer choose to **denormalize** a properly normalized database? Give TWO specific scenarios where denormalization would be appropriate and explain WHY denormalization helps in each case.

**ANSWER:** (3 points per scenario)

**Grading breakdown per scenario:**
- 1.5 points for clear, specific scenario description
- 1.5 points for explanation of WHY denormalization helps
- Must provide TWO distinct scenarios

**Acceptable Scenario #1: Read-heavy reporting/analytics** (3 points)

*Scenario description (1.5 points):*
- Frequently-run reports that join many tables (5+ joins) and perform slowly
- Data warehouse or business intelligence applications
- Dashboard queries that need sub-second response times
- Monthly reports that aggregate data across multiple tables

*Why denormalization helps (1.5 points):*
- Pre-joining tables eliminates expensive JOIN operations at query time
- Reduces number of table lookups needed
- Improves query performance significantly (faster reads)
- Trade redundancy for speed in read-heavy scenarios
- Acceptable trade-off when data changes infrequently but is queried often

**Acceptable Scenario #2: Performance-critical real-time queries** (3 points)

*Scenario description (1.5 points):*
- High-traffic web application queries causing bottlenecks
- Real-time systems where query speed is critical (e.g., e-commerce product pages)
- Customer-facing queries that must return in milliseconds
- Queries hit by millions of users simultaneously

*Why denormalization helps (1.5 points):*
- Reduces query complexity and execution time
- Decreases database server load
- Improves user experience (faster page loads)
- Can handle higher concurrent user load
- Scalability improvement for read-heavy workloads

**Acceptable Scenario #3: Calculated/aggregated fields** (3 points)

*Scenario description (1.5 points):*
- Storing pre-calculated totals, counts, or aggregations
- Example: Order total stored in ORDER table instead of calculating from ORDER_DETAIL
- Example: Student GPA stored in STUDENT table instead of calculating from grades
- Expensive calculations that don't change often

*Why denormalization helps (1.5 points):*
- Avoids recalculating same value repeatedly
- Calculation once during write is cheaper than calculation on every read
- Particularly beneficial when calculation is expensive (complex aggregation, multiple joins)
- Improves read performance dramatically
- Acceptable if calculated values updated consistently (via trigger or application logic)

**Acceptable Scenario #4: Historical snapshots / Audit trails** (3 points)

*Scenario description (1.5 points):*
- Preserving data as it was at a point in time
- Example: Storing customer address on ORDER table (even though also in CUSTOMER table)
- Audit requirements to preserve exact state at time of transaction
- Versioning or historical reporting needs

*Why denormalization helps (1.5 points):*
- Maintains historical accuracy even if related data changes
- If customer moves, old orders still show where they lived when order placed
- Prevents retroactive changes from affecting historical records
- Required for compliance/audit purposes
- Provides snapshot in time rather than current state

**Acceptable Scenario #5: Materialized views / Caching** (3 points)

*Scenario description (1.5 points):*
- Creating pre-computed summary tables
- Materialized views that store query results
- Cache tables for complex analytics
- Example: Daily sales summary table

*Why denormalization helps (1.5 points):*
- Complex queries run once (during materialization) instead of repeatedly
- Users query the fast cache instead of the slow source
- Reduces load on transactional database
- Can be refreshed periodically (nightly, hourly) when acceptable
- Separates operational and analytical workloads

**Grading guidelines:**

**Full credit (3 points per scenario):**
- Specific, realistic scenario clearly described (1.5)
- Clear explanation of performance/business benefit (1.5)
- Shows understanding of normalization vs. denormalization trade-offs

**Partial credit (1.5-2.5 points per scenario):**
- Scenario described but lacking specificity (1 point)
- Explanation present but weak connection to denormalization benefit (1 point)
- Shows some understanding but missing key details

**Minimal credit (0.5-1 point per scenario):**
- Vague scenario like "for performance" without specifics (0.5)
- Correct general idea but poor articulation (0.5)

**No credit (0 points per scenario):**
- Incorrect scenario (e.g., suggesting denormalization to fix a normalized database "problem")
- No explanation of why it helps
- Answer demonstrates misunderstanding of denormalization concept

**Common student mistakes:**
- Saying "to make queries faster" without explaining specific scenario or why
- Suggesting denormalization to "fix" problems (normalization solves problems, not creates them)
- Confusing denormalization with poor database design
- Not providing TWO distinct scenarios (providing same scenario twice)

**Example of full-credit student answer:**

*Scenario 1:*
"A retail website displays product information including category name and subcategory name on every product page. This page is viewed millions of times per day. Instead of joining PRODUCT → SUBCATEGORY → CATEGORY tables on every page view, we could store CategoryName and SubcategoryName directly in the PRODUCT table."

*Why it helps:*
"This eliminates two JOIN operations on every product page view, dramatically reducing query time from ~50ms to ~5ms. Since category names change rarely (maybe once per year), the redundancy is manageable. The trade-off is worthwhile because reads outnumber writes by 1000:1."

**This answer would receive 6/6 points:**
- Specific scenario (1.5/1.5)
- Clear explanation with concrete benefits (1.5/1.5)
- Shows understanding of trade-offs (bonus: demonstrates sophisticated thinking)

---

## GRADING RUBRIC SUMMARY

| Section | Points | Notes |
|---------|--------|-------|
| **Part A (T/F)** | 19.5 | 1.5 points × 13 questions |
| **Part B (Multiple Choice)** | 42.5 | 2.5 points × 17 questions |
| **Part C (Short Answer)** | 38 | Variable points, see individual answers |
| **TOTAL** | **100** | |

### Point Distribution by Bloom's Taxonomy Level:

| Cognitive Level | Questions | Approximate Points |
|----------------|-----------|-------------------|
| **Knowledge/Recall** | ~35% of questions | ~33 points |
| **Comprehension/Application** | ~45% of questions | ~47 points |
| **Analysis/Synthesis** | ~20% of questions | ~20 points |

---

## COMMON GRADING NOTES FOR INSTRUCTORS

### Partial Credit Guidelines:

**Part A (T/F): No partial credit**
- All or nothing per question

**Part B (Multiple Choice): No partial credit**
- All or nothing per question

**Part C (Short Answer): Award generous partial credit**
- Award credit for correct reasoning even if minor details wrong
- For decomposition problems (Q37c), award partial credit per table
- For drawing problems (Q36, Q38), award credit for attempted notation
- Don't double-penalize: if student makes error in part (a), don't penalize again in part (c) if they apply that error consistently
- Focus on understanding demonstrated, not perfection

### Common Student Mistakes to Watch For:

1. **Confusing partial dependencies (2NF) with transitive dependencies (3NF)**
   - Partial = depends on part of composite key
   - Transitive = depends through intermediate non-key attribute
   - Both are "indirect dependencies" but different contexts

2. **Drawing ERD relationship lines without proper crow's feet notation**
   - Plain lines with no symbols (don't fail them, but deduct points)
   - Award partial credit if it's clear they understand the relationships

3. **Forgetting to indicate primary keys in decomposed tables**
   - Deduct 0.25 per table, but don't fail the entire question
   - If structure correct but PK not marked, give substantial partial credit

4. **Mixing up determinant and dependent in functional dependencies**
   - Determinant = left side (X in X → Y)
   - Dependent = right side (Y in X → Y)
   - This is a definitional mistake, but check if they understand the concept

5. **Not understanding that bridge tables are for M:N relationships**
   - If student creates bridge for 1:M relationship, deduct points but check overall understanding
   - May indicate confusion about cardinality, not bridge entity concept

### Time Pressure Considerations:

- Some students may not finish despite 85 minutes
- If a student clearly ran out of time (last questions blank/rushed), consider:
  - Did they demonstrate understanding in earlier questions?
  - Is the incomplete work due to lack of knowledge or lack of time?
  - For borderline passing students, consider allowing brief oral explanation of incomplete questions (instructor discretion)

### Grading Consistency:

- Grade all responses to question #34 first, then all #35, etc.
- This ensures consistent application of rubric across all students
- For drawing questions, keep reference images handy
- For ambiguous answers, give benefit of doubt if reasonable interpretation exists

### Academic Integrity Flags:

- Watch for identical errors across multiple exams (possible collaboration)
- Unusually sophisticated answers beyond course scope (possible AI use)
- Identical wording in short-answer questions
- If concerns arise, document and follow institutional academic integrity procedures

---

## EXAM STATISTICS EXPECTATIONS

For a well-prepared class with effective teaching:

**Expected score distribution:**
- Mean: 78-84 points (B to B+ range)
- Median: 80-85 points
- Standard deviation: 10-14 points

**Item difficulty:**
- Part A (T/F): Should average 80-90% correct (recognition level)
- Part B (Multiple Choice): Should average 70-80% correct (application level)
- Part C (Short Answer): Should average 65-75% correct (analysis level)

**Red flags to investigate:**
- Mean below 70: Exam may be too difficult OR teaching/preparation was insufficient
- Mean above 90: Exam may be too easy OR class is exceptionally strong
- Very high standard deviation (>18): Questions may have reliability issues
- Specific question answered correctly by <40% of students: Question may be flawed or concept needs better teaching

**Item analysis recommendations:**
- After grading, note which questions most students missed
- Review those concepts for next year's teaching
- Consider revising problematic questions
- Celebrate questions with good discrimination (good students get right, weak students miss)
