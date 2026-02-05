# Architecture Strategy – Project Chimera
**Version:** Day 1 Draft (February 04, 2026)  
**Scope:** Pre-specification architectural decisions (Task 1.2)  
**Objective:** Establish system-level constraints, patterns, and trade-offs before formal specs or implementation

---

## 1. Architectural North Star

Project Chimera is designed as a **governed autonomous agent platform**, not a prompt-driven content bot.  
All architectural decisions are evaluated against four non-negotiable properties:

1. **Scalability through Parallelism** – support simultaneous content generation, engagement, and negotiation.
2. **Governance & Safety** – deterministic quality control, escalation, and auditability.
3. **Economic Correctness** – strong consistency for wallets, budgets, and transactions.
4. **Traceability** – every action attributable, inspectable, and reversible where possible.

This document captures early directional decisions that constrain downstream specs and code.

---

## 2. Chosen Agent Pattern

### FastRender Hierarchical Swarm  
**Planner → Worker → Judge**

This pattern is selected as the *default execution model* for Chimera agents.

---

### Why Not Sequential Chains?
Sequential chains introduce:
- Linear latency (unacceptable for bursty workloads like comment floods or trend hijacking)
- Single-point-of-failure reasoning
- Poor utilization of parallel compute

Sequential execution is acceptable for narrow reasoning tasks but fails for real-time influencer operations.

---

### Why Not Flat Swarms?
Flat swarms maximize throughput but lack:
- Centralized quality control
- Deterministic commit semantics
- Containment against hallucination cascades

In practice, flat swarms amplify small reasoning errors into system-wide failures—especially dangerous when agents have economic agency.

---

### Why Hierarchical Swarm Wins
The FastRender hierarchical swarm provides a **clean separation of concerns**:

- **Planner**
  - Converts high-level intent into a task DAG
  - Dynamically replans based on state feedback
  - Maintains strategic coherence across parallel work

- **Workers**
  - Stateless, horizontally scalable
  - Execute narrow tasks via MCP tools (posting, rendering, querying, transacting)
  - Designed for fast failure and retry

- **Judge**
  - Validates outputs against specs, policy, and confidence thresholds
  - Performs OCC-style commits to global state
  - Triggers escalation or rollback on violations

This architecture balances **speed, correctness, and safety**, and matches the Chimera SRS exactly.  
It is also empirically validated by prior FastRender swarm experiments in browser and tool-agent contexts.

---

## 3. Human-in-the-Loop (HITL) Strategy

### Placement: Judge Layer + Orchestrator Dashboard

Human oversight is introduced **by exception**, not by default.

---

### Confidence-Based Control
- **Confidence ≥ 0.90**
  - Auto-approved
  - Committed immediately
- **Confidence 0.70 – 0.90**
  - Asynchronous human review queue
  - Agent continues with other tasks
- **Confidence < 0.70**
  - Hard stop
  - Mandatory human intervention

---

### Mandatory HITL Domains
Regardless of confidence score:
- Political messaging
- Legal or medical claims
- High-value financial transactions
- Reputation-sensitive brand interactions

---

### Rationale
This model enforces *management by exception*:
- Humans intervene only where automation risk is high
- Routine operations remain fully autonomous
- Review load scales sublinearly with agent output

The Orchestrator Dashboard acts as a **control plane**, not a micromanagement interface.

---

## 4. Data & Storage Strategy

### Hybrid, Postgres-Centric Architecture (Initial Phase)

The data layer is intentionally conservative to preserve correctness and debuggability.

---

### PostgreSQL (System of Record)
Primary responsibilities:
- Campaign definitions
- Agent configurations
- Wallet balances and transaction logs
- Budget enforcement
- Structured metadata (via JSONB)

**Why Postgres?**
- ACID guarantees are mandatory for economic agency
- Mature tooling, observability, and migration paths
- JSONB allows schema evolution without early rigidity

---

### Weaviate (Semantic Memory)
Responsibilities:
- Long-term persona memory
- Content embeddings
- Trend and audience clustering
- Retrieval-augmented generation (RAG)

Weaviate is explicitly *not* a source of truth—only an advisory memory layer.

---

### Redis (Ephemeral State)
Responsibilities:
- Task queues
- Review queues
- Short-term episodic context
- Rate limiting and debouncing

Redis failures must be recoverable without data loss.

---

### High-Velocity Telemetry (Future Scaling)
Metrics such as:
- View counts
- Engagement spikes
- Timestamped interactions

Initial approach:
- PostgreSQL with JSONB and/or TimescaleDB extension

Escalation path:
- Introduce Cassandra-style append-only stores **only if**
  sustained write throughput exceeds Postgres capabilities.

This avoids premature fragmentation while preserving a clear scaling path.

---

## 5. MCP as a Hard Architectural Boundary

All external interactions occur **exclusively via MCP servers**:
- Social platforms (e.g., Twitter/X, TikTok)
- Rendering pipelines (image/video)
- Financial systems (Coinbase AgentKit)
- Observability and telemetry

Benefits:
- Tool decoupling
- Auditability
- Hot-swappable integrations
- Unified permission and policy enforcement

No agent may call external systems directly.

---

## 6. High-Level System Topology

```mermaid
graph TD
    Orchestrator["Orchestrator Dashboard<br/>(Human Super-Orchestrator)"]
        --> Planner["Planner Agent<br/>(Goal → Task DAG)"]

    Planner --> TaskQueue[Task Queue<br/>(Redis)]

    TaskQueue --> Workers["Worker Pool<br/>(Stateless, MCP-bound)"]

    Workers --> ReviewQueue[Review Queue<br/>(Redis)]
    ReviewQueue --> Judge["Judge Agent<br/>(Validate + OCC Commit)"]

    Judge --> GlobalState["Global State<br/>(PostgreSQL + Weaviate)"]
    Judge -. Escalate .-> HITL["Human Reviewers<br/>(Dashboard Queue)"]

    Workers --> MCP["MCP Servers<br/>(Social, Finance, Media, Telemetry)"]

    GlobalState --> Planner
