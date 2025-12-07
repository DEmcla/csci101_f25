# Module 3 Exam - Question Revisions for AI-Resistance
**Goal:** Make exam more resistant to AI cheating while maintaining 75-minute time limit
**Strategy:** Add course-specific context, require application, use scenarios

---

## REVISION 1: Question 30 (COMPLETE REPLACEMENT)

### **OLD Question 30 (4 points):**
> Describe the encapsulation process as data moves down through the layers of the TCP/IP model when sending an email. What headers are added at each layer?

### **NEW Question 30 (4 points) - IPv4 Subnet Calculation:**

**Question Text:**
```
**Turn in on paper. Show all work.**

Consider the following two devices on a network:

Device A: IP address 192.168.10.75/26
Device B: IP address 192.168.10.135/26

a) Are these two devices on the same subnet or different subnets? (1 point)

b) Show your work by determining the network address for each device. (2 points)

c) What is the subnet mask in dotted decimal notation for this network? (1 point)
```

**Grading Rubric:**
```
a) 1 point - Correct answer (Different subnets)

b) 2 points - Work shown:
   • Convert /26 to subnet mask: 255.255.255.192 (0.5 pt)
   • Device A network address: 192.168.10.64 (0.75 pt)
   • Device B network address: 192.168.10.128 (0.75 pt)

c) 1 point - 255.255.255.192

PARTIAL CREDIT:
- Award points for methodology even if arithmetic errors
- Must show work for parts b and c
```

**Why this is better:**
- ✅ On paper = can't copy-paste
- ✅ "Show your work" requirement
- ✅ Tests understanding, not memorization
- ✅ Simpler than Q33 (only 2 IPs, not 4 subnets)
- ✅ Still appropriate difficulty for CSCI 101

---

## REVISION 2: Question 26 → Add Course Context

### **OLD Question 26 (4 points):**
> Explain the three-way handshake process used by TCP to establish a connection. Include the names of the three messages exchanged.

### **NEW Question 26 (4 points):**

**Question Text:**
```
In this module, we discussed how TCP establishes reliable connections before data transfer.

a) List the three messages exchanged during TCP's three-way handshake in order. (1.5 points)

b) Explain why this process is called a "handshake" - what is being agreed upon between the two devices? (1.5 points)

c) What would happen if the third message (ACK) was lost due to network congestion? (1 point)
```

**Why this is better:**
- ✅ Part (c) requires application/critical thinking
- ✅ AI will give generic answers; students need to think through scenarios
- ✅ "What would happen if..." questions test understanding

---

## REVISION 3: Question 27 → Scenario-Based Application

### **OLD Question 27 (5 points):**
> Compare and contrast TCP and UDP. Describe at least two key differences and give an example application that would use each protocol.

### **NEW Question 27 (5 points):**

**Question Text:**
```
You're helping design a new application with these requirements:

**Feature 1:** A live video stream that broadcasts a lecturer speaking to 500 students
**Feature 2:** A chat system where students can ask questions to the lecturer

a) Which transport protocol (TCP or UDP) would you recommend for Feature 1 (video stream)? Explain your reasoning. (2 points)

b) Which transport protocol would you recommend for Feature 2 (chat)? Explain your reasoning. (2 points)

c) What trade-off exists when choosing UDP for video streaming? (1 point)
```

**Why this is better:**
- ✅ Scenario-based = requires application
- ✅ AI gives theoretical answers; this requires practical decisions
- ✅ Tests understanding of when to use each protocol
- ✅ More engaging than "compare and contrast"

---

## REVISION 4: Question 31 → Add Personal Context

### **OLD Question 31 (5 points):**
> Explain the concept of packet switching and describe why it is more efficient than circuit switching for computer data communications. Use a specific example in your explanation.

### **NEW Question 31 (4 points):**

**Question Text:**
```
a) In 2-3 sentences, explain what packet switching is and how it differs from circuit switching. (2 points)

b) Imagine you're at home streaming a Netflix movie while also browsing social media. Using this personal scenario, explain why packet switching is better suited for this type of internet usage than circuit switching would be. (2 points)
```

**Why this is better:**
- ✅ Reduced from 5 to 4 points (helps reach 100 point total)
- ✅ Personal scenario forces application
- ✅ Shorter answers = less time to AI-cheat
- ✅ "Using this personal scenario" = harder for AI to give generic answer

---

## REVISION 5: Question 28 → Add Critique Element

### **OLD Question 28 (3 points):**
> Explain the main purpose and benefits of using a layered architecture (like the OSI or TCP/IP model) in network design. Why don't we just have one large, monolithic protocol instead?

### **NEW Question 28 (3 points):**

**Question Text:**
```
A student says: "Network layering is just unnecessary complexity. A single monolithic protocol would be simpler and faster."

Respond to this student by:
a) Identifying one reason why they might think this (1 point)
b) Explaining two benefits of layering that prove why this claim is incorrect (2 points)
```

**Why this is better:**
- ✅ Critique format = requires analysis, not just recall
- ✅ "Respond to this student" = more engaging
- ✅ Part (a) requires understanding the other perspective
- ✅ AI gives generic lists; this requires argumentation

---

## REVISION 6: Question 29 → Add "Most Important" Ranking

### **OLD Question 29 (5 points):**
> Explain why IPv6 was developed and describe at least three improvements it offers over IPv4.

### **NEW Question 29 (5 points):**

**Question Text:**
```
a) What was the primary problem that drove the development of IPv6? (1 point)

b) List three improvements that IPv6 offers over IPv4. (1.5 points)

c) Of the three improvements you listed, which do you think is MOST important for the future of the internet? Explain your reasoning in 2-3 sentences. (2.5 points)
```

**Why this is better:**
- ✅ Part (c) requires judgment and justification
- ✅ "Which is most important" = no single right answer
- ✅ AI will hedge; students must take a position
- ✅ Tests deeper understanding

---

## REVISION 7: Question 14 → Add Real-World Context

### **OLD Question 14 (3 points):**
> What is the primary advantage of packet switching over circuit switching for computer data communications?
> A) Guaranteed bandwidth for each connection
> B) Efficient use of network resources by sharing infrastructure
> C) Simpler network equipment and protocols
> D) Lower latency for all types of traffic

### **NEW Question 14 (3 points):**

**Question Text:**
```
You're video chatting with a friend when you pause to check your email for 30 seconds, then resume the conversation.

What advantage of packet switching makes this scenario more efficient than circuit switching?

A) Packet switching reserves a dedicated path for your video call
B) Packet switching allows other users to share network resources during your 30-second pause
C) Packet switching guarantees your video quality stays constant
D) Packet switching prevents your email from interfering with your video call
```

**Why this is better:**
- ✅ Concrete scenario instead of abstract concept
- ✅ Tests understanding in context
- ✅ Distractors are more realistic

---

## REVISION 8: Question 37 (CLI) → Add Troubleshooting Scenario

### **OLD Question 37 (3 points):**
> Explain the difference between the tracert (Windows) / traceroute (Mac/Linux) command and the ping command. When would you use tracert/traceroute instead of ping?

### **NEW Question 37 (3 points):**

**Question Text:**
```
You're helping a friend troubleshoot their internet connection. You run `ping google.com` and notice:
- Some packets are getting through (60% success rate)
- Response times vary wildly (20ms to 500ms)
- Several packets are lost

a) Should you run tracert/traceroute next? Why or why not? (2 points)

b) What information would tracert/traceroute show you that ping doesn't? (1 point)
```

**Why this is better:**
- ✅ Real troubleshooting scenario
- ✅ Tests practical application
- ✅ "Should you" = requires decision-making
- ✅ Connects multiple concepts

---

## REVISION 9: Question 20 → Scenario Instead of Definition

### **OLD Question 20 (3 points):**
> What does NAT (Network Address Translation) primarily accomplish?
> A) Encrypts all network traffic for security
> B) Allows multiple devices to share a single public IP address
> C) Converts domain names to IP addresses
> D) Increases network bandwidth

### **NEW Question 20 (3 points):**

**Question Text:**
```
Your home has 5 devices (laptop, phone, tablet, smart TV, gaming console) all connected to Wi-Fi. Your ISP only gave you ONE public IP address (e.g., 73.45.123.67).

How do all 5 devices access the internet simultaneously with just one public IP?

A) Each device takes turns using the public IP address
B) The router uses NAT to translate between private IPs (like 192.168.1.x) and the single public IP
C) The ISP automatically assigns temporary public IPs when needed
D) Devices share bandwidth by splitting the IP address into subnets
```

**Why this is better:**
- ✅ Personal, relatable scenario
- ✅ Tests understanding, not memorization
- ✅ Context makes the "why" clear

---

## REVISION 10: Add ONE NEW Question (Optional - builds context)

### **NEW Question 38 (2 points bonus or replace a weak question):**

**Question Text:**
```
In one sentence, explain the difference between a switch and a router to someone who has never taken a networking class.
```

**Why this is valuable:**
- ✅ "Explain to someone who..." = tests true understanding
- ✅ One sentence = can't AI a paragraph and copy
- ✅ Forces simplification (Feynman technique)
- ✅ Quick to grade (2 min reading, max)

**Sample acceptable answers:**
- "A switch connects devices within one network; a router connects different networks together."
- "Switches let devices on the same network talk to each other; routers let you access the internet."

---

## SUMMARY OF CHANGES

| Question | Old Type | New Type | AI Resistance Gain |
|----------|----------|----------|-------------------|
| Q30 | Generic explanation | **Paper calculation** | ⭐⭐⭐⭐⭐ |
| Q32 | IP classification | **Turned in on paper** | ⭐⭐⭐⭐⭐ |
| Q26 | List steps | Add "what if" scenario | ⭐⭐⭐ |
| Q27 | Compare/contrast | Application scenario | ⭐⭐⭐⭐ |
| Q31 | Generic explanation | Personal scenario | ⭐⭐⭐ |
| Q28 | List benefits | Critique argument | ⭐⭐⭐⭐ |
| Q29 | List improvements | Rank by importance | ⭐⭐⭐ |
| Q14 | Abstract concept | Real-world scenario | ⭐⭐ |
| Q37 | Explain difference | Troubleshooting decision | ⭐⭐⭐⭐ |
| Q20 | Definition | Personal scenario | ⭐⭐ |

---

## POINT ADJUSTMENTS TO REACH 100 POINTS

**Current total:** 110 points

**Adjustments needed:** -10 points

**Recommended:**
- Q31: Reduced 5 → 4 points (-1)
- Remove Q33 entirely (-6 points)
- Q30: New version is 4 points (same as old)
- Adjust one 3-point MC to 2 points (-1)
- Or adjust two MC from 3 → 2.5 points each (-1)

**New total:** 100 points

---

## TIME IMPACT ANALYSIS

**Do these revisions slow down cheating?**

| Revision | Cheating Time Impact |
|----------|---------------------|
| Paper questions (Q30, Q32) | +30-45 sec (can't copy-paste) |
| Scenario questions | +15-20 sec (need to read carefully) |
| "Explain to someone" format | +10 sec (can't use generic AI answer) |
| Critique/ranking questions | +20 sec (AI hedges, student must decide) |

**Net effect:** Strategic cheaters now need **~70 seconds per revised question** (vs. 60 before)

**Full exam cheat time estimate:** ~48-52 minutes (was ~41 minutes)

**Result:** Even less time buffer for cheaters, more advantage to prepared students

---

## IMPLEMENTATION CHECKLIST

- [ ] Replace Q30 with subnet calculation (mark as "turn in on paper")
- [ ] Mark Q32 as "turn in on paper"
- [ ] Update Q26, Q27, Q28, Q29, Q31, Q37 with scenario/application versions
- [ ] Update Q14, Q20 with scenario-based versions
- [ ] Remove Q33 (subnetting) entirely
- [ ] Adjust points to total 100
- [ ] Update exam instructions to note paper submission for Q30, Q32
- [ ] Add time management guidance to match Module 2

**Estimated revision time:** 30-45 minutes to update HTML
