# Computer Networking: A Brief History
## CSCI 101

---

## Slide 1: Computer Networking: A Brief History
**CSCI 101**

---

## Slide 2: 1970s: Development of Early Networking Protocols
**1973:** Development of the Ethernet protocol begins at Xerox PARC, led by Robert Metcalfe

**Inspired by ALOHAnet's Random Access Protocol**
- Allowed multiple devices to use single communication channel

**Key Features:**
- Designed to send data packets over coaxial cables
- Multiple hosts could communicate on same "medium"
- CSMA/CD (Carrier Sense Multiple Access with Collision Detection) managed data collisions
- Ethernet becomes a standard for local area networks (LANs)

---

## Slide 3: 1970s: Development of Early Networking Protocols
**1974:** Vint Cerf and Bob Kahn publish the first specification of the Transmission Control Protocol (TCP)

**Four Key Innovations:**

**Network Agnosticism:**
- Reliable inter-network communication (satellite, radio, wired)

**Packet Switching:**
- Small packets independently routed and reassembled

**End-to-end Communication:**
- Receiving end acknowledged receipt of data
- Mechanism for retransmission of lost packets

**Layered Architecture:**
- Separation of data transmission (TCP) from addressing and routing (IP)

---

## Slide 4: 1970s: Development of Early Networking Protocols
**1976:** IBM introduces Systems Network Architecture (SNA)
- Proprietary networking protocol for connecting IBM mainframe computers

**Architecture:**
- Used 7-layer architecture (similar to, but not the same as OSI model)

**Components:**
- **Logical Units (LUs):** Endpoints representing devices/applications communicating with each other
- **Physical Units (PUs):** Control points managing communication between network parts
- **Transmission Control Units (TCUs):** Data flow management (including error checking and data sequencing)

**Impact:**
- Influenced design of future protocols

---

## Slide 5: 1970s: Development of Early Networking Protocols
**1978:** TCP is split into TCP and IP (Internet Protocol)

**Why Split?**

**Scalability:**
- Handling both transmission control and routing within single protocol very complex
- Became issue with increasing number of connected networks and devices

**Modularity and Flexibility:**
- Different aspects of communication handled by different protocols

**Network Agnosticism:**
- Separating responsibilities allowed:
  - Transmission control (TCP) to focus on reliable delivery
  - IP to focus on routing

---

## Slide 6: Central Challenge
**Now that computers do stuff, how do you get computers to talk to each other?**

**The Problems:**
- Different manufacturers → different hardware
- Different operating systems → different data formats
- Geographical distances → unreliable transmission media

**The Need:**
- Clear need for standardization and collaboration

---

## Slide 7: Leonard's Big Idea: Packet Switching (1961)
**Leonard Kleinrock, MIT**

**[IMAGE: network_models_images/image1.png]**

**The Problem: Circuit Switching**
- Telephone networks reserved dedicated paths
- Connection stays open entire time (even during idle periods)
- Wasteful for computer communication
- Computers send data in bursts, then process

**The Solution: Packet Switching**
- Break messages into small, independent packets
- Packets share network infrastructure
- Automatic rerouting around failures
- Handle temporary congestion by buffering

**Publication:**
"Information Flow in Large Communication Nets" (1961)
- Used queuing theory to prove packet switching more efficient

---

## Slide 8: Circuit vs Packet Switching: Book Analogy

**[VISUAL NEEDED: Split-screen diagram]**

**Circuit Switching:**
- Reserve entire mail truck for one book
- Truck travels whether full or empty
- Wasteful but guaranteed delivery

**Packet Switching:**
- Mail each page separately
- Pages take different routes
- Efficient use of postal system
- Pages reassembled at destination

**Result:**
Mathematical proof that packet-switched networks > circuit-switched networks

---

## Slide 9: First Connection (1965): MIT to California
**Lawrence G. Roberts and Thomas Merrill**

**[IMAGE: network_models_images/image2.png]**

**Achievement:**
- First computer-to-computer communication over telephone line
- MIT Lincoln Laboratory → System Development Corporation (California)

**Technology: Bell 103A Modem (similar specs)**
- Introduction Year: 1962
- Data Rate: 300 bits per second (bps)
- Modulation: Frequency-shift keying (FSK)
- Connection: Dial-up analog telephone lines

**Speed Perspective:**
- 300 bps = ~37 characters of text per second
- Single page of text: ~2 minutes
- Today's speeds: Millions of times faster

**Result:**
"Took several tries, finally worked!"

**Significance:**
Proved remote computer communication was feasible

---

## Slide 10: Birth of ARPANET (1969)

**[VISUAL NEEDED: Map showing 4 nodes]**

**Funding:**
- U.S. Department of Defense (ARPA)

**Goals:**
- Develop resilient, decentralized communication network
- Enable resource sharing among research institutions
- Create network that could withstand nuclear attack (Cold War motivation)

**Technology:**
- First operational packet-switched network
- Precursor to the Internet

**Key Contributors:**
- **Steve Crocker:** Led development of ARPANET communication protocols
- **Vint Cerf:** Involved in ARPANET, later co-developed TCP/IP (1974)
- **Leonard Kleinrock:** Packet switching theorist, UCLA lab hosted first node
- **Bob Kahn:** Later co-developed TCP/IP with Cerf (1974)

---

## Slide 11: ARPANET: Initial Four Nodes

**The Original Network (1969):**

**Node 1: UCLA**
- Leonard Kleinrock's laboratory
- First node (September 1969)

**Node 2: Stanford Research Institute (SRI)**
- Network information center
- October 1969

**Node 3: UC Santa Barbara (UCSB)**
- Interactive computing expertise
- November 1969

**Node 4: University of Utah**
- Graphics and visualization research
- December 1969

**Technology:**
- Interface Message Processors (IMPs) at each node
- Network Control Protocol (NCP) for communication

---

## Slide 12: ARPANET: The First Message

**Date:** October 29, 1969

**Attempt:**
- UCLA student Charley Kline tries to login to SRI computer remotely
- Began typing "LOGIN"

**Result:**
- System crashed after "LO"

**Significance:**
- Even with failure, demonstrated packet switching could recover and continue
- This resilience was exactly what designers wanted
- Network didn't require complete restart after failure

---

## Slide 13: ARPANET Design Principles

**Key Innovations:**

**Distributed Routing:**
- No central control point
- Automatic adaptation to failures
- Packets reroute around damaged links

**Separation of Concerns:**
- IMPs (Interface Message Processors) handled networking
- Host computers provided services
- Network could evolve independently

**Open Standards:**
- Common protocols all participants could implement
- Network growth without vendor constraints
- Foundation for Internet's open architecture

**Resilience Through Routing:**
- Not a full mesh network
- Smart routing provided reliability without requiring direct connections between all nodes

---

## Slide 14: Ethernet: Managing the "Polite Conversation"

**CSMA/CD Process:**

**[VISUAL NEEDED: Flowchart]**

**How It Works:**
1. **Carrier Sense:** Listen to network before transmitting
2. **Multiple Access:** If quiet → start transmitting
3. **Collision Detection:** Monitor while transmitting
4. If collision detected:
   - Stop immediately
   - Wait random time (exponential backoff)
   - Try again

**Result:**
- Efficient sharing without centralized control
- Automatic adaptation to network traffic
- Foundation for modern Ethernet (evolved to 400 Gbps)

---

## Slide 15: Metcalfe's Commercial Success

**1979:**
- Robert Metcalfe leaves Xerox
- Founds **3Com Corporation**

**Impact:**
- Commercialized Ethernet technology
- Became leading networking equipment company
- Proved open standards can be foundation for successful business

**Lesson:**
Open standards enable innovation AND commercial success

---

## Slide 16: TCP: Port Numbers and Connections

**Port Numbers:**
- Enable multiple simultaneous connections
- Different applications use different ports
- Like apartment numbers in a building:
  - IP address = building address
  - Port number = specific apartment

**Well-Known Ports:**
- HTTP: 80
- HTTPS: 443
- SSH: 22
- SMTP: 25
- FTP: 21

**Three-Way Handshake:**
1. Client → Server: **SYN** (synchronize)
2. Server → Client: **SYN-ACK** (synchronize-acknowledge)
3. Client → Server: **ACK** (acknowledge)

**Result:** Both sides ready to exchange data

---

## Slide 17: TCP Technical Features

**Reliability Mechanisms:**

**Flow Control:**
- Prevents fast senders from overwhelming slow receivers
- Sliding window mechanism
- Receiver specifies how much data it can accept

**Congestion Control:**
- Detects network overload
- Automatically adjusts transmission rates
- Prevents network collapse

**Error Detection and Recovery:**
- Sequence numbers for every byte
- Acknowledgments confirm receipt
- Automatic retransmission of lost packets

**Result:**
Reliable communication over unreliable networks

---

## Slide 18: The Standardization Challenge (Late 1970s)

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
- Organizations isolated

**The Question:**
How do we create universal standards for global networking?

---

## Slide 19: Timeline: The Path to Modern Networking

**1961:** Kleinrock publishes packet switching theory

**1965:** First long-distance computer connection (Roberts & Merrill)

**1969:** ARPANET launches (4 nodes)

**1973:** Ethernet developed (Metcalfe at Xerox PARC)

**1974:** TCP specification published (Cerf & Kahn)

**1976:** IBM introduces SNA (proprietary alternative)

**1978:** TCP/IP split (modularity and scalability)

**1980s:** Standardization efforts begin (OSI model, TCP/IP adoption)

---

## Slide 20: Key Concepts: Foundations Established

**Packet Switching:**
- Messages broken into small, independent packets
- Efficient, reliable, flexible communication
- Foundation for all modern networking

**Network Protocols:**
- Standardized rules enabling different systems to communicate
- Define data formats, transmission procedures

**Layered Architecture:**
- Organize functions into distinct layers
- Modular design enables independent evolution
- Separation of concerns

**Internetworking:**
- Connecting different types of networks
- "Network of networks" concept
- Universal addressing and routing

**Open Standards:**
- Public specifications anyone can implement
- Enable interoperability and competition
- Foundation for Internet's success

---

## Slide 21: Lessons from History

**1. Design Decisions Have Lasting Impact**
- 1960s-70s protocols still power today's Internet
- Good foundational design = remarkable longevity
- Packet switching concept unchanged for 60+ years

**2. Open Standards Beat Proprietary Systems**
- TCP/IP succeeded, SNA faded
- Collaboration > competition for standards
- Openness enables innovation

**3. Practical Solutions Win**
- "Rough consensus and running code"
- Working implementations > theoretical perfection
- Iterative refinement based on experience
- ARPANET tested TCP/IP in real conditions

---

## Slide 22: Why History Matters

**Understanding Current Technology:**
- Know WHY networks work the way they do
- Design decisions explain current limitations
- Historical context for troubleshooting

**Learning from Success:**
- Open standards enabled global Internet
- Layered architecture manages complexity
- End-to-end reliability principle
- Network agnosticism provides flexibility

**Applying Lessons to Future:**
- These principles guide modern protocol development
- Foundation for cloud computing, IoT, mobile networks
- Framework for understanding new technologies

---

## Slide 23: The Foundation is Set

**Achievements by 1978:**
✓ Packet switching proven (theory → practice)
✓ ARPANET demonstrates viability
✓ Ethernet solves LAN problem
✓ TCP/IP enables internetworking
✓ Clear need for universal standards

**What's Next:**
- 1980s: Standardization efforts (OSI Model)
- 1983: ARPANET adopts TCP/IP formally
- 1990s: World Wide Web transforms accessibility
- 2000s+: Modern Internet emerges

**Core Principles Established:**
These 1960s-70s innovations still guide networking today

---

## Slide 24: Questions & Discussion

**Topics to Consider:**

- How did packet switching change what was possible with computer communications?

- Why was ARPANET's distributed design more resilient than centralized systems?

- What made Ethernet successful for local area networks?

- Why did TCP/IP need to be split into two separate protocols?

- How do open standards enable both collaboration and commercial success?

- What lessons from 1960s-70s networking apply to modern technology development?

- How do these innovations affect your daily use of the Internet?
