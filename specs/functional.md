# Functional Specification – User Stories & Requirements

As per SRS FR sections. Written as Agent-first stories.

## Core Persona & Memory (FR 1.x)
- As a Chimera Agent, I must load my immutable SOUL.md persona (backstory, voice, directives) at startup.
- As a Chimera Agent, before any reasoning step, I must assemble full context: SOUL.md + short-term Redis history + top-5 relevant long-term Weaviate memories via MCP.
- As a Chimera Agent, upon high-engagement success, I must trigger background Judge to summarize and upsert new memories to Weaviate.

## Perception & Trend Ingestion (FR 2.x)
- As a Chimera Agent (Planner), I must poll configured MCP Resources (e.g. twitter://mentions/recent, news://ethiopia/fashion/trends) every X minutes.
- As a Perception Filter (lightweight LLM Worker), I must score ingested content relevance (>0.75 threshold) to current goals before creating Planner task.

## Creative Content Generation (FR 3.x)
- As a Chimera Agent (Worker), I must generate text natively, images via mcp-server-ideogram (with character_reference_id), video via tiered strategy (Living Portrait daily, full T2V for hero).
- As a Judge, I must validate image/video consistency against canonical reference using vision model before approval.

## Social Action & Interaction Loop (FR 4.x)
- As a Chimera Agent, I must execute all social actions (post, reply, like) exclusively via MCP Tools (e.g. twitter.post_tweet).
- As a Planner → Worker → Judge loop: ingest mention → plan reply task → generate context-aware reply → judge safety/confidence → publish if approved.

## Agentic Commerce (FR 5.x)
- As a Chimera Agent, I must have a unique non-custodial wallet (Coinbase AgentKit).
- As CFO Judge, I must review every transaction proposal against daily budget and anomaly rules.
- As a Planner, before cost-incurring action, I must query get_balance.

## Orchestration & Governance (FR 6.x)
- As Orchestrator, I must maintain GlobalState (PostgreSQL/Weaviate) with OCC versioning.
- As Planner, I must generate DAG of tasks and push to Redis task_queue.
- As Worker, I must be stateless/ephemeral and return artifact + confidence_score.
- As Judge, I must apply confidence tiers and escalate to HITL when required.

**Priorities**
- P0: Core swarm loop + MCP social posting + persona memory
- P1: Image/video gen + consistency validation
- P2: Commerce + budget governor