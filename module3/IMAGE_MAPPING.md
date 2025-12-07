# Visual Assets Mapping for Networking Lectures

This document maps images from the original PowerPoints to the new presentation files.

---

## CS_Hierarchy.pptx Images
**Note:** This presentation is NOT for networking lectures, but images may be useful for other modules.

### Image Locations:

**Slide 3 - Example of Inheritance (OOP)**
- **File:** `cs_hierarchy_images/image5.png` (77 KB)
- **Content:** Code example showing Animal base class with Dog/Cat derived classes
- **Not relevant for networking lectures**

**Slide 4 - Example of Polymorphism**
- **File:** `cs_hierarchy_images/image6.png` (54 KB)
- **Content:** Code example demonstrating polymorphic behavior
- **Not relevant for networking lectures**

**Slide 5 - Example of Hierarchy Structure**
- **File:** `cs_hierarchy_images/image7.png` (18 KB)
- **Content:** Diagram showing class hierarchy benefits
- **Not relevant for networking lectures**

**Slide 12 - Hierarchy Concept**
- **File:** `cs_hierarchy_images/image1.png` (218 KB)
- **Content:** General hierarchy diagram or concept illustration
- **Possibly useful for explaining layered architecture concept**

**Slide 21 - File System Hierarchy (3 images)**
- **File 1:** `cs_hierarchy_images/image2.png` (57 KB)
- **File 2:** `cs_hierarchy_images/image3.png` (58 KB)
- **File 3:** `cs_hierarchy_images/image4.png` (92 KB)
- **Content:** Windows, Linux, Mac file system tree structures (side-by-side comparison)
- **Not relevant for networking lectures**

---

## Network_Models (1).pptx Images
**These images ARE relevant for networking lectures**

### Image Locations:

**Slide 23 - Brief History of Connecting Computers (1961)**
- **File:** `network_models_images/image1.png` (822 KB)
- **Original Context:** "1961: Leonard Kleinrock publishes his first paper on packet switching theory"
- **Likely Content:** Photo of Kleinrock or illustration of packet switching concept
- **Use in New Presentations:**
  - **Lecture 1, Slide 4:** Packet Switching Theory (1961) - Leonard Kleinrock
  - **Alternative:** Could also use on title slide for historical context

**Slide 26 - First Connection (1965)**
- **File:** `network_models_images/image2.png` (1.0 MB)
- **Original Context:** "1965: First computer-to-computer communication... Bell 103A Modem"
- **Likely Content:** Photo of Bell 103A modem or early computer connection
- **Use in New Presentations:**
  - **Lecture 1, Slide 7:** First Connection (1965) - Roberts & Merrill
  - Shows historical hardware that enabled first connection

---

## Recommended Image Placement for New Presentations

### Lecture 1 (lecture1_presentation_v2.md)

#### Historical Photos/Diagrams:

**Slide 1 (Title Slide):**
- Consider adding: Network diagram or Internet connectivity visual
- **Option:** Use `network_models_images/image1.png` for historical context

**Slide 4 (Packet Switching Theory - 1961):**
- **ADD:** `network_models_images/image1.png`
- Shows Kleinrock or packet switching concept

**Slide 6 (Analogy: Sending a Book):**
- **RECOMMEND:** Create new visual diagram
- Show circuit switching (dedicated truck) vs. packet switching (individual letters)
- Split-screen comparison illustration

**Slide 7 (First Connection - 1965):**
- **ADD:** `network_models_images/image2.png`
- Shows Bell 103A modem or early connection hardware

**Slide 10 (ARPANET: Initial Four Nodes):**
- **RECOMMEND:** Create new visual
- Map showing UCLA, SRI, UCSB, University of Utah with connecting lines
- Or diagram showing IMP structure

**Slide 14 (Ethernet Technology):**
- **RECOMMEND:** Create new visual
- Diagram showing CSMA/CD process
- Or coaxial cable ethernet topology

**Slide 15 (CSMA/CD: Managing Collisions):**
- **RECOMMEND:** Create new visual
- Flowchart showing listen → transmit → detect collision → backoff → retry

**Slide 22 (TCP/IP Split):**
- **RECOMMEND:** Create new visual
- Before: Single TCP block
- After: Separate TCP and IP blocks with defined responsibilities

**Slide 25 (Timeline):**
- **RECOMMEND:** Create timeline graphic
- Visual timeline from 1961-1978 with key milestones

### Lecture 2 (lecture2_presentation_v2.md)

#### Layer Diagrams & Models:

**Slide 6 (OSI Seven Layers):**
- **RECOMMEND:** Create layer diagram
- Seven colored boxes stacked vertically
- Each labeled with layer number, name, and key function

**Slide 17 (TCP/IP Four Layers):**
- **RECOMMEND:** Create layer diagram
- Four colored boxes stacked vertically
- Show correspondence to OSI layers

**Slide 18 (OSI vs TCP/IP):**
- **RECOMMEND:** Create side-by-side comparison diagram
- Two stacks showing how OSI 7 layers map to TCP/IP 4 layers
- Use colors to show relationships

**Slide 20 (Encapsulation Process):**
- **RECOMMEND:** Create encapsulation diagram
- Show data packet growing with each layer's header
- Visual representation of headers being added/removed

**Slide 22 (Network Hardware by Layer):**
- **RECOMMEND:** Create hardware placement diagram
- Show physical devices (router, switch, NIC) mapped to their layers

**Slide 28 (Troubleshooting with Layers):**
- **RECOMMEND:** Create troubleshooting flowchart
- Decision tree for systematic layer-by-layer diagnosis

---

## Additional Visual Recommendations

### Diagrams to Create:

1. **Packet Switching vs Circuit Switching**
   - Side-by-side comparison
   - Visual representation of resources being shared vs. dedicated

2. **ARPANET Growth Map**
   - Map of United States showing original 4 nodes
   - Optional: Expansion to more nodes

3. **Ethernet Evolution Timeline**
   - 10 Mbps → 100 Mbps → 1 Gbps → 10 Gbps → 40/100 Gbps → 400 Gbps
   - Show cable types changing (coax → twisted pair → fiber)

4. **TCP Three-Way Handshake**
   - Sequence diagram showing SYN, SYN-ACK, ACK
   - Client and server with arrows and labels

5. **OSI Layer Stack**
   - Professional-looking 7-layer diagram
   - Color-coded layers with icons

6. **TCP/IP Layer Stack**
   - 4-layer diagram
   - Show mapping to OSI model with dotted lines

7. **Encapsulation/De-encapsulation**
   - Data packet with headers being added layer by layer
   - Reverse process on receiving side

8. **IPv4 vs IPv6 Comparison**
   - Address format examples
   - Size comparison (32-bit vs 128-bit)

9. **Network Devices by Layer**
   - Hub (Layer 1), Switch (Layer 2), Router (Layer 3)
   - Show where each operates in the stack

10. **DNS Hierarchy Diagram**
    - Tree structure: Root → TLD → Authoritative
    - Example: www.example.com resolution

---

## Images Currently Available

### From CS_Hierarchy.pptx:
- ❌ OOP code examples (not relevant)
- ❌ File system hierarchies (not relevant)
- ⚠️ General hierarchy concept (image1.png) - potentially useful for explaining layered concepts

### From Network_Models (1).pptx:
- ✅ Historical photo/diagram (image1.png) - Kleinrock/packet switching (1961)
- ✅ Historical hardware (image2.png) - Bell 103A modem (1965)

---

## Action Items for Complete Visual Package

### Immediate Use (Existing Images):
1. ✅ Copy `network_models_images/image1.png` → Use in Lecture 1, Slide 4
2. ✅ Copy `network_models_images/image2.png` → Use in Lecture 1, Slide 7

### Create New (High Priority):
3. 🎨 OSI 7-layer diagram (for Lecture 2, Slide 6)
4. 🎨 TCP/IP 4-layer diagram (for Lecture 2, Slide 17)
5. 🎨 OSI vs TCP/IP side-by-side (for Lecture 2, Slide 18)
6. 🎨 Encapsulation diagram (for Lecture 2, Slide 20)
7. 🎨 Packet vs Circuit switching comparison (for Lecture 1, Slide 6)
8. 🎨 TCP three-way handshake (for Lecture 2, Slide 12)

### Create New (Medium Priority):
9. 🎨 ARPANET 4-node map (for Lecture 1, Slide 10)
10. 🎨 CSMA/CD flowchart (for Lecture 1, Slide 15)
11. 🎨 Timeline graphic 1961-1978 (for Lecture 1, Slide 25)
12. 🎨 Network devices by layer (for Lecture 2, Slide 22)

### Create New (Lower Priority):
13. 🎨 Ethernet evolution timeline
14. 🎨 IPv4 vs IPv6 visual comparison
15. 🎨 DNS hierarchy tree
16. 🎨 Troubleshooting decision tree

---

## Tools for Creating New Visuals

**Recommended Tools:**
- **Draw.io / diagrams.net** (free, web-based)
- **Lucidchart** (professional, easy templates)
- **PowerPoint** (built-in SmartArt and shapes)
- **Canva** (templates for infographics)
- **Google Slides** (collaborative, free)

**For Technical Diagrams:**
- **Visio** (Microsoft, professional)
- **OmniGraffle** (Mac)
- **yEd** (free, graph editor)

---

## Image Specifications for PowerPoint

**Recommended Settings:**
- Format: PNG (transparent background when possible)
- Resolution: 1920x1080 (or higher for detail)
- DPI: 150-300 for crisp display
- File size: Optimize to <500KB when possible

**Color Scheme:**
- Use consistent colors across diagrams
- Consider colorblind-friendly palettes
- Match presentation theme

---

## Files Included

Images have been extracted to:
- `cs_hierarchy_images/` - 7 images from CS_Hierarchy.pptx
- `network_models_images/` - 2 images from Network_Models (1).pptx

**Ready to use in new presentations!**
