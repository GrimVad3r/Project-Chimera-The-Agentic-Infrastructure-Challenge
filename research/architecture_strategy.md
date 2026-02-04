# Architecture Strategy – Project Chimera
**Version:** Day 1 Draft (Feb 04, 2026)  
**Goal:** High-level decisions before specs/code (Task 1.2)

## Chosen Agent Pattern
**FastRender Hierarchical Swarm (Planner – Worker – Judge)**  
- **Why this over Sequential Chain or Flat Swarm?**  
  - Sequential: Too slow/linear for parallel content gen/replies (e.g., 50 comments at once).  
  - Flat: No quality gate → hallucinations cascade.  
  - Hierarchical with Planner (decomposes goals, dynamic replan), stateless Workers (execute MCP tools fast), Judge (validate, OCC commit, escalate) → balances speed, quality, safety.  
  Matches SRS exactly; proven in experiments (FastRender browser swarm).

## Human-in-the-Loop Placement
**Primarily at Judge layer + Orchestrator Dashboard**  
- Judge auto-approves >0.90 confidence, async queues 0.70–0.90, rejects/escalates <0.70 or sensitive topics.  
- Human reviewers (via lightweight ReviewCard UI) handle only escalated/high-risk items (politics, legal claims, high-spend tx).  
- Keeps velocity high while enforcing "Management by Exception".

## Database Strategy for High-Velocity Video Metadata
**Hybrid Approach (Start with Postgres-centric)**  
- **PostgreSQL** (core transactional): campaigns, agent configs, wallet tx logs, structured metadata (JSONB columns for flexibility). ACID critical for commerce.  
- **Weaviate** (vector DB): long-term semantic memory, persona evolution, trend clustering.  
- **Redis**: short-term episodic cache, task/review queues.  
- **High-velocity consideration** (views, engagement spikes, timestamps): If Postgres write bottleneck appears → add TimescaleDB (time-series extension) or evaluate Cassandra for pure append-heavy metadata.  
  Rationale: Postgres + extensions covers 90% use cases with strong consistency for wallets/ledgers; avoid premature NoSQL split.

## High-Level Topology (Mermaid Diagram)

```mermaid
graph TD
    Orchestrator[Orchestrator Dashboard<br>(Human Super-Orchestrator)] --> Planner[Planner Agent<br>(Goal → Task DAG)]
    Planner --> TaskQueue[Task Queue<br>(Redis)]
    TaskQueue --> Workers[Worker Pool<br>(Stateless, MCP Tools)]
    Workers --> ReviewQueue[Review Queue<br>(Redis)]
    ReviewQueue --> Judge[Judge Agent<br>(Validate + OCC Commit)]
    Judge --> GlobalState[Global State<br>(PostgreSQL + Weaviate)]
    Judge -.-> HITL[Human Reviewers<br>(Dashboard Queue)]
    Workers --> MCP[MCP Servers<br>(Twitter, Coinbase, Image/Video Gen, etc.)]
    GlobalState --> Planner