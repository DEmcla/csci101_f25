# A Brief History of Connecting Computers (Networking)
## CSCI 101

---

## Slide 1: A Brief History of Connecting Computers
**CSCI 101**

The story of how we built the Internet

---

## Slide 2: The Challenge
**How do you get computers to talk to each other?**

**Problems:**
- Different manufacturers = different hardware
- Different operating systems = different data formats
- Long distances = unreliable transmission
- No standards = isolated systems

**Question:** Can we connect ANY computer to ANY other computer?

---

## Slide 3: Starting Place: Connecting Computers

**Before Networking:**
- Computers were standalone systems
- Data transfer via physical media (punch cards, tape)
- No remote communication capability
- Each system isolated

**The Vision:**
Computers that can communicate across distances

---

## Slide 4: Packet Switching Theory (1961)
**Leonard Kleinrock, MIT**

**[IMAGE: network_models_images/image1.png]**
*Historical photo/illustration of Kleinrock or packet switching concept*

**The Problem: Circuit Switching**
- Telephone networks reserved dedicated paths
- Connection stays open entire time (even during idle periods)
- Wasteful for computer communication
- Computers send data in bursts, then process

**Publication:**
"Information Flow in Large Communication Nets" (1961)
- Used queuing theory to prove packet switching more efficient

---

## Slide 5: Packet Switching: The Solution

**Key Idea:**
Break messages into small, independent packets

**Benefits:**
- **Efficient:** Multiple communications share same infrastructure
- **Reliable:** Packets automatically reroute around failures
- **Flexible:** Handles temporary congestion by buffering

**Foundation:**
Mathematical proof that packet-switched networks > circuit-switched networks

---

## Slide 6: Analogy: Sending a Book

**[VISUAL NEEDED: Diagram comparing circuit vs packet switching]**
*Split-screen showing mail truck (circuit) vs individual letters (packets)*

**Circuit Switching:**
- Reserve entire mail truck for one book
- Truck travels whether full or empty
- Wasteful but guaranteed

**Packet Switching:**
- Mail each page separately
- Pages take different routes
- Efficient use of postal system
- Reassemble at destination

---

## Slide 7: First Connection (1965)
**Lawrence G. Roberts and Thomas Merrill**

**[IMAGE: network_models_images/image2.png]**
*Bell 103A modem or early connection hardware*

**Achievement:**
First computer-to-computer communication over telephone line

**Connection:**
- MIT Lincoln Laboratory → System Development Corporation (California)
- Used Bell 103A Modem (similar specs)

**Bell 103A Specifications:**
- Introduction Year: 1962
- Data Rate: 300 bits per second (bps)
- Modulation: Frequency-shift keying (FSK)
- Connection: Dial-up analog telephone lines

**Result:**
"Took several tries, finally worked!"

---

## Slide 8: What 300 bps Means

**Speed:**
300 bits per second = ~37 characters of text per second

**Perspective:**
- Single page of text: ~2 minutes
- Today's speeds: Millions of times faster

**Significance:**
Proved remote computer communication was feasible

---

## Slide 9: Birth of ARPANET (1969)
**The First Packet-Switched Network**

**Funding:**
U.S. Department of Defense (ARPA)

**Goals:**
- Develop resilient, decentralized communication network
- Enable resource sharing among research institutions
- Create network that could withstand nuclear attack (Cold War motivation)

**Leadership:**
- Steve Crocker: Led protocol development
- Vint Cerf: Later co-developed TCP/IP
- Leonard Kleinrock: UCLA lab hosted first node

---

## Slide 10: ARPANET: Initial Four Nodes (1969)

**[VISUAL NEEDED: Map of United States showing 4 nodes]**
*UCLA, SRI, UCSB, University of Utah with connecting lines*

**The Original Network:**

1. **UCLA** - Leonard Kleinrock's laboratory
2. **Stanford Research Institute (SRI)** - Network information center
3. **UC Santa Barbara (UCSB)** - Interactive computing expertise
4. **University of Utah** - Graphics and visualization research

**Technology:**
- Interface Message Processors (IMPs) at each node
- Network Control Protocol (NCP) for communication

---

## Slide 11: The First Message

**Date:**
October 29, 1969

**Attempt:**
UCLA student Charley Kline tries to login to SRI computer remotely

**Message:**
Began typing "LOGIN"

**Result:**
System crashed after "LO"

**Lesson:**
Even with failure, demonstrated packet switching could recover and continue
- This resilience was exactly what designers wanted

---

## Slide 12: ARPANET Design Principles

**Key Innovations:**

**Distributed Routing:**
- No central control point
- Automatic adaptation to failures
- Packets reroute around damaged links

**Open Standards:**
- Common protocols all participants could implement
- Network growth without vendor constraints

**Separation of Concerns:**
- IMPs handled networking
- Host computers provided services
- Network could evolve independently

---

## Slide 13: Development of Ethernet (1973)
**Robert Metcalfe, Xerox PARC**

**Challenge:**
Local Area Networks (LANs) - connecting multiple computers in same building

**Inspiration:**
ALOHAnet (University of Hawaii)
- Used radio for random access protocol
- Multiple devices shared single communication channel

**Innovation:**
Adapted random access for wired networks

---

## Slide 14: Ethernet Technology

**Medium:**
Coaxial cables (originally)

**Protocol:**
CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

**How it Works:**
1. **Carrier Sense:** Listen before transmitting
2. **Multiple Access:** Multiple hosts share same medium
3. **Collision Detection:** Detect when transmissions interfere
4. **Backoff:** Wait random time, then retry

**Impact:**
Standard for LANs, still used today (evolved to 400 Gbps)

---

## Slide 15: CSMA/CD: Managing Collisions

**[VISUAL NEEDED: Flowchart of CSMA/CD process]**
*Listen → Transmit → Detect Collision? → Backoff → Retry*

**The "Polite Conversation" Protocol:**

1. Listen to network (is anyone talking?)
2. If quiet → start transmitting
3. While transmitting → monitor for collisions
4. If collision detected:
   - Stop immediately
   - Wait random time (exponential backoff)
   - Try again

**Result:**
Efficient sharing without centralized control

---

## Slide 16: Metcalfe's Commercial Success

**1979:**
Robert Metcalfe leaves Xerox, founds **3Com Corporation**

**Impact:**
- Commercialized Ethernet technology
- Became leading networking equipment company
- Proved open standards can be foundation for successful business

**Lesson:**
Open standards enable innovation AND commercial success

---

## Slide 17: Transmission Control Protocol (1974)
**Vint Cerf and Bob Kahn**

**Challenge:**
Internetworking - connecting different types of networks

**Publication:**
First TCP specification (1974)

**Goal:**
Enable communication across diverse network technologies
- ARPANET, packet radio, satellite links, LANs

---

## Slide 18: TCP: Four Key Innovations

**1. Network Agnosticism:**
- Works over ANY underlying network type
- Reliable inter-network communication (satellite, radio, wired)

**2. Packet Switching:**
- Small packets independently routed and reassembled
- Efficient resource use

**3. End-to-End Communication:**
- Reliability at endpoints, not in network
- Receiving end acknowledges receipt
- Automatic retransmission of lost packets

**4. Layered Architecture:**
- Separation of functions into distinct layers
- Modular design enables independent evolution

---

## Slide 19: TCP Technical Features

**Port Numbers:**
- Enable multiple simultaneous connections
- Different applications use different ports

**Three-Way Handshake:**
- Establishes reliable connections
- SYN → SYN-ACK → ACK

**Flow Control:**
- Prevents fast senders from overwhelming slow receivers
- Sliding window mechanism

**Congestion Control:**
- Detects network overload
- Automatically adjusts transmission rates

---

## Slide 20: IBM's Alternative: SNA (1976)
**Systems Network Architecture**

**Purpose:**
Proprietary networking protocol for IBM mainframe computers

**Architecture:**
- Seven-layer model (similar to, but predates OSI)
- Comprehensive enterprise solution

**Components:**
- **Logical Units (LUs):** Endpoints representing devices/applications
- **Physical Units (PUs):** Control points managing communication
- **Transmission Control Units (TCUs):** Data flow management (error checking, sequencing)

---

## Slide 21: SNA: Strengths and Limitations

**Strengths:**
- Excellent IBM integration
- Sophisticated for its time
- Comprehensive enterprise features
- Influenced future protocol design

**Limitations:**
- Proprietary system
- Difficult to connect non-IBM equipment
- Expensive for mixed environments
- Vendor lock-in

**Lesson:**
Open standards win long-term vs. proprietary solutions

---

## Slide 22: TCP/IP Split (1978)
**Two Protocols Are Better Than One**

**Problem:**
Single protocol handling BOTH transmission control AND routing became too complex

**Solution:**
Split into two protocols:

**TCP (Transmission Control Protocol):**
- Reliable data delivery
- Error checking and retransmission
- Flow control

**IP (Internet Protocol):**
- Addressing and routing
- Moving packets across networks

---

## Slide 23: Why Split TCP and IP?

**Scalability:**
- Growing networks needed specialized functions
- Single protocol couldn't handle both efficiently

**Modularity:**
- Each protocol optimized for specific function
- Clean separation of responsibilities

**Flexibility:**
- New transport protocols could use IP
- New network technologies only affect IP layer

**Network Agnosticism:**
- TCP focuses on reliable delivery
- IP focuses on routing

---

## Slide 24: The Standardization Challenge (Late 1970s)

**Fragmentation Crisis:**

**Multiple Incompatible Systems:**
- ARPANET / TCP/IP (research community)
- IBM SNA (enterprises)
- DEC DECnet (DEC minicomputers)
- Xerox XNS (office equipment)

**Problems:**
- Systems couldn't communicate with each other
- Vendor lock-in
- High costs
- Limited innovation

**Need:**
Universal standards for global communication

---

## Slide 25: Timeline: The Path to Modern Networking

**1961:** Kleinrock publishes packet switching theory

**1965:** First long-distance computer connection

**1969:** ARPANET launches (4 nodes)

**1973:** Ethernet developed (Metcalfe)

**1974:** TCP specification published (Cerf & Kahn)

**1976:** IBM introduces SNA

**1978:** TCP/IP split

**1980s:** Standardization efforts (OSI model, TCP/IP adoption)

---

## Slide 26: Key Concepts

**Packet Switching:**
- Messages broken into small, independent packets
- Efficient, reliable, flexible communication

**Network Protocols:**
- Standardized rules enabling different systems to communicate
- Define data formats, transmission procedures

**Layered Architecture:**
- Organize functions into distinct layers
- Modular design, independent evolution

**Internetworking:**
- Connecting different types of networks
- "Network of networks" concept

**Open Standards:**
- Public specifications anyone can implement
- Enable interoperability and competition

---

## Slide 27: Lessons from History

**1. Design Decisions Have Lasting Impact**
- 1960s-70s protocols still power today's Internet
- Good foundational design = remarkable longevity

**2. Open Standards Beat Proprietary Systems**
- TCP/IP succeeded, SNA faded
- Collaboration > competition for standards

**3. Practical Solutions Win**
- "Rough consensus and running code"
- Working implementations > theoretical perfection
- Iterative refinement based on experience

---

## Slide 28: Why History Matters

**Understanding Current Technology:**
- Know WHY networks work the way they do
- Design decisions explain current limitations

**Troubleshooting:**
- Historical context helps diagnose problems
- Understand protocol behavior and edge cases

**Future Innovation:**
- Learn from successful approaches
- Avoid repeating past mistakes
- Build on proven foundations

---

## Slide 29: The Foundation is Set

**Achievements by 1978:**
- Packet switching proven (theory → practice)
- ARPANET demonstrates viability
- Ethernet solves LAN problem
- TCP/IP enables internetworking
- Clear need for universal standards

**What's Next (Lecture 2):**
- OSI Model (theoretical framework)
- TCP/IP Model (practical implementation)
- Layer-by-layer functions
- Modern applications

---

## Slide 30: Key Takeaways

**Core Principles Established:**
✓ Packet switching is the foundation
✓ Layered architecture manages complexity
✓ Open standards enable global networks
✓ End-to-end reliability is crucial
✓ Network agnosticism provides flexibility

**These principles STILL guide networking today**

---

## Slide 31: Questions & Discussion

**Topics to Consider:**

- How did packet switching change what was possible?
- Why did ARPANET's design prove so resilient?
- What made Ethernet successful for LANs?
- Why did TCP/IP need to be split?
- How do these 1960s-70s innovations affect your daily life?
- What lessons apply to modern technology development?
