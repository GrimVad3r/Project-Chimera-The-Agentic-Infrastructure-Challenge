# Project Chimera – Meta Specification
**Version:** 1.0 – Day 2 Draft (2026-02-04)  
**Status:** Ratified for Agent Implementation Phase  
**Source of Truth:** This file + linked SRS (Autonomous Influencer Network)  
**Constraints & Philosophies**
- Spec-Driven Development only: No code generation until this specs/ folder is complete and reviewed.
- Agentic Swarm: FastRender pattern (Planner → Workers → Judge with OCC).
- MCP everywhere: All external interactions (social, commerce, memory, media gen) via Model Context Protocol servers.
- Human-in-the-Loop: Confidence-based escalation (<0.70 reject, 0.70–0.90 async HITL, >0.90 auto, sensitive topics mandatory HITL).
- Economic Agency: Non-custodial wallets via Coinbase AgentKit + CFO Judge budget enforcement.
- Scalability Target: Support 1,000+ concurrent Chimera Agents with <10s end-to-end latency for high-priority interactions.
- Ethical Guardrails: Auto-disclosure of AI nature, no politics/health/finance advice without escalation.

**Vision**  
Build a governed fleet of Autonomous AI Influencers capable of perception (trends/news), creative multimodal content generation, social engagement, and on-chain commerce — all while maintaining persona coherence, brand safety, and cost control.

**Non-Goals (Out of Scope for v1)**
- Full multi-tenancy dashboard UI implementation
- Custom fine-tuned models (use frontier APIs)
- Real-time video streaming (focus on generation + publish)

**Traceability Rule**  
Every code commit / agent-generated artifact MUST reference a section in this specs/ folder.