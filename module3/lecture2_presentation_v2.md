# Networking Models
## CSCI 101

---

## Slide 1: Networking Models
**CSCI 101**

Open Systems Interface (OSI) and TCP/IP

---

## Slide 2: The Standardization Crisis (1980)

**The Problem:**

**Fragmented Landscape:**
- Multiple incompatible systems (IBM SNA, DEC DECnet, Xerox XNS, TCP/IP)
- Organizations locked into single vendors
- Systems couldn't communicate across platforms
- High costs, limited innovation

**The Question:**
How do we create universal standards for global networking?

---

## Slide 3: Two Parallel Approaches

**OSI Model (1980-1984):**
- International Organization for Standardization (ISO)
- Theoretical, comprehensive framework
- "Top-down" design from first principles
- Seven layers, detailed specifications

**TCP/IP (Ongoing):**
- ARPANET research community
- Practical, evolutionary development
- "Bottom-up" design from real needs
- Four layers, proven in operation

---

## Slide 4: The OSI Model (1984)
**Open Systems Interconnection**

**Development:**
- 1980: ISO begins development
- 1984: OSI model published
- Goal: Universal networking framework

**Philosophy:**
Careful theoretical analysis produces superior design

**Key Concept:**
"Open Systems" = conforming to public specifications
- ANY conforming system can communicate with ANY other

---

## Slide 5: OSI: Four Key Innovations

**1. Open Systems:**
- Conform to publicly available specifications
- Challenged proprietary vendor lock-in

**2. Layered Architecture:**
- Systematic seven-layer structure
- Clear separation of concerns

**3. Service Definitions:**
- What each layer provides to layer above
- Implementation flexibility

**4. Protocol Specifications:**
- Detailed procedures and message formats
- Enable independent implementations to interoperate

---

## Slide 6: OSI Seven Layers
**Systematic Organization of Network Functions**

**[VISUAL NEEDED: OSI 7-layer stack diagram]**
*Seven colored boxes stacked vertically with layer numbers and names*

| Layer | Name | Function |
|-------|------|----------|
| 7 | Application | Enable users to access network |
| 6 | Presentation | Translate, encrypt, compress data |
| 5 | Session | Create, terminate, manage sessions |
| 4 | Transport | Manage delivery and error checking |
| 3 | Network | Identify shortest path (routing) |
| 2 | Data Link | Data packed into frames |
| 1 | Physical | Forms physical medium for transport |

---

## Slide 7: Layer 1 - Physical Layer

**Function:**
Transmission and reception of raw bitstreams over physical medium

**Responsibilities:**
- Electrical signal characteristics (voltage levels, timing)
- Mechanical specifications (cables, connectors)
- Physical media (copper, fiber optic, wireless)

**Network Hardware:**
- Cables (Ethernet, fiber optics)
- Connectors
- Hubs
- Network Interface Cards (NICs) - partially
- Repeaters
- Modems

**Evolution:**
10 Mbps → 400 Gbps (Ethernet)

---

## Slide 8: Layer 2 - Data Link Layer

**Function:**
Node-to-node data transfer, error detection and correction

**Responsibilities:**
- **Framing:** Organize bits into structured frames
- **Error Detection:** CRC (Cyclic Redundancy Check)
- **Media Access Control:** Manage shared medium (CSMA/CD)
- **Flow Control:** Prevent overwhelming receivers

**Sublayers:**
- **MAC (Media Access Control):** Physical addressing
- **LLC (Logical Link Control):** Interface to Layer 3

**Network Hardware:**
- Switches (forward based on MAC addresses)
- Bridges
- Network Interface Cards (NICs)

---

## Slide 9: Layer 3 - Network Layer

**Function:**
Routing packets across network boundaries, logical addressing

**Responsibilities:**
- **Logical Addressing:** IP addresses (hierarchical)
- **Routing:** Finding paths across networks
- **Packet Forwarding:** Moving packets toward destination
- **Fragmentation:** Handling different packet sizes

**Network Hardware:**
- Routers (direct packets based on IP addresses)
- Layer 3 Switches (routing + switching)
- Firewalls (some operate at this layer)

**Protocols:**
- IP (IPv4, IPv6)
- ICMP (error reporting)
- ARP (IP to MAC mapping)

---

## Slide 10: Layer 4 - Transport Layer

**Function:**
End-to-end communication, data flow control, error recovery

**Responsibilities:**
- Segmentation and reassembly
- Reliable delivery (acknowledgments, retransmission)
- Flow control (sliding window)
- Congestion control
- Port-based multiplexing

**Network Hardware:**
- Gateways (connect different protocols)
- Load Balancers (distribute traffic)

**Protocols:**
- **TCP:** Reliable, connection-oriented
- **UDP:** Fast, connectionless

---

## Slide 11: TCP vs UDP

**TCP (Transmission Control Protocol):**
- Connection-oriented (three-way handshake)
- Reliable delivery guaranteed
- Sequencing and acknowledgments
- Flow and congestion control
- **Use:** Web browsing, email, file transfer

**UDP (User Datagram Protocol):**
- Connectionless
- No reliability guarantees
- Minimal overhead = faster
- **Use:** Video streaming, gaming, DNS queries

**Choice depends on application requirements**

---

## Slide 12: TCP Three-Way Handshake

**[VISUAL NEEDED: Sequence diagram]**
*Client and Server with SYN, SYN-ACK, ACK arrows between them*

**Establishing Connections:**

1. **Client → Server: SYN**
   - "I want to connect, here's my sequence number"

2. **Server → Client: SYN-ACK**
   - "I'm ready, here's my sequence number, I got yours"

3. **Client → Server: ACK**
   - "Got it, let's exchange data"

**Result:**
Both sides ready, sequence numbers established

**Port Numbers:**
- Enable multiple simultaneous connections
- Well-known ports: HTTP (80), HTTPS (443), SSH (22)

---

## Slide 13: Layer 5 - Session Layer

**Function:**
Manage sessions between applications

**Responsibilities:**
- Session establishment and authentication
- Maintaining state information
- Dialog control (half-duplex vs. full-duplex)
- Checkpoint and recovery
- Session termination

**Network Hardware:**
- Application Gateways (some)
- Note: Most session management handled by software

**Modern Examples:**
- Web session cookies
- Database sessions
- Authenticated connections

---

## Slide 14: Layer 6 - Presentation Layer

**Function:**
Data representation and transformation

**Responsibilities:**

**1. Data Translation:**
- Big-endian vs. little-endian
- Different number representations

**2. Character Encoding:**
- ASCII, Unicode, UTF-8

**3. Encryption/Decryption:**
- SSL/TLS for secure communication

**4. Compression/Decompression:**
- Reduce bandwidth requirements

**Network Hardware:**
- Encryption Devices
- Some Gateways (protocol conversion)

**Modern Reality:**
Often handled by applications (browsers, email clients)

---

## Slide 15: Layer 7 - Application Layer

**Function:**
Network services directly to user applications

**Network Hardware:**
- Proxies (content decisions)
- Layer 7 Switches (application-aware)
- Firewalls (advanced - filter based on application content)

**Major Protocols:**
- **HTTP/HTTPS:** Web browsing
- **SMTP:** Email sending
- **POP3/IMAP:** Email retrieval
- **FTP/SFTP:** File transfer
- **DNS:** Domain name resolution
- **SSH:** Secure remote access
- **SNMP:** Network management

---

## Slide 16: TCP/IP Model
**The Practical Alternative**

**Development:**
- Evolved from ARPANET experience
- **1983:** ARPANET formally adopts TCP/IP
- Tested through operational use
- Focus: Solving real-world problems

**Philosophy:**
"Rough consensus and running code"
- Working implementations over theoretical perfection
- Iterative refinement based on experience

---

## Slide 17: TCP/IP Four Layers

**[VISUAL NEEDED: TCP/IP 4-layer stack diagram]**
*Four colored boxes stacked vertically*

**4. Application Layer:**
- Combines OSI Layers 5, 6, 7
- Direct interface to applications
- HTTP, SMTP, DNS, FTP

**3. Transport Layer:**
- TCP (reliable) and UDP (fast)
- Port-based multiplexing

**2. Internet Layer:**
- IP addressing and routing
- ICMP, ARP

**1. Network Interface Layer:**
- Combines OSI Layers 1, 2
- Access to physical network

---

## Slide 18: OSI vs TCP/IP
**Direct Comparison**

**[VISUAL NEEDED: Side-by-side layer comparison]**
*OSI 7 layers and TCP/IP 4 layers with mapping lines showing correspondence*

| Aspect | OSI | TCP/IP |
|--------|-----|--------|
| **Expands to** | Open Systems Interconnection | Transmission Control Protocol |
| **Meaning** | Theoretical model for computing systems | Client-server model for Internet transmission |
| **Layers** | 7 layers | 4 layers |
| **Developed by** | ISO (International Standards Org) | DoD (Department of Defense) |
| **Tangible** | No (theoretical) | Yes (implemented) |
| **Usage** | Educational/conceptual | Powers the Internet |
| **Approach** | Vertical (top-down) | Horizontal (bottom-up) |

---

## Slide 19: OSI vs TCP/IP: Analysis

**OSI Strengths:**
- Comprehensive theoretical framework
- Clear separation of concerns
- Excellent for education
- Systematic troubleshooting

**TCP/IP Strengths:**
- Proven in real-world operation
- Simpler, more efficient
- Responsive to changing needs
- Open development process

**The Outcome:**
- TCP/IP won in practice (powers Internet)
- OSI won in education (teaching framework)

---

## Slide 20: Encapsulation Process
**How Data Travels Through Layers**

**[VISUAL NEEDED: Encapsulation diagram]**
*Show data packet growing with each layer's header being added*

**Sending (Adding Headers):**
```
Application Data
  ↓ + TCP/UDP Header (ports, sequence)
  ↓ + IP Header (source/dest addresses)
  ↓ + Ethernet Header & Trailer (MAC, CRC)
  ↓ Physical transmission (bits)
```

**Receiving (Removing Headers):**
```
Physical bits received
  ↑ Remove Ethernet header/trailer
  ↑ Remove IP header
  ↑ Remove TCP/UDP header
  ↑ Application receives data
```

**Each layer adds its information, next layer strips it off**

---

## Slide 21: TCP/IP Protocols by Layer

**Application Layer:**
HTTP/HTTPS • FTP • SMTP • POP3/IMAP • DNS • Telnet/SSH • SNMP • DHCP • NTP

**Transport Layer:**
TCP • UDP

**Internet Layer:**
IP (IPv4, IPv6) • ICMP • ARP • RARP

**Network Interface Layer:**
Ethernet • Wi-Fi • PPP • Frame Relay • MAC

---

## Slide 22: Network Hardware by Layer

**Application Layer:**
- Servers (web, email, DNS)
- Proxies, Application firewalls

**Transport Layer:**
- Load balancers
- Gateways

**Internet Layer (Network):**
- Routers
- Layer 3 Switches

**Network Interface Layer:**
- NICs (Network Interface Cards)
- Switches
- Hubs
- Bridges
- Access Points
- Modems
- Physical cables (Cat5e, Cat6, fiber optic)

---

## Slide 23: IPv4 vs IPv6

**IPv4:**
- 32-bit addresses (192.168.1.1)
- ~4.3 billion addresses
- Address exhaustion problem
- Workaround: NAT (Network Address Translation)

**IPv6:**
- 128-bit addresses (2001:db8::1)
- 340 undecillion addresses (essentially unlimited)
- Built-in IPSec security
- Improved efficiency
- Gradual adoption ongoing

**Challenge:**
IPv4 and IPv6 not directly compatible - requires transition mechanisms

---

## Slide 24: 1990s: Internet Growth

**1990:**
- ARPANET officially decommissioned
- Internet continues growing with TCP/IP
- OSI remains academic/educational tool

**1991:**
Tim Berners-Lee introduces **World Wide Web**
- Transformed Internet accessibility
- HTTP protocol built on TCP/IP
- Rapid global adoption

**Result:**
TCP/IP becomes THE standard for global networking

---

## Slide 25: 2000s and Beyond

**2000s:**
- OSI model: Fundamental part of networking education
- TCP/IP: Dominant protocol suite for Internet
- Continued expansion and innovation

**2010s-2020s:**
- Internet of Things (IoT) - billions of devices
- Cloud computing - distributed services
- Mobile networks - ubiquitous connectivity
- Software-Defined Networking (SDN)
- Network Function Virtualization (NFV)

**TCP/IP remains central, OSI guides understanding**

---

## Slide 26: Modern Networking Security

**Security at Each Layer:**

**Application:** HTTPS, S/MIME, SSH
**Transport:** TLS/SSL
**Network:** IPSec, VPNs
**Data Link:** WPA3 (Wi-Fi security)
**Physical:** Locked equipment, secure cabling

**Defense in Depth:**
Multiple layers of protection
- If one layer compromised, others provide backup

---

## Slide 27: Quality of Service (QoS)

**Why QoS Matters:**
- Real-time apps (voice, video) need priority
- Limited network capacity
- Not all traffic equally time-sensitive

**QoS Mechanisms:**
- Traffic classification and marking
- Priority queuing
- Bandwidth reservation
- Congestion management

**Use Cases:**
- VoIP (Voice over IP)
- Video conferencing
- Streaming media

---

## Slide 28: Troubleshooting with Layers

**Systematic Approach:**

**Layer 1 (Physical):**
- Check cables, connections, power
- Verify link lights

**Layer 2 (Data Link):**
- Check switch configuration
- Verify MAC addresses

**Layer 3 (Network):**
- Check IP addresses, routing
- Use ping, traceroute

**Layer 4 (Transport):**
- Check firewall rules, port numbers
- Verify TCP connections

**Layer 7 (Application):**
- Check application settings, logs

**Work through layers systematically to isolate problems**

---

## Slide 29: Tools for Learning Networking

**Simulation Tools:**
- Cisco Packet Tracer (free)
- GNS3, EVE-NG (advanced)

**Protocol Analysis:**
- Wireshark (packet capture and analysis)

**Virtualization:**
- VMware, VirtualBox
- Virtual network labs

**Cloud Platforms:**
- AWS, Azure, Google Cloud
- Free tiers for learning

**Certifications:**
- CompTIA Network+
- Cisco CCNA

---

## Slide 30: Career Applications

**Network Administrator:**
- Design, implement, maintain networks
- Configure routers, switches

**Network Engineer:**
- Optimize performance, plan capacity
- Advanced troubleshooting

**Security Professional:**
- Protect networks and data
- Implement defense in depth

**Cloud Architect:**
- Design cloud infrastructure
- Virtual networking

**Software Developer:**
- Build networked applications
- APIs, web services

**DevOps Engineer:**
- Automate infrastructure
- Container networking

---

## Slide 31: Key Takeaways

**Essential Concepts:**

✓ **Layered architecture** enables modular design
✓ **OSI (7 layers)** provides conceptual framework
✓ **TCP/IP (4 layers)** provides implementation
✓ **Encapsulation** structures data for transmission
✓ **Open standards** enabled global Internet
✓ **Each layer has specific responsibilities**
✓ Understanding layers essential for troubleshooting

**The Foundation:**
Principles from 1960s-1980s still guide networking today

---

## Slide 32: Connecting Lecture 1 & 2

**Lecture 1: Historical Foundations (1961-1978)**
- Packet switching theory → practice
- ARPANET demonstrated viability
- Ethernet solved LAN problem
- TCP development enabled internetworking

**Lecture 2: Standardization (1980s-present)**
- OSI model provided theoretical framework
- TCP/IP became practical standard
- Layer-by-layer functions defined
- Modern applications built on foundation

**Together:**
Complete understanding of networking fundamentals

---

## Slide 33: Questions & Discussion

**Topics to Consider:**

- Why did TCP/IP succeed over OSI in practice?
- How does understanding layers help troubleshooting?
- What layer does your favorite application use?
- How has cloud computing affected these models?
- What emerging tech will challenge these models?
- How do security threats span multiple layers?

---

## Slide 34: Next Steps

**Hands-On Practice:**
- Install Wireshark → analyze real traffic
- Try Cisco Packet Tracer → build virtual networks
- Explore your home network → identify devices

**Further Study:**
- Network+ certification materials
- TCP/IP protocol RFCs
- Network security fundamentals
- Cloud networking services

**Remember:**
Theory + practice = mastery
