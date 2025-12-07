# Module 2 Exam: Comprehensive Review Analysis

## 1. TECHNICAL ACCURACY REVIEW

### ✅ Technically Correct Questions (38/40)

Most questions are technically accurate and align with standard database theory.

### ⚠️ Issues Requiring Attention (2 items)

#### **Issue #1: Question 18 - Ambiguous Answer**
**Question:** Given the functional dependency `{OrderID, ProductID} → Quantity`, what type of key is `{OrderID, ProductID}`?

**Current Answer:** c) Composite primary key

**Problem:**
- The functional dependency notation alone doesn't prove it's a PRIMARY key
- It could be a composite candidate key that isn't selected as primary
- The question should either:
  - State "this is the primary key" explicitly, OR
  - Change answer to d) "Candidate key" (more technically precise)

**Recommendation:** Revise question to say "Given a table with primary key {OrderID, ProductID}..."

#### **Issue #2: Question 35 - Unclear Second Violation**
**Question:** Identify TWO specific violations of 1NF in LIBRARY_CHECKOUT table

**Current Answer:**
- Violation #1: BookAuthors contains multiple values ✅ (Clear and correct)
- Violation #2: "Possible repeating groups if multiple books checked out" ⚠️ (Speculative)

**Problem:**
- The second violation requires students to imagine a scenario not shown in the data
- Students see only ONE row of sample data
- They can't determine from the schema whether repeating groups exist

**Recommendation:**
- **Option A:** Show actual repeating groups in the table (BookISBN1, BookISBN2 columns)
- **Option B:** Ask for only ONE violation and make it worth 5 points (simpler fix)
- **Option C:** Show multiple rows where patron info repeats, making the violation visible

---

## 2. STUDENT PERSPECTIVE: DIFFICULTY & TIME CONSTRAINTS

### Overall Assessment: **SLIGHTLY TOO TIGHT** for average prepared students

### Time Analysis by Section

#### **Part A: True/False (15 questions, 12 minutes suggested)**
- **Actual time needed:** 10-15 minutes
- **Per question:** 48 seconds average
- **Assessment:** ✅ **REASONABLE**
  - Straightforward recognition questions
  - Open book helps (can verify definitions)
  - No calculations or drawing required

#### **Part B: Multiple Choice (18 questions, 30 minutes suggested)**
- **Actual time needed:** 30-40 minutes for average student
- **Per question:** 100 seconds (1:40) average suggested, but realistically need 120-133 seconds (2:00-2:13)
- **Assessment:** ⚠️ **SLIGHTLY TIGHT**

**Why it's tight:**
- Questions 22, 26, 30 require careful analysis of functional dependencies
- Questions require reading tables, identifying keys, and reasoning through scenarios
- Even with open notes, students need time to:
  - Read the question carefully
  - Analyze the table structure
  - Recall/find relevant concept in notes
  - Eliminate wrong answers
  - Select and mark answer

**Breakdown by difficulty:**
- **Quick questions (8):** 16, 17, 19, 23, 24, 28, 29, 31 — 60 seconds each = 8 minutes
- **Medium questions (7):** 18, 20, 21, 25, 27, 32, 33 — 90 seconds each = 10.5 minutes
- **Complex questions (3):** 22, 26, 30 (require table analysis) — 180 seconds each = 9 minutes
- **TOTAL REALISTIC:** 27.5 minutes minimum for strong students, 35+ for average

#### **Part C: Short Answer (7 questions, 30 minutes suggested)**
- **Actual time needed:** 35-45 minutes for average student
- **Assessment:** ⚠️ **TOO TIGHT**

**Time breakdown by question:**
| Question | Points | Suggested Time | Realistic Time | Reason |
|----------|--------|----------------|----------------|---------|
| Q34 (PK/FK) | 4 | 3 min | 3-4 min | Straightforward definitions |
| Q35 (1NF violations) | 5 | 4 min | 5-7 min | Need to analyze table, explain TWO violations |
| Q36 (Draw notation) | 5 | 4 min | 4-5 min | Drawing takes time, must be precise |
| Q37 (3NF decompose) | 6 | 6 min | 8-10 min | **Most complex**: analyze, explain, decompose |
| Q38 (Draw ERD) | 5 | 5 min | 6-8 min | Drawing takes time, need three entities + relationships |
| Q39 (3 anomalies) | 3.5 | 3 min | 3-4 min | Listing is quick, but need good descriptions |
| Q40 (Denormalize) | 4 | 5 min | 4-5 min | Need TWO scenarios with explanations |
| **TOTAL** | **32.5** | **30 min** | **33-43 min** | Average student: 38 minutes |

**Why Part C is too tight:**
- Q37 (decomposition) is complex: analyze FDs → identify violation → explain anomaly → draw two tables
- Q38 (ERD) requires careful drawing of three entities with proper notation
- Students writing by hand are slower than typing
- Nervous students make mistakes and need time to correct/redraw

#### **Review Time: 3 minutes suggested**
- **Assessment:** ❌ **INSUFFICIENT**
- Most students will have 0-1 minute for review, if any
- Anxious students will run out of time

### **Overall Time Assessment:**

| Section | Suggested | Realistic Minimum | Realistic Average |
|---------|-----------|-------------------|-------------------|
| Part A | 12 min | 10 min | 13 min |
| Part B | 30 min | 28 min | 35 min |
| Part C | 30 min | 33 min | 40 min |
| Review | 3 min | 2 min | 0-1 min |
| **TOTAL** | **75 min** | **73 min** | **88-89 min** |

**Conclusion:** Average prepared student needs **13-15 minutes more than allocated**.

### Difficulty Assessment by Bloom's Taxonomy

#### **Knowledge/Recall (Easy)** — 40% of exam
- Part A: Questions 1, 2, 3, 5, 8, 9, 10, 12, 13, 15
- Part B: Questions 16, 17, 19, 23, 24, 28, 31
- Part C: Question 34, 39
- **Assessment:** Appropriate for 100-level course

#### **Comprehension/Application (Medium)** — 45% of exam
- Part A: Questions 4, 6, 7, 11, 14
- Part B: Questions 18, 20, 21, 25, 27, 29, 32, 33
- Part C: Questions 35, 36, 40
- **Assessment:** Appropriate, well-scaffolded

#### **Analysis/Synthesis (Hard)** — 15% of exam
- Part B: Questions 22, 26, 30
- Part C: Questions 37, 38
- **Assessment:** Appropriate amount of challenge, but time-consuming

### Difficulty Recommendations

**Current difficulty is APPROPRIATE** for 100-level, but **time allocation is the problem**.

**Stress factors for average student:**
1. Drawing/diagramming takes longer than anticipated (Q36, Q38)
2. Analyzing functional dependencies under time pressure (Q22, Q26, Q30, Q37)
3. Writing explanations by hand (all Part C)
4. Fear of running out of time creates anxiety → slower performance
5. Open book/note helps but takes time to find information

---

## 3. PEDAGOGICAL PERSPECTIVE

### Constructive Alignment: ✅ **EXCELLENT**

**Learning Objectives → Assessment Alignment:**

The exam directly tests what was taught in the module materials:

| Learning Objective | Assessment Coverage | Quality |
|-------------------|---------------------|---------|
| Identify database anomalies | Q15, Q37b, Q39 | ✅ Excellent |
| Define functional dependencies | Q5, Q20, Q24, Q37 | ✅ Excellent |
| Determine appropriate keys | Q2, Q18, Q34, Q37c, Q38 | ✅ Excellent |
| Recognize 1NF/2NF/3NF violations | Q4, Q7, Q9, Q19, Q22, Q26, Q35, Q37a | ✅ Excellent |
| Decompose tables | Q30, Q37c | ✅ Excellent |
| Understand ERDs and cardinality | Q1, Q3, Q13, Q21, Q27, Q29, Q31, Q36, Q38 | ✅ Excellent |
| Bridge entities | Q6, Q11, Q21, Q38 | ✅ Excellent |
| Explain denormalization | Q8, Q25, Q40 | ✅ Excellent |
| Light coverage BCNF+ | Q14, Q28 | ✅ Appropriate (not overemphasized) |

**Assessment:** The exam perfectly reflects the course content and emphasis.

### Cognitive Load Analysis: ⚠️ **MODERATE CONCERNS**

#### **Positive Aspects:**
1. **Scaffolding:** Questions progress from simple (Part A) to complex (Part C) ✅
2. **Chunking:** Exam divided into clear sections with different cognitive demands ✅
3. **Open book/note:** Reduces memorization burden, focuses on application ✅
4. **Variety:** T/F, MC, and short answer engage different cognitive processes ✅

#### **Concerns:**
1. **Working Memory Overload in Part B:**
   - Questions 22, 26, 30 require holding table structure, FDs, and normal form rules in working memory simultaneously
   - Under time pressure, this is cognitively demanding
   - **Mitigation:** Students can refer to notes, but adds time

2. **Drawing Under Time Pressure (Part C):**
   - Q36 and Q38 require precision and visual accuracy
   - Mistakes require erasing/redrawing → time loss → anxiety
   - Hand-drawing crow's feet notation under time pressure is stressful
   - **Concern:** Tests drawing speed as much as understanding

3. **Cumulative Fatigue:**
   - By minute 60-65, students are mentally fatigued
   - Part C requires highest cognitive effort but comes at the end
   - **Risk:** Capable students may perform poorly due to fatigue, not lack of knowledge

### Assessment Validity: ✅ **STRONG**

#### **Content Validity:** ✅ Excellent
- Comprehensive coverage of all module topics
- Appropriate balance: heavy on 1NF-3NF, light on BCNF+
- Representative sample of the domain

#### **Construct Validity:** ✅ Excellent
- Questions test conceptual understanding, not just memorization
- Requires application (decomposition, diagram drawing)
- Distinguishes between superficial and deep understanding

#### **Face Validity:** ✅ Excellent
- Questions clearly relate to database design
- Students will perceive exam as fair and relevant
- Professional appearance and clear instructions

### Assessment Reliability Concerns: ⚠️ **MODERATE**

#### **Potential Reliability Issues:**

1. **Question 35 (1NF violations):**
   - Second violation is ambiguous
   - Two equally-prepared students might get different scores based on interpretation
   - **Impact:** Reduces inter-rater reliability

2. **Question 36 (Drawing crow's feet):**
   - What counts as "close enough" for partial credit?
   - Grading rubric says "deduct 0.5 if close but minor errors"
   - "Close" is subjective → inconsistent grading possible
   - **Recommendation:** Provide visual examples in rubric

3. **Question 38 (ERD Drawing):**
   - "Accept reasonable variations in notation as long as relationships are correct"
   - This is good, but needs more specificity
   - Does entity box shape matter? Do line styles matter?
   - **Recommendation:** Show example acceptable variations in answer key

4. **Time Pressure Variability:**
   - Students who work quickly have advantage disproportionate to knowledge
   - Slower, thoughtful students may be penalized unfairly
   - **Impact:** Exam may measure speed as much as mastery

### Formative vs. Summative Balance: ⚠️ **CONCERNS**

**Current exam is purely summative** (measures final achievement).

**Missing formative elements:**
- No low-stakes check-in during exam ("Are you managing time well?")
- No scaffolded support for complex questions
- No opportunity for students to demonstrate partial understanding without penalty

**Pedagogical concern:**
- Students who "almost get it" score similarly to students who "don't get it at all"
- This is particularly true for Q37 (worth 6 points, all-or-nothing feel despite rubric)

**Recommendation:** Consider adding more granular partial credit opportunities

### Universal Design for Learning (UDL): ⚠️ **NEEDS IMPROVEMENT**

#### **Multiple Means of Representation:** ⚠️ Partial
- ✅ Text-based questions accessible
- ✅ Visual elements (tables, notation) support visual learners
- ❌ No accommodations mentioned for students with visual processing difficulties
- ❌ Font size, spacing not specified (readability concerns)

#### **Multiple Means of Action/Expression:** ❌ Limited
- ✅ Variety of response types (T/F, MC, short answer)
- ❌ All Part C requires hand-drawing (difficult for students with fine motor challenges)
- ❌ No option to verbally describe crow's feet notation or type responses
- ❌ No choice in how to demonstrate understanding (all students must draw ERDs)

#### **Multiple Means of Engagement:** ⚠️ Partial
- ✅ Questions vary in difficulty (provides challenge for all levels)
- ⚠️ High-stakes, timed nature may disadvantage students with test anxiety
- ❌ No low-entry, high-ceiling problems (all students do same questions)

**Recommendation:**
- Consider alternative response formats (e.g., "describe in words OR draw")
- Provide larger answer spaces for students who need to write bigger
- Consider extended time as default (85-90 minutes) rather than accommodation

### Cognitive Justice & Equity Considerations

#### **Advantages of Current Design:**
1. **Open book/note** — Reduces advantage for students with strong memorization (more equitable)
2. **Clear instructions** — Reduces confusion, helps ELL students
3. **Points clearly marked** — Students can strategically allocate time

#### **Potential Equity Issues:**

1. **Drawing Requirements (Q36, Q38):**
   - Assumes all students can draw precisely and quickly
   - Disadvantages: students with dysgraphia, fine motor challenges, visual-spatial difficulties
   - **Not testing:** understanding (what we want)
   - **Actually testing:** drawing speed and precision (not what we want)
   - **Recommendation:** "You may draw OR describe in words with clear labels"

2. **Reading Speed & Volume:**
   - Exam requires fast reading (especially Part B with 18 scenarios)
   - Disadvantages: ELL students, students with dyslexia, slow processors
   - Open book doesn't fully mitigate if reading the *exam* is the bottleneck
   - **Recommendation:** Extended time should be generous (time + 50%, not just +20%)

3. **Cultural Assumptions:**
   - Examples (library checkout, university enrollment) assume familiarity with US academic systems
   - Generally fine, but worth noting
   - Students from different educational backgrounds may need extra cognitive load to parse context

4. **Test Anxiety:**
   - Timed exams disadvantage students with anxiety disorders disproportionately
   - 75 minutes with no buffer creates "time panic" — performance tanks
   - **Recommendation:** Build in buffer (83-90 minutes) for ALL students

---

## 4. OVERALL RECOMMENDATIONS

### 🔴 **Critical Issues (Must Fix):**

1. **Question 18:** Clarify that {OrderID, ProductID} is stated to be the primary key
2. **Question 35:** Revise to show clearer second 1NF violation OR ask for only one violation
3. **Time Allocation:** Increase to 85-90 minutes OR reduce content

### 🟡 **Important Issues (Strongly Recommend Fixing):**

4. **Part C Drawing Questions:** Add option "draw OR describe in words"
5. **Review Time:** Actually allocate 5-8 minutes by reducing content slightly
6. **Answer Key:** Add visual examples for Q36 and Q38 to improve grading consistency

### 🟢 **Enhancement Suggestions (Nice to Have):**

7. **Question Distribution:** Consider moving 1-2 MC questions to T/F to save time
8. **Partial Credit:** Make Q37c worth 3 points (1.5 per table) instead of 2 to allow finer grading
9. **Rubric Detail:** For Q38, specify what notation variations are acceptable

---

## 5. SPECIFIC REVISION OPTIONS

### **Option A: Keep 40 Questions, Extend Time**
- Change exam to **90 minutes**
- No content changes needed
- Pros: Comprehensive coverage maintained, students less stressed
- Cons: Longer class period needed, potential scheduling issues

### **Option B: Reduce to 35 Questions, Keep 75 Minutes**
- Remove 3 multiple choice questions (suggest: #18, #25, #33)
- Remove 2 true/false questions (suggest: #8, #14)
- Adjust point totals to still reach 100 points
- Pros: Time becomes reasonable, less rushed
- Cons: Slightly reduced coverage

### **Option C: Hybrid Approach (RECOMMENDED)**
- **Extend time to 82-85 minutes** (split the difference)
- **Remove 2-3 lowest-value questions:**
  - Remove Q33 (DateOfBirth attribute type — least important)
  - Remove Q8 or Q14 (denormalization definition already tested in Q25 and Q40)
- **Adjust Q36 or Q38** to allow verbal description alternative
- **Result:** Manageable time, maintains coverage, more equitable

---

## 6. SUMMARY SCORES

| Criterion | Score | Notes |
|-----------|-------|-------|
| **Technical Accuracy** | 9.5/10 | Two minor issues (Q18, Q35) |
| **Content Coverage** | 10/10 | Excellent alignment with module |
| **Difficulty Level** | 9/10 | Appropriate for 100-level |
| **Time Feasibility** | 6.5/10 | Too tight for average student |
| **Clarity** | 9/10 | Clear instructions, minor ambiguities |
| **Equity/UDL** | 6.5/10 | Drawing requirements problematic |
| **Pedagogical Soundness** | 8.5/10 | Strong construct validity, some reliability concerns |
| **Grading Practicality** | 8/10 | Detailed rubric, but some subjectivity in drawings |

### **Overall Assessment: 8.25/10 — STRONG EXAM with room for improvement**

**Strengths:**
- Comprehensive, well-aligned with learning objectives
- Good mix of question types and difficulty levels
- Strong pedagogical foundation
- Excellent content validity

**Weaknesses:**
- Time constraints too tight for average student (primary issue)
- Drawing requirements create equity concerns
- Minor technical ambiguities (Q18, Q35)
- Limited UDL implementation

**Recommendation:** **Implement Option C (Hybrid Approach)** to create an excellent, equitable exam that accurately assesses student learning without unnecessary time pressure.
