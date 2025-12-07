# CSCI 101: Module 3 Study Guide
## Computer Networking Foundations & Command Line Mastery

---

## START HERE: Which Study Path Is Right for You?

**Answer these questions to find your path:**

### Are you prepared for this exam?

**Path A: Well-Prepared Student**
- Completed all assigned readings and tutorials
- Attended all lectures and took notes
- Completed CLI lab exercises
- Understand most concepts, just need review

**Use: "Quick Review Track" (30-60 minutes)** then target specific weak areas

---

**Path B: Average Student**
- Did most readings and assignments
- Attended most classes
- Some concepts are fuzzy
- Need structured review

**Use: "3-Hour Crash Course"** (recommended)

---

**Path C: Struggling Student**
- Missed several classes or readings
- Didn't complete all assignments
- Many concepts unclear
- Need to learn from scratch

**Use: "Emergency Rescue Guide"** (Start below, then move to 3-Hour Crash Course)

---

## EMERGENCY RESCUE GUIDE (For Path C Students)

*Start here if you missed most of the coursework. This gives you the absolute basics.*

### What You MUST Know to Pass (30 minutes)

#### Concept #1: What is Packet Switching?
The revolutionary idea that made computer networking possible.
- **Old way (Circuit Switching):** Dedicated line between two points (like a phone call)
- **New way (Packet Switching):** Break data into small pieces, send them independently, reassemble at destination
- **Why it matters:** More efficient, more reliable, allows many users to share the same network

#### Concept #2: The Two Networking Models
**OSI Model (7 Layers)** - The theoretical/teaching model
- Application, Presentation, Session, Transport, Network, Data Link, Physical
- Memory trick: "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing" (top to bottom)

**TCP/IP Model (4 Layers)** - The practical/real-world model
- Application, Transport, Internet, Network Interface
- This is what the actual internet uses!

#### Concept #3: TCP vs UDP (MEMORIZE THIS)
```
TCP = Reliable, Slow, Connection-oriented
    - Like certified mail (guaranteed delivery, receipt confirmation)
    - Uses: Web browsing, email, file transfers

UDP = Unreliable, Fast, Connectionless
    - Like sending a postcard (fast, but no guarantee)
    - Uses: Video streaming, gaming, DNS queries
```

#### Concept #4: IP Addressing Basics
- **IPv4:** 192.168.1.1 (four numbers, dots, running out of addresses)
- **IPv6:** 2001:0db8:85a3::8a2e:0370:7334 (longer, colons, practically unlimited)
- **Private IPs:** 192.168.x.x, 10.x.x.x, 172.16-31.x.x (used inside your network)
- **Public IPs:** Everything else (used on the internet)

#### Concept #5: Essential CLI Commands
```
Navigation:
  pwd / cd       = Where am I? / Change directory
  ls / dir       = List files

Network Diagnostics:
  ping           = Test if a host is reachable
  traceroute     = Show the path to a destination
  ipconfig       = Show your network configuration
```

---

### Can You Answer These 5 Basic Questions?

**Q1:** What technology did packet switching replace for computer networking?
<details><summary>Click for answer</summary>
Circuit switching
</details>

**Q2:** How many layers does the OSI model have? TCP/IP model?
<details><summary>Click for answer</summary>
OSI = 7 layers, TCP/IP = 4 layers
</details>

**Q3:** Which protocol would you use for a video call - TCP or UDP?
<details><summary>Click for answer</summary>
UDP - speed matters more than perfect delivery for real-time video
</details>

**Q4:** Is 192.168.1.100 a public or private IP address?
<details><summary>Click for answer</summary>
Private (192.168.x.x is always private)
</details>

**Q5:** What command tests if you can reach a website?
<details><summary>Click for answer</summary>
ping
</details>

**If you got 3+ correct:** Proceed to 3-Hour Crash Course
**If you got 0-2 correct:** Read this section again, then review lecture slides

---

## QUICK REVIEW TRACK (For Path A: Well-Prepared Students)

*You've done the work. Here's a 30-minute refresher.*

### Top 5 Concepts Students Get Wrong (Focus Here!)

#### COMMON MISTAKE #1: Confusing the OSI and TCP/IP Models

**OSI Model (7 Layers):**
- Theoretical reference model
- Created by ISO in 1984
- Great for teaching layer concepts
- Each layer has specific, narrow function

**TCP/IP Model (4 Layers):**
- Practical model used by the internet
- Developed earlier (1970s)
- Combines some OSI layers
- What actually runs on networks today

**Mapping:**
```
OSI                     TCP/IP
---                     ------
7. Application   ]
6. Presentation  ]----> Application
5. Session       ]

4. Transport     -----> Transport

3. Network       -----> Internet

2. Data Link     ]
1. Physical      ]----> Network Interface
```

**Memory trick:**
- OSI = "Open" (theoretical, educational)
- TCP/IP = "Practical" (what's actually used)

---

#### COMMON MISTAKE #2: Confusing TCP and UDP Characteristics

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | Best effort |
| Order | Maintains order | No ordering |
| Speed | Slower (overhead) | Faster (minimal overhead) |
| Handshake | 3-way handshake | None |
| Error checking | Yes, with retransmission | Optional, no retransmission |

**When to use TCP:**
- File downloads (need every byte)
- Email (must arrive completely)
- Web pages (HTML must be intact)

**When to use UDP:**
- Live video/audio (old frames don't matter)
- Gaming (speed > perfection)
- DNS queries (simple, fast lookups)

**Memory trick:**
- **TCP** = "Trust" (reliable, verified)
- **UDP** = "Unreliable but Darn fast"

---

#### COMMON MISTAKE #3: Misunderstanding What Each Layer Does

Students often mix up layer responsibilities. Focus on the KEY function:

| Layer | Key Question | Answer |
|-------|--------------|--------|
| Application | What service does the user need? | HTTP, SMTP, DNS, FTP |
| Transport | How do we ensure reliable delivery? | TCP (reliable) or UDP (fast) |
| Network | How do we route between networks? | IP addressing, routers |
| Data Link | How do we communicate on the same network? | MAC addresses, switches |
| Physical | How do we transmit bits? | Cables, signals, wireless |

**Key Insight:** Data goes DOWN the layers on sending, UP on receiving. Each layer adds/removes headers (encapsulation).

---

#### COMMON MISTAKE #4: Not Understanding NAT's Purpose

**What is NAT (Network Address Translation)?**
- Translates private IPs to public IPs and back
- Allows many devices to share one public IP
- Your home router uses NAT!

**Why NAT exists:**
- IPv4 address exhaustion (only ~4.3 billion addresses)
- Security (hides internal network structure)
- Cost (don't need a public IP for every device)

**Example:**
```
Your laptop: 192.168.1.100 (private)
         |
    Home Router (NAT)
         |
Internet sees: 74.125.224.72 (public - your ISP assigned this)
```

---

#### COMMON MISTAKE #5: Confusing Routers and Switches

| Device | Layer | Uses | Function |
|--------|-------|------|----------|
| **Router** | Network (3) | IP addresses | Connects DIFFERENT networks |
| **Switch** | Data Link (2) | MAC addresses | Connects devices on SAME network |
| **Hub** | Physical (1) | N/A | Dumb repeater (obsolete) |

**Memory trick:**
- **Router** = "Routes between networks" (like a post office sorting mail between cities)
- **Switch** = "Switches within a network" (like a mail room directing to specific offices)

---

### 10-Minute Memory Refresh

**Historical Milestones:**
- 1961: Packet switching theory (Kleinrock)
- 1969: ARPANET (first 4 nodes)
- 1973: Ethernet (Metcalfe)
- 1974: TCP (Cerf & Kahn)
- 1983: TCP/IP becomes ARPANET standard
- 1984: OSI model published

**OSI Layers (Top to Bottom):**
- All People Seem To Need Data Processing
- 7-Application, 6-Presentation, 5-Session, 4-Transport, 3-Network, 2-Data Link, 1-Physical

**Encapsulation Terms:**
- Application: Data
- Transport: Segments
- Network: Packets
- Data Link: Frames
- Physical: Bits

**CLI Commands to Know:**
- `ping` = Test connectivity
- `traceroute/tracert` = Show path
- `ipconfig/ifconfig` = Show network config
- `netstat` = Show connections
- `nslookup/dig` = DNS query

**You're Ready!**

---

## 3-HOUR CRASH COURSE (For Path B: Average Students)

*Structured review of all key concepts with examples*

### Hour 1: Networking History & Foundations (60 minutes)

#### Minutes 1-15: The Problem & Solution

**The Problem (Pre-1960s):**
- Computers couldn't communicate with each other
- Circuit switching (telephone system) was inefficient for computers
- Dedicated lines wasted resources when idle

**The Solution: Packet Switching**
- Proposed by Leonard Kleinrock (1961) using queuing theory
- Break messages into small packets
- Each packet travels independently
- Packets can take different routes
- Reassemble at destination

**Why Packet Switching Won:**
| Circuit Switching | Packet Switching |
|-------------------|------------------|
| Dedicated path required | Shared network paths |
| Wasteful when idle | Efficient use of bandwidth |
| Single point of failure | Resilient to failures |
| Fixed capacity | Scalable |

**Key Terms:**
- **Packet:** Small unit of data with header information
- **Routing:** Finding the best path for packets
- **Queuing Theory:** Mathematical foundation for packet switching

---

#### Minutes 16-30: ARPANET & Early Networking

**ARPANET (1969):**
- First operational packet-switched network
- Funded by DARPA (US Department of Defense)
- Initial 4 nodes: UCLA, SRI, UCSB, University of Utah
- Proved packet switching worked at scale

**Key Milestones:**
- **1965:** First long-distance computer connection (MIT to California, 300 bps)
- **1969:** ARPANET goes live (October 29 - first message "LO")
- **1971:** Email invented on ARPANET
- **1973:** Ethernet invented by Robert Metcalfe at Xerox PARC

**Why This Matters:**
- ARPANET proved packet switching theory
- Became the foundation for the internet
- Open protocols enabled growth

---

#### Minutes 31-45: TCP/IP Development

**The Challenge:**
- Different networks couldn't talk to each other
- Needed a common "language" (protocol)

**The Solution: TCP (1974)**
- Created by Vint Cerf and Bob Kahn
- Transmission Control Protocol
- Enabled "internetworking" - connecting different networks

**The Split (1978):**
- TCP was split into two protocols:
  - **IP (Internet Protocol):** Handles addressing and routing
  - **TCP (Transmission Control Protocol):** Handles reliable delivery

**1983: The Switch**
- ARPANET officially adopted TCP/IP (January 1, 1983 - "Flag Day")
- This made the internet possible

**Key People to Remember:**
| Person | Contribution |
|--------|--------------|
| Leonard Kleinrock | Packet switching theory |
| Larry Roberts | ARPANET project leader |
| Vint Cerf | TCP/IP co-creator |
| Bob Kahn | TCP/IP co-creator |
| Robert Metcalfe | Ethernet inventor |

---

#### Minutes 46-60: The Standards War

**The Problem (1980s):**
- Multiple competing protocols:
  - ARPANET (TCP/IP)
  - IBM's SNA
  - Digital's DECnet
  - Xerox's XNS
  - Novell's IPX/SPX
- Networks couldn't interoperate

**OSI Model (1984):**
- Created by ISO (International Organization for Standardization)
- 7-layer reference model
- Designed to be THE networking standard
- Ultimately became a teaching/reference model, not the standard

**Why TCP/IP Won:**
- Already working and deployed
- Open and free (no licensing)
- Simpler and more practical
- ARPANET/Internet adoption drove it
- "Running code wins"

**Key Insight:** Understanding WHY decisions were made helps you understand modern networking.

---

### Hour 2: Networking Models & Layers (60 minutes)

#### Minutes 1-20: OSI Model Deep Dive

**The 7 Layers (Top to Bottom):**

**Layer 7 - Application**
- What users interact with
- Protocols: HTTP, HTTPS, FTP, SMTP, DNS, SSH
- Example: Your web browser

**Layer 6 - Presentation**
- Data formatting and encryption
- Handles: Encryption (SSL/TLS), compression, character encoding
- Example: HTTPS encryption

**Layer 5 - Session**
- Manages connections/sessions
- Handles: Session establishment, maintenance, termination
- Example: Keeping you logged in

**Layer 4 - Transport**
- Reliable (or fast) delivery
- Protocols: TCP (reliable), UDP (fast)
- Example: Ensuring all bytes of a file arrive

**Layer 3 - Network**
- Routing between networks
- Protocol: IP (Internet Protocol)
- Devices: Routers
- Example: Getting data from your network to Google's network

**Layer 2 - Data Link**
- Communication on same network
- Uses: MAC addresses
- Devices: Switches
- Example: Getting data from your laptop to your router

**Layer 1 - Physical**
- Actual signal transmission
- Includes: Cables, wireless signals, electrical impulses
- Example: Ethernet cable, Wi-Fi radio waves

---

**Memory Tricks for OSI Layers:**

**Top to Bottom (7 to 1):**
- **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
- **A**ll **P**ros **S**tudy **T**his **N**etworking **D**ata **P**roperly

**Bottom to Top (1 to 7):**
- **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way
- **P**hysical **D**ata **N**etwork **T**ransport **S**ession **P**resentation **A**pplication

---

#### Minutes 21-40: TCP/IP Model & Comparison

**TCP/IP Model (4 Layers):**

| Layer | Function | Key Protocols |
|-------|----------|---------------|
| Application | User services | HTTP, FTP, SMTP, DNS, SSH |
| Transport | End-to-end delivery | TCP, UDP |
| Internet | Routing between networks | IP, ICMP |
| Network Interface | Local network communication | Ethernet, Wi-Fi |

**OSI to TCP/IP Mapping:**

```
        OSI Model              TCP/IP Model
    +--------------+        +------------------+
    | Application  |        |                  |
    +--------------+        |    Application   |
    | Presentation |   -->  |                  |
    +--------------+        +------------------+
    | Session      |
    +--------------+
    | Transport    |   -->  |    Transport     |
    +--------------+        +------------------+
    | Network      |   -->  |    Internet      |
    +--------------+        +------------------+
    | Data Link    |        |                  |
    +--------------+   -->  | Network Interface|
    | Physical     |        |                  |
    +--------------+        +------------------+
```

**Why Both Models Exist:**
- **OSI:** Great for understanding concepts, teaching, troubleshooting
- **TCP/IP:** What actually runs on the internet

---

#### Minutes 41-60: Encapsulation

**What is Encapsulation?**
- Each layer adds its own header information
- Data gets "wrapped" as it goes down the layers
- Unwrapped as it goes up at the destination

**Data Unit Names:**

| Layer | Data Unit | What's Added |
|-------|-----------|--------------|
| Application | Data | Application info |
| Transport | Segment | Port numbers, sequence numbers |
| Network | Packet | IP addresses |
| Data Link | Frame | MAC addresses |
| Physical | Bits | Electrical/optical signals |

**Visual Example:**
```
Sending Email:

Application: [Email Content]

Transport:   [TCP Header][Email Content]
              (port 25)

Network:     [IP Header][TCP Header][Email Content]
            (source/dest IP)

Data Link:   [Frame Header][IP Header][TCP Header][Email Content][Trailer]
              (MAC addresses)

Physical:    10110010110010110011... (bits on the wire)
```

**Key Insight:** Each layer only needs to understand its own header. This is why layers are independent!

---

### Hour 3: Protocols, Addressing & CLI (60 minutes)

#### Minutes 1-20: TCP vs UDP Deep Dive

**TCP (Transmission Control Protocol)**
- **Connection-oriented:** Must establish connection first
- **Three-way handshake:**
  1. SYN (Client: "Want to connect?")
  2. SYN-ACK (Server: "Yes, I'm ready")
  3. ACK (Client: "Great, let's go!")
- **Reliable:** Guarantees delivery, retransmits lost packets
- **Ordered:** Packets delivered in sequence
- **Flow control:** Prevents overwhelming the receiver

**UDP (User Datagram Protocol)**
- **Connectionless:** No handshake needed
- **Unreliable:** No guarantee of delivery
- **Fast:** Minimal overhead
- **No ordering:** Packets may arrive out of order
- **Use cases:** When speed > reliability

**Protocol Comparison:**

| Use Case | Protocol | Why? |
|----------|----------|------|
| Web browsing | TCP | Need complete HTML |
| Email | TCP | Must arrive intact |
| File download | TCP | Every byte matters |
| Video call | UDP | Speed matters, old frames useless |
| Gaming | UDP | Latency critical |
| DNS query | UDP | Simple, fast lookup |
| Video streaming | UDP | Buffering handles packet loss |

**Memory Trick:**
- TCP = "Trustworthy" (reliable but slower)
- UDP = "Ultra-speed Delivery" (fast but unreliable)

---

#### Minutes 21-40: IP Addressing

**IPv4 Addressing**
- Format: `192.168.1.1` (4 octets, dotted decimal)
- Size: 32 bits (~4.3 billion addresses)
- Problem: Running out of addresses!

**Private vs Public IP Ranges:**

| Type | Ranges | Use |
|------|--------|-----|
| Private | 10.0.0.0 - 10.255.255.255 | Internal networks |
| Private | 172.16.0.0 - 172.31.255.255 | Internal networks |
| Private | 192.168.0.0 - 192.168.255.255 | Home networks |
| Public | Everything else | Internet-routable |

**NAT (Network Address Translation):**
- Translates private IPs to public IPs
- Multiple devices share one public IP
- Your home router does this!

---

**IPv6 Addressing**
- Format: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Size: 128 bits (practically unlimited: 340 undecillion addresses)
- Notation: Hexadecimal, colons
- Can shorten: `2001:db8:85a3::8a2e:370:7334` (:: replaces consecutive zeros)

**IPv4 vs IPv6:**

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address size | 32 bits | 128 bits |
| Format | Dotted decimal | Hexadecimal with colons |
| Addresses | ~4.3 billion | ~340 undecillion |
| Header | Variable length | Fixed 40 bytes |
| Security | Optional (IPSec) | Built-in (IPSec required) |
| NAT | Common/necessary | Not needed |

---

**Other Key Protocols:**

| Protocol | Layer | Purpose |
|----------|-------|---------|
| DNS | Application | Translates domain names to IP addresses |
| DHCP | Application | Automatically assigns IP addresses |
| ICMP | Network | Error messages, ping uses this |
| ARP | Data Link | Maps IP addresses to MAC addresses |

**DNS Example:**
```
You type: www.google.com
DNS translates to: 142.250.80.78
Your computer connects to: 142.250.80.78
```

---

#### Minutes 41-60: Command Line Interface (CLI)

**Why CLI Matters:**
- Faster than clicking through GUIs
- Can be automated with scripts
- Works over remote connections (SSH)
- Available on all systems
- Essential for network troubleshooting

**Navigation Commands:**

| Task | Windows | Mac/Linux |
|------|---------|-----------|
| Show current directory | `cd` (no args) | `pwd` |
| List files | `dir` | `ls` |
| Change directory | `cd folder` | `cd folder` |
| Go up one level | `cd ..` | `cd ..` |
| Go to home | `cd %USERPROFILE%` | `cd ~` |
| Clear screen | `cls` | `clear` |

**File Operations:**

| Task | Windows | Mac/Linux |
|------|---------|-----------|
| View file contents | `type file.txt` | `cat file.txt` |
| Create folder | `mkdir folder` | `mkdir folder` |
| Copy file | `copy src dest` | `cp src dest` |
| Move/rename | `move src dest` | `mv src dest` |
| Delete file | `del file.txt` | `rm file.txt` |
| Delete folder | `rmdir folder` | `rm -r folder` |

---

**Network Diagnostic Commands:**

**`ping` - Test Connectivity**
```
ping google.com
```
- Tests if a host is reachable
- Uses ICMP protocol
- Shows round-trip time (latency)
- Packet loss indicates network problems

**`traceroute` / `tracert` - Trace Path**
```
traceroute google.com    (Mac/Linux)
tracert google.com       (Windows)
```
- Shows each hop (router) between you and destination
- Helps identify where problems occur
- Shows latency at each hop

**`ipconfig` / `ifconfig` - Network Configuration**
```
ipconfig               (Windows)
ifconfig               (Mac/Linux - older)
ip addr                (Linux - modern)
```
- Shows your IP address(es)
- Shows subnet mask
- Shows default gateway
- Shows DNS servers

**`netstat` - Network Statistics**
```
netstat -an
```
- Shows active connections
- Shows listening ports
- Helps identify what's connected

**`nslookup` / `dig` - DNS Lookup**
```
nslookup google.com
dig google.com         (Mac/Linux)
```
- Queries DNS servers
- Shows IP address for domain name
- Helps troubleshoot DNS issues

---

**Path Concepts:**

**Absolute Path:** Complete path from root
- Windows: `C:\Users\Student\Documents\file.txt`
- Mac/Linux: `/home/student/documents/file.txt`

**Relative Path:** Path from current location
- `./file.txt` (file in current directory)
- `../file.txt` (file in parent directory)
- `folder/file.txt` (file in subfolder)

---

## PRACTICE QUIZ (With Difficulty Ratings)

### Basic Questions (Should get 100% correct)

1. What technology did packet switching replace?
   - **Answer:** Circuit switching

2. How many layers does the OSI model have?
   - **Answer:** 7 layers

3. Which protocol is reliable - TCP or UDP?
   - **Answer:** TCP

4. What does DNS do?
   - **Answer:** Translates domain names to IP addresses

5. What command tests if a host is reachable?
   - **Answer:** ping

---

### Moderate Questions (Should get 70%+ correct)

6. TRUE or FALSE: The TCP/IP model was created after the OSI model.
   - **Answer:** FALSE (TCP/IP came first, OSI was 1984)

7. At which layer do routers operate?
   - **Answer:** Network layer (Layer 3)

8. What does the three-way handshake establish?
   - **Answer:** A TCP connection (SYN, SYN-ACK, ACK)

9. Is 10.0.0.50 a public or private IP address?
   - **Answer:** Private

10. What layer handles MAC addresses?
    - **Answer:** Data Link layer (Layer 2)

11. What protocol would you use for live video streaming?
    - **Answer:** UDP (speed over reliability)

12. What does NAT stand for and what does it do?
    - **Answer:** Network Address Translation; translates private IPs to public IPs

---

### Challenging Questions (Target 50%+ correct)

13. Why did TCP/IP win over the OSI protocols?
    - **Answer:** Already deployed, open/free, simpler, practical (running code wins)

14. Put these in order from LARGEST to SMALLEST data unit: Packet, Bit, Frame, Segment
    - **Answer:** Segment > Packet > Frame > Bit (in terms of encapsulation order)

15. A video call uses which transport protocol and why?
    - **Answer:** UDP, because speed and low latency matter more than perfect delivery

16. What's the difference between a router and a switch?
    - **Answer:** Router connects different networks (uses IPs), switch connects devices on same network (uses MACs)

17. What information does `traceroute` show that `ping` doesn't?
    - **Answer:** The path/hops between source and destination

18. Name two differences between IPv4 and IPv6.
    - **Answer:** Any two of: address size (32 vs 128 bits), format (dotted decimal vs hex/colons), address space, built-in security in IPv6, no NAT needed for IPv6

---

## FINAL CHECKLIST: Am I Ready?

Rate your confidence (1-5) for each skill:

**History & Foundations:**
- ___ Understand why packet switching was revolutionary
- ___ Know key milestones (ARPANET, TCP/IP, Ethernet)
- ___ Understand why TCP/IP won over OSI protocols
- ___ Can name key contributors and their contributions

**Networking Models:**
- ___ Can list all 7 OSI layers in order
- ___ Know the function of each OSI layer
- ___ Can map OSI layers to TCP/IP model
- ___ Understand encapsulation process
- ___ Know which devices operate at which layers

**Protocols & Addressing:**
- ___ Can compare and contrast TCP vs UDP
- ___ Know when to use TCP vs UDP
- ___ Understand IPv4 address format
- ___ Can identify private vs public IP ranges
- ___ Understand purpose of NAT
- ___ Know basic IPv6 format
- ___ Understand what DNS, DHCP, ICMP, ARP do

**Command Line:**
- ___ Can navigate file system with CLI
- ___ Know basic network diagnostic commands
- ___ Understand output of ping, traceroute, ipconfig
- ___ Know difference between absolute and relative paths

**If most ratings are 3+, you're ready!**
**If many ratings are 1-2, focus on those specific topics.**

---

## QUICK REFERENCE SHEET (Print This!)

**OSI Model (7 Layers - Top to Bottom):**
```
7. Application    - HTTP, FTP, SMTP, DNS
6. Presentation   - Encryption, formatting
5. Session        - Connection management
4. Transport      - TCP (reliable), UDP (fast)
3. Network        - IP, routing, routers
2. Data Link      - MAC addresses, switches
1. Physical       - Cables, signals, bits
```

**Memory Trick:** All People Seem To Need Data Processing

**TCP/IP Model (4 Layers):**
```
Application      (combines OSI 5-7)
Transport        (same as OSI 4)
Internet         (same as OSI 3)
Network Interface (combines OSI 1-2)
```

**TCP vs UDP:**
```
TCP = Reliable, Ordered, Slow (web, email, files)
UDP = Unreliable, Fast, Simple (video, gaming, DNS)
```

**Private IP Ranges:**
```
10.0.0.0 - 10.255.255.255
172.16.0.0 - 172.31.255.255
192.168.0.0 - 192.168.255.255
```

**Key Devices:**
```
Router = Layer 3 = IP addresses = Between networks
Switch = Layer 2 = MAC addresses = Same network
```

**CLI Commands:**
```
ping          = Test connectivity
traceroute    = Show path to destination
ipconfig      = Show network configuration
netstat       = Show connections
nslookup      = DNS lookup
```

**Encapsulation Order (Sending):**
```
Data → Segment → Packet → Frame → Bits
(Application → Transport → Network → Data Link → Physical)
```

---

## EXAM STRATEGY

**For Open Note/Open Book:**
- Organize your notes by topic BEFORE the exam
- Tab or bookmark key sections
- Create a quick-reference cheat sheet
- Know WHERE to find information, not just what it is

**Time Management:**
- Read ALL questions first
- Answer easy questions first
- Budget time based on point values
- Save 5-10 minutes for review

**For Conceptual Questions:**
- Think about the "why" not just the "what"
- Consider real-world applications
- If two answers seem right, look for the BEST answer

**For CLI Questions:**
- Visualize what the command would do
- Think about the output you would see
- Remember cross-platform differences (Windows vs Mac/Linux)

**Common Mistakes to Avoid:**
- Don't confuse OSI and TCP/IP models
- Don't mix up TCP and UDP characteristics
- Don't forget that routers use IPs, switches use MACs
- Don't confuse the layer numbers (remember the mnemonic!)
- Don't leave questions blank (partial credit is possible)

---

## Cross-References to Course Materials

**For deeper understanding, review:**

- **Networking History:** lecture1_presentation.md, lecture1_speaker_notes.md
- **OSI Model:** lecture2_presentation.md (Layer-by-layer section)
- **TCP/IP Model:** lecture2_presentation.md, lecture2_speaker_notes.md
- **Protocols & Addressing:** lecture2_speaker_notes.md, IPv6_NetworkAddressing.pdf
- **CLI Skills:** CLE_tutorial.md, CLI_Mastery_Lecture_Notes.md
- **Hands-on Practice:** CLI_Lab_Setup_Package/

---

## Still Confused? Get Help!

**Office Hours:** [Insert schedule]
**Tutoring Center:** [Insert location/hours]
**Study Groups:** [Insert information]

**Tonight Before Exam:**
- Review this study guide (focus on COMMON MISTAKES)
- Do the practice quiz (aim for 70%+)
- Get good sleep (seriously - sleep > cramming)
- Have materials ready and organized

**Day of Exam:**
- Eat a good breakfast
- Arrive early
- Take deep breaths - you've got this!

---

## Good Luck!

Remember: This is an open-note exam. Success comes from understanding concepts AND knowing where to find information quickly. Organize your materials well!

**You've got this!**

---

*Study guide created for CSCI 101 Module 3 Exam*
*Topics: Computer Networking Foundations & Command Line Mastery*
