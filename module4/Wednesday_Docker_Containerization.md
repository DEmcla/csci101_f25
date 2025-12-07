# [Module 4] Docker: Containerization Overview
## Introduction to Containers and Modern Deployment

### Class Overview (75 minutes)

This lecture provides an introduction to containerization and Docker. You'll encounter these tools in future courses and industry work.

| Segment | Topic | Time |
|---------|-------|------|
| 1 | The Deployment Problem: "It Works on My Machine" | 10 min |
| 2 | What is Containerization? | 15 min |
| 3 | Containers vs Virtual Machines | 10 min |
| 4 | Docker: The Container Standard | 15 min |
| 5 | Core Docker Concepts: Images, Containers, Registries | 15 min |
| 6 | Demo: Running Your First Container | 5 min |
| 7 | Wrap-up & Exit Ticket | 5 min |

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. **Explain** the "works on my machine" problem that containerization solves
2. **Define** containerization and its benefits for software deployment
3. **Compare** containers and virtual machines, identifying key differences
4. **Identify** Docker's role as the industry-standard container platform
5. **Describe** core Docker concepts: images, containers, and registries
6. **Recognize** real-world use cases for containerization

---

## Key Terms for Today

| Term | Definition |
|------|------------|
| **Container** | A lightweight, standalone package containing everything needed to run a piece of software |
| **Containerization** | The process of packaging an application with all its dependencies into a container |
| **Docker** | The most popular platform for building, running, and sharing containers |
| **Image** | A read-only template (blueprint) used to create containers |
| **Docker Hub** | A public registry where Docker images are stored and shared |
| **Virtual Machine (VM)** | A complete computer system simulated in software, including its own operating system |
| **Dockerfile** | A text file containing instructions to build a Docker image |
| **Registry** | A storage and distribution system for container images |

---

## 1. The Deployment Problem: "It Works on My Machine"

### A Story Every Developer Knows

**Scene: A software development team**

```
Developer: "I finished the feature! It works perfectly!"

QA Tester: "It's not working on my machine."

Developer: "That's weird... it works on MY machine."

Operations: "It crashed in production."

Developer: "But... it works on my machine! 😭"
```

This is one of the most common problems in software development.

### Why Does This Happen?

Software doesn't run in isolation. It depends on many things:

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR APPLICATION                         │
├─────────────────────────────────────────────────────────────┤
│  Dependencies:                                              │
│  ├── Python 3.11.2 (not 3.10, not 3.12)                    │
│  ├── PostgreSQL 15.1                                        │
│  ├── Redis 7.0                                              │
│  ├── 47 Python packages (specific versions)                 │
│  ├── System libraries (OpenSSL, libffi, etc.)              │
│  └── Environment variables (DATABASE_URL, API_KEY, etc.)   │
├─────────────────────────────────────────────────────────────┤
│  Operating System: Ubuntu 22.04                             │
└─────────────────────────────────────────────────────────────┘
```

**The problem:** Different computers have different:
- Operating systems (Windows, macOS, Linux)
- Software versions (Python 3.10 vs 3.11)
- System configurations
- Installed libraries
- Environment variables

### The Cost of "Works on My Machine"

| Impact | Example |
|--------|---------|
| **Wasted time** | Hours debugging environment differences |
| **Delayed releases** | "We can't deploy until we fix the staging server" |
| **Production outages** | Code that worked in testing fails live |
| **Onboarding friction** | New developers spend days setting up |
| **Inconsistent testing** | Tests pass locally, fail in CI/CD |

> "We need a way to ship the entire environment, not just the code."

**Enter: Containerization**

---

## 2. What is Containerization?

### The Shipping Container Analogy

Before standardized shipping containers (invented in 1956):

```
OLD WAY: Shipping goods internationally

┌─────────┐     ┌─────────┐     ┌─────────┐
│  Loose  │     │Different│     │ Unload, │
│  Cargo  │ --> │  Ships  │ --> │ Reload  │ --> Destination
│ (chaos) │     │(custom) │     │(manual) │
└─────────┘     └─────────┘     └─────────┘

Problems:
- Each item packed differently
- Loading/unloading took days
- Theft and damage common
- Different handling for each port
```

After standardized containers:

```
NEW WAY: Standardized shipping containers

┌─────────┐     ┌─────────┐     ┌─────────┐
│Standard │     │   Any   │     │  Crane  │
│Container│ --> │  Ship   │ --> │  Lift   │ --> Destination
│(uniform)│     │(standard)│    │(standard)│
└─────────┘     └─────────┘     └─────────┘

Benefits:
- Same container works everywhere
- Automated loading/unloading
- Secure and protected
- Efficient global shipping
```

**Software containers work the same way!**

### Software Containerization

A **container** packages your application with everything it needs:

```
┌─────────────────────────────────────────────────────────────┐
│                     CONTAINER                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               Your Application Code                  │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │     Runtime (Python 3.11, Node.js 18, Java 17)      │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │    Libraries & Dependencies (exact versions)         │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │        System Tools & Configuration                  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Key insight:** The container runs identically everywhere because it includes *everything* the application needs.

### Benefits of Containerization

| Benefit | Explanation |
|---------|-------------|
| **Consistency** | Same container runs the same way on any machine |
| **Isolation** | Containers don't interfere with each other or the host system |
| **Portability** | Move containers between laptop, server, cloud |
| **Efficiency** | Containers share the host OS kernel, using fewer resources |
| **Speed** | Containers start in seconds (vs. minutes for VMs) |
| **Scalability** | Easy to run multiple copies for high-traffic applications |

---

## Checkpoint #1: Understanding the Problem

**Answer these questions:**

1. What does "it works on my machine" mean, and why is it a problem?
2. Name three things (besides code) that your application might depend on.
3. How is a software container similar to a physical shipping container?

<details>
<summary>Click for Answers</summary>

1. **"It works on my machine"** means the software runs correctly on the developer's computer but fails elsewhere. It's a problem because it wastes time debugging, delays deployments, and can cause production failures.

2. **Dependencies include (any three):**
   - Programming language runtime (Python, Node.js, Java)
   - Database software (PostgreSQL, MySQL, MongoDB)
   - External libraries and packages
   - System libraries (OpenSSL, etc.)
   - Environment variables and configuration
   - Operating system version

3. **Similarity:** Just as shipping containers standardize how goods are packaged and transported (same container works on any ship, truck, or crane), software containers standardize how applications are packaged and deployed (same container runs on any machine with Docker).

</details>

---

## 3. Containers vs Virtual Machines

### What's a Virtual Machine?

A **Virtual Machine (VM)** is a complete computer simulated in software.

```
┌─────────────────────────────────────────────────────────────┐
│                    VIRTUAL MACHINE                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   Application                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │              Libraries & Binaries                    │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │             Guest Operating System                   │   │
│  │           (Full Windows, Linux, etc.)               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         ↕️                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         Hypervisor (VMware, VirtualBox)             │   │
│  └─────────────────────────────────────────────────────┘   │
│                         ↕️                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Host Operating System                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                      Hardware                              │
└─────────────────────────────────────────────────────────────┘
```

**Key point:** Each VM has its own **complete operating system**.

### How Containers Are Different

Containers share the host operating system's kernel:

```
┌─────────────────────────────────────────────────────────────┐
│                      CONTAINERS                             │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │   App A   │  │   App B   │  │   App C   │               │
│  ├───────────┤  ├───────────┤  ├───────────┤               │
│  │   Libs    │  │   Libs    │  │   Libs    │               │
│  └───────────┘  └───────────┘  └───────────┘               │
│         ↕️              ↕️              ↕️                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Container Runtime (Docker)              │   │
│  └─────────────────────────────────────────────────────┘   │
│                         ↕️                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │          Host Operating System (shared kernel)       │   │
│  └─────────────────────────────────────────────────────┘   │
│                      Hardware                              │
└─────────────────────────────────────────────────────────────┘
```

**Key point:** Containers share the host OS kernel - no separate OS per container!

### Side-by-Side Comparison

| Aspect | Virtual Machine | Container |
|--------|-----------------|-----------|
| **Size** | Gigabytes (includes full OS) | Megabytes (no OS) |
| **Startup time** | Minutes | Seconds |
| **Resource usage** | Heavy (needs RAM for each OS) | Light (shares host OS) |
| **Isolation** | Complete (separate OS) | Process-level |
| **Portability** | Limited by hypervisor | Highly portable |
| **Use case** | Running different OS, strong isolation | Application deployment |

### An Analogy: Houses vs Apartments

**Virtual Machines are like separate houses:**
- Each house has its own foundation, plumbing, electrical
- Complete isolation from neighbors
- Expensive and takes long to build
- You maintain everything yourself

**Containers are like apartments:**
- Share building infrastructure (plumbing, electrical, foundation)
- Still have your own private space
- More efficient use of resources
- Quick to move in
- Building management handles shared systems

### When to Use Each

| Use Virtual Machines When... | Use Containers When... |
|------------------------------|------------------------|
| Running different operating systems | Deploying applications |
| Maximum security isolation needed | Microservices architecture |
| Legacy software requires specific OS | Cloud-native development |
| Testing OS-level changes | Scaling applications |

---

## Checkpoint #2: VMs vs Containers

**True or False:**

1. Containers include a complete operating system like VMs do.
2. Containers start faster than virtual machines.
3. Virtual machines provide stronger isolation than containers.
4. You can run Linux containers on a Windows host without virtualization.

<details>
<summary>Click for Answers</summary>

1. **False.** Containers share the host OS kernel - they don't include their own operating system.
2. **True.** Containers start in seconds because they don't need to boot an OS.
3. **True.** VMs have complete hardware and OS isolation; containers share the kernel.
4. **False.** Linux containers need a Linux kernel. On Windows/Mac, Docker uses a lightweight VM to provide a Linux kernel. (Windows containers exist but are different.)

</details>

---

## 4. Docker: The Container Standard

### A Brief History

| Year | Event |
|------|-------|
| 2008 | Linux containers (LXC) available but complex |
| 2013 | Docker launched - made containers easy to use |
| 2014 | Docker explodes in popularity |
| 2017 | Kubernetes becomes standard for container orchestration |
| Today | Docker is synonymous with containers |

**Docker's genius:** It didn't invent containers - it made them **easy**.

### Why Docker Won

Before Docker, using containers required:
- Deep Linux knowledge
- Complex configuration
- Manual setup of isolation, networking, storage
- No standard way to share containers

Docker provided:
- Simple commands (`docker run`, `docker build`)
- Dockerfile for reproducible builds
- Docker Hub for sharing images
- Cross-platform support
- Great developer experience

```bash
# Before Docker (complex Linux commands)
# Pages of configuration, kernel features, cgroups, namespaces...

# With Docker (one command)
docker run -p 80:80 nginx
```

### Docker Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐         ┌─────────────────────────┐      │
│   │   Docker    │  <--->  │     Docker Daemon       │      │
│   │    CLI      │         │  (background service)    │      │
│   │  (commands) │         │                         │      │
│   └─────────────┘         └───────────┬─────────────┘      │
│                                       │                     │
│                    ┌──────────────────┼──────────────────┐ │
│                    │                  │                  │ │
│               ┌────▼────┐       ┌─────▼─────┐     ┌──────▼──┐
│               │ Images  │       │ Containers│     │ Networks│
│               └─────────┘       └───────────┘     └─────────┘
│                    │                                        │
│                    ▼                                        │
│            ┌─────────────┐                                  │
│            │ Docker Hub  │  (or other registries)           │
│            │  (remote)   │                                  │
│            └─────────────┘                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Components:**
- **Docker CLI**: Commands you type (`docker run`, `docker build`)
- **Docker Daemon**: Background service that does the actual work
- **Images**: Blueprints for creating containers
- **Containers**: Running instances of images
- **Registry**: Storage for images (Docker Hub)

---

## 5. Core Docker Concepts

### 5.1 Images: The Blueprint

A **Docker Image** is a read-only template for creating containers.

**Think of it like:**
- A **recipe** - instructions to create something
- A **class** in programming - defines what objects look like
- A **snapshot** - frozen point-in-time of a system

**Images are built in layers:**

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Image                            │
├─────────────────────────────────────────────────────────────┤
│  Layer 4: COPY . /app           (your application code)     │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: RUN pip install       (install dependencies)      │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: WORKDIR /app          (set working directory)     │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: Python 3.11           (base image)                │
├─────────────────────────────────────────────────────────────┤
│  Layer 0: Alpine Linux          (minimal OS)                │
└─────────────────────────────────────────────────────────────┘
```

**Why layers matter:**
- Layers are cached and reused
- If only your code changes, only the top layer rebuilds
- Multiple images can share base layers (saves space)

### 5.2 Containers: Running Instances

A **Container** is a running instance of an image.

```
Image vs Container:

   ┌─────────────┐                    ┌─────────────┐
   │             │                    │  Container  │
   │   IMAGE     │  -- docker run --> │  (running)  │
   │  (recipe)   │                    │             │
   └─────────────┘                    └─────────────┘
                                             │
                                             ▼
You can run multiple                  ┌─────────────┐
containers from one image:            │  Container  │
                                      │  (running)  │
   ┌─────────────┐                    └─────────────┘
   │             │                           │
   │   nginx     │  ------------------>      ▼
   │   image     │                    ┌─────────────┐
   │             │                    │  Container  │
   └─────────────┘                    │  (running)  │
                                      └─────────────┘
```

**Key points:**
- One image can create many containers
- Containers have their own writable layer
- Containers are ephemeral (temporary) by default
- Stopping a container doesn't delete it

### 5.3 Dockerfile: Building Images

A **Dockerfile** is a text file with instructions to build an image.

```dockerfile
# Example Dockerfile for a Python web application

# Start from an official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]
```

**Common Dockerfile instructions:**

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image to start from |
| `WORKDIR` | Set working directory |
| `COPY` | Copy files from host to image |
| `RUN` | Execute commands during build |
| `ENV` | Set environment variables |
| `EXPOSE` | Document which ports the container uses |
| `CMD` | Default command when container runs |

### 5.4 Docker Hub: Sharing Images

**Docker Hub** is like GitHub for container images.

```
┌─────────────────────────────────────────────────────────────┐
│                       Docker Hub                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Official Images:                                           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │  nginx  │ │ python  │ │  node   │ │postgres │          │
│  │ 1B+ ⬇️  │ │ 1B+ ⬇️  │ │ 1B+ ⬇️  │ │ 1B+ ⬇️  │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
│                                                             │
│  Community Images:                                          │
│  ┌─────────────────────────────────────────────────┐       │
│  │  user/my-app    |    org/custom-image    |  ... │       │
│  └─────────────────────────────────────────────────┘       │
│                                                             │
│  [Search images]  [Create repository]                       │
└─────────────────────────────────────────────────────────────┘
```

**Image naming convention:**

```
docker.io  /  library  /  nginx  :  1.25
─────────     ───────     ─────     ────
 registry     namespace    name     tag

Examples:
- nginx              (official, latest)
- nginx:1.25         (official, specific version)
- myuser/myapp       (user's image)
- myuser/myapp:v2.0  (user's image, versioned)
```

---

## Checkpoint #3: Docker Concepts

**Fill in the blanks:**

1. A Docker _______ is a blueprint for creating containers.
2. A running instance of an image is called a _______.
3. The file containing instructions to build an image is called a _______.
4. Docker _______ is a public registry for sharing images.

<details>
<summary>Click for Answers</summary>

1. **image** - A Docker image is a blueprint for creating containers.
2. **container** - A running instance of an image is called a container.
3. **Dockerfile** - The file containing instructions to build an image is called a Dockerfile.
4. **Hub** - Docker Hub is a public registry for sharing images.

</details>

---

## 6. Demo: Running Your First Container

### Basic Docker Commands

```bash
# Pull an image from Docker Hub
docker pull nginx

# Run a container
docker run nginx

# Run a container in the background (-d = detached)
docker run -d nginx

# Run with port mapping (-p host:container)
docker run -d -p 8080:80 nginx

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# List images
docker images

# Remove an image
docker rmi nginx
```

### Live Demo: Running nginx

```bash
# Step 1: Pull the nginx image
$ docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
...
Status: Downloaded newer image for nginx:latest

# Step 2: Run nginx container with port mapping
$ docker run -d -p 8080:80 nginx
a1b2c3d4e5f6g7h8i9j0...

# Step 3: Visit http://localhost:8080 in your browser
# You'll see "Welcome to nginx!"

# Step 4: Check running containers
$ docker ps
CONTAINER ID   IMAGE   STATUS         PORTS
a1b2c3d4e5f6   nginx   Up 2 minutes   0.0.0.0:8080->80/tcp

# Step 5: Stop the container
$ docker stop a1b2c3d4e5f6
a1b2c3d4e5f6
```

**What just happened?**
1. Downloaded nginx image (pre-built web server)
2. Created and started a container from that image
3. Mapped port 8080 on your computer to port 80 in the container
4. nginx is now serving web pages!

---

## Real-World Use Cases

### Who Uses Docker?

| Company | How They Use Docker |
|---------|---------------------|
| **Spotify** | Microservices architecture, 1000+ services |
| **Netflix** | Container-based deployment, millions of containers daily |
| **PayPal** | Consistent dev/prod environments |
| **NASA** | Scientific computing workloads |
| **Expedia** | Rapid deployment of travel services |

### Common Use Cases

```
┌─────────────────────────────────────────────────────────────┐
│                    Docker Use Cases                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔧 Development                                             │
│     - Consistent environments for all team members          │
│     - No more "works on my machine"                         │
│     - Quick setup for new developers                        │
│                                                             │
│  🧪 Testing                                                 │
│     - Isolated test environments                            │
│     - Run tests in production-like conditions               │
│     - Easy cleanup after tests                              │
│                                                             │
│  🚀 Deployment                                              │
│     - Same container in dev, staging, production            │
│     - Blue-green deployments                                │
│     - Easy rollbacks                                        │
│                                                             │
│  📈 Scaling                                                 │
│     - Run multiple container copies                         │
│     - Kubernetes orchestration                              │
│     - Handle traffic spikes                                 │
│                                                             │
│  🏠 Self-Hosting                                            │
│     - Run services at home (media servers, etc.)            │
│     - Easy backup and migration                             │
│     - Isolated applications                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary: The Docker Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    Docker Workflow                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Write Code  →  Create Dockerfile  →  Build Image          │
│       │                │                    │               │
│       ▼                ▼                    ▼               │
│   ┌───────┐      ┌───────────┐        ┌─────────┐          │
│   │app.py │      │Dockerfile │  --->  │  Image  │          │
│   └───────┘      └───────────┘        └────┬────┘          │
│                                            │               │
│         ┌──────────────────────────────────┼──────────┐    │
│         │                                  │          │    │
│         ▼                                  ▼          ▼    │
│   ┌───────────┐                      ┌─────────┐ ┌───────┐ │
│   │ Docker Hub│  <-- docker push --> │Container│ │Container│
│   │ (share)   │                      │(laptop) │ │(server)│ │
│   └───────────┘                      └─────────┘ └───────┘ │
│                                                             │
│                  Same image runs identically everywhere!    │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Point |
|---------|-----------|
| **The Problem** | "Works on my machine" wastes time and causes failures |
| **Containerization** | Packages app + dependencies into portable units |
| **VMs vs Containers** | VMs include full OS; containers share host kernel |
| **Docker** | Made containers easy and became the industry standard |
| **Image** | Read-only template/blueprint for containers |
| **Container** | Running instance of an image |
| **Dockerfile** | Instructions to build an image |
| **Docker Hub** | Public registry to share images |

---

## Exit Ticket

**Before you leave, answer these questions:**

1. A teammate says "Why don't we just use virtual machines instead of Docker?" What's one key advantage containers have over VMs?

2. Explain in your own words: What's the difference between a Docker image and a Docker container?

3. Your company's website needs to handle a sudden spike in traffic. How might containers help solve this problem?

---

## Looking Back and Ahead

**Monday (GitHub):** We learned how to track and share code changes
**Today (Docker):** We learned how to package and deploy applications consistently

**Together:** Modern development workflow
- Code changes tracked in GitHub
- Application packaged in Docker containers
- Consistent deployment anywhere

---

*Module 4, Lecture 2 | CSCI 101 | Fall 2025*
