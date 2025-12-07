# Module 3 Exam Review & Recommendations
**Reviewer Analysis:** Comparison with Module 2 Exam Standards
**Context:** First-year CS survey course, 75 minutes, open book/notes, no AI

---

## EXECUTIVE SUMMARY

**Overall Assessment:** The exam has **1 critical issue** (Q33 subnetting) and several questions that may be too advanced for a CSCI 101 survey course. Recommend reducing complexity and aligning difficulty with Module 2.

**Key Stats:**
- **Module 2:** 100 points, 35 questions, 75 minutes
- **Module 3:** 110 points, 37 questions, 75 minutes ⚠️ *10% more points in same time*

---

## CRITICAL ISSUES (Must Fix)

### 🔴 **ISSUE #1: Question 33 - IPv4 Subnetting Problem (6 points)**

**Problem:** This is a **Networking course-level question**, NOT appropriate for CSCI 101 survey course.

**Why it's too hard:**
- Requires binary math and subnet calculations
- 5 sub-parts (a-e) in a timed exam
- Concepts like "borrowing bits," CIDR notation, calculating usable hosts
- This is typically covered in CSCI 3xx Networking courses, not intro CS

**Module 2 Comparison:** Module 2 had NO calculation-heavy problems of this complexity

**Recommendation:**
- **REMOVE entirely** OR
- **Replace with conceptual question:** "Explain what subnetting is and why organizations use it" (2-3 points max)

---

### ⚠️ **ISSUE #2: Point Distribution Too Heavy**

**Problem:** 110 points in 75 minutes vs. Module 2's 100 points

**Time pressure:**
- Students need ~41 seconds per point (vs. 45 seconds in Module 2)
- Part 3 short answers total 35 points with complex multi-part questions
- Question 33 alone is 6 points with 5 sub-questions

**Recommendation:**
- **Reduce to 100 points total** (match Module 2)
- Remove or simplify Question 33 (-6 points)
- Consider reducing Question 31 from 5 to 4 points

---

## MODERATE ISSUES (Consider Revising)

### 📝 **Question 19: SLAAC (IPv6 Stateless Address Autoconfiguration)**

**Current:** Multiple choice about IPv6 autoconfiguration

**Issue:**
- SLAAC is pretty advanced for intro students
- IPv6 is important but this specific mechanism may be too detailed

**Recommendation:** KEEP (it's multiple choice) but consider if students have been adequately prepared

---

### 📝 **Question 17: IPv6 Tunneling Mechanisms**

**Current:** Asks about tunneling with deprecated technology (6to4) mentioned in answer

**Issue:**
- Mentions "6to4, though now deprecated" - confusing for students
- Tunneling concepts may be too networking-specific

**Recommendation:**
- **Revise answer** to remove deprecated technology reference
- OR **Simplify** to: "Which mechanism allows IPv6 and IPv4 to coexist during transition?"
  - Options: A) NAT, B) Dual Stack, C) Subnetting, D) DHCP
  - Answer: B) Dual Stack

---

### 📝 **Question 31: Packet Switching Explanation (5 points)**

**Current:** Requires defining packet switching, circuit switching, efficiency advantages, AND example

**Issue:**
- 5 points for a very detailed explanation in timed exam
- Students need to synthesize a lot of information

**Module 2 Comparison:** Module 2's highest short answer was 6 points (ERD diagram - visual task)

**Recommendation:**
- **Reduce to 4 points** (less demanding rubric)
- OR **Simplify rubric:** Remove requirement to define both switching types, focus on packet switching benefits

---

### 📝 **Question 32: Private/Public IP Classification (3 points)**

**Current:** Classify 3 addresses + explain NAT

**Issue:**
- Rubric says "0.33 each" which is awkward and hard to grade
- Mixing classification with NAT explanation makes grading unclear

**Recommendation:**
**Clarify rubric:**
```
• 0.5 points for each correct classification (1.5 total)
• 1.5 points for explaining why NAT is required
```

---

## MINOR CLARITY IMPROVEMENTS

### Question 4 (True/False)
**Current:** "TCP provides connectionless, unreliable data transmission while UDP provides connection-oriented, reliable data transmission."

**Issue:** This is a "reversal trap" question - could be clearer

**Recommendation:** KEEP as-is (tests careful reading) OR rephrase positively:
"TCP provides connection-oriented, reliable data transmission."

---

### Question 24 (Multiple Choice)
**Current:** Shows IPv6 address with "::" compression notation

**Issue:** Students may not have learned :: compression syntax

**Recommendation:** Ensure this was taught, or provide note: "Note: :: represents consecutive groups of zeros"

---

## MISSING ELEMENTS (Compared to Module 2)

### ⚠️ **No Time Management Guidance**

**Module 2 included:**
```
Time management suggestion:
- Part A: 10 minutes
- Part B: 28 minutes
- Part C: 32 minutes
- Review: 5 minutes
```

**Recommendation:** Add time guidance:
```
Time management suggestion:
- Part 1 (T/F): 8-10 minutes
- Part 2 (MC): 18-20 minutes
- Part 3 (Short Answer): 30-35 minutes
- Part 4 (CLI): 10-12 minutes
- Review: 5 minutes
```

---

### ⚠️ **Instructions Could Be Clearer**

**Module 2 was very explicit:**
- "Write all answers clearly and legibly"
- "For diagram questions, you may hand-draw and upload"
- "You may NOT use AI tools (ChatGPT, Claude, etc.)"

**Recommendation:** Match Module 2's explicit instruction style

---

## QUESTIONS THAT ARE GOOD ✅

These questions are **appropriate, clear, and well-calibrated** for CSCI 101:

**True/False:**
- Q1-Q10: All appropriate difficulty

**Multiple Choice:**
- Q11 (OSI Network Layer function) ✅
- Q12 (Router operates at Layer 3) ✅
- Q14 (Packet switching advantages) ✅
- Q15 (TCP three-way handshake) ✅
- Q20 (NAT purpose) ✅
- Q22 (DNS function) ✅
- Q34-Q37 (CLI questions) ✅ **Well-designed, practical**

**Short Answer:**
- Q26 (TCP three-way handshake) ✅
- Q27 (TCP vs UDP) ✅
- Q28 (Layered architecture benefits) ✅
- Q29 (Why IPv6 was developed) ✅
- Q30 (Encapsulation process) ✅

---

## RECOMMENDED CHANGES SUMMARY

### **MUST DO:**
1. ❌ **REMOVE Question 33** (subnetting calculation) - Too advanced for CSCI 101
2. ✏️ **Add time management guidance** to instructions
3. ✏️ **Reduce total to 100 points** (remove Q33 = -6 points, adjust one 5-pt question to 4 pts = -1 point)

### **SHOULD DO:**
4. ✏️ **Simplify Question 17** (IPv6 transition) - Remove tunneling reference
5. ✏️ **Clarify Question 32 rubric** (0.5 points instead of 0.33)
6. ✏️ **Review Question 31** - Consider reducing from 5 to 4 points

### **NICE TO HAVE:**
7. ✏️ Add note about :: notation in Q24 if not taught
8. ✏️ Make instructions match Module 2's explicit style

---

## ALIGNMENT WITH LEARNING OBJECTIVES

**Good coverage of:**
- ✅ OSI and TCP/IP models
- ✅ Network protocols (TCP, UDP, IP)
- ✅ IPv4 vs IPv6 concepts
- ✅ Network diagnostics (CLI tools)
- ✅ DNS, NAT, basic networking

**Over-emphasis on:**
- ⚠️ IPv6 details (Q17, Q19, Q24, Q29) - 4 questions on IPv6
- ⚠️ Advanced subnetting (Q33) - Not appropriate for level

**Could add:**
- Consider 1-2 questions on network security basics (if covered in module)
- Consider question on network topologies (if covered)

---

## FINAL RECOMMENDATION

**Overall Grade:** B+ (Good exam, but needs adjustments)

**Action Items for Instructor:**

1. **Immediate:** Remove or radically simplify Question 33
2. **Before publishing:** Add time management guidance
3. **Consider:** Reducing point total to 100 to match Module 2
4. **Review:** Ensure all IPv6 concepts tested were adequately taught

**After fixes, this will be an A-level exam** appropriate for CSCI 101.

---

## REVISED POINT DISTRIBUTION (Recommended)

```
Part 1: True/False     10 questions × 2 pts  = 20 points  (8-10 min)
Part 2: Multiple Choice 15 questions × 2.5 pts = 37.5 points* (18-20 min)
Part 3: Short Answer    7 questions (varying)  = 32.5 points (30-35 min)
Part 4: CLI Questions   4 questions (varying)  = 10 points   (10-12 min)
                                        TOTAL = 100 points    (75 min)

*Round 37.5 to 38, or adjust one question to make exactly 100
```

**Changes from current:**
- Remove Q33 (subnetting) = -6 points
- Reduce one 5-point question to 4 points = -1 point
- Reduce MC from 3 pts each to 2.5 pts each = -7.5 points
- Total reduction: -14.5 points (110 → ~95.5, adjust to 100)

OR keep current structure but **definitely remove Q33**.
