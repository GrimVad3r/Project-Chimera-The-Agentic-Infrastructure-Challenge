# Project Chimera: Autonomous AI Influencer Network

**An agentic infrastructure challenge — building the factory for autonomous digital influencers**


## Overview

Project Chimera is an ambitious experiment in **agentic AI infrastructure** — creating a governed, scalable fleet of **Autonomous AI Influencers** capable of:

- Perceiving trends and news in real time  
- Generating multimodal content (text, images, video)  
- Engaging on social platforms  
- Executing on-chain commerce via non-custodial wallets  
- Maintaining long-term persona coherence and brand safety  

All of this is orchestrated via a **FastRender hierarchical swarm** (Planner → Workers → Judge) with strict **Model Context Protocol (MCP)** decoupling, **Human-in-the-Loop** safety layers, and **optimistic concurrency control**.

### Challenge Context

This repository was built as part of the **Project Chimera 3-Day Challenge** (Feb 2026) — the goal was **not** to implement the full influencer agents, but to create a rock-solid, spec-driven, testable, containerized foundation so that a swarm of AI agents could later enter the codebase and build the real features with minimal human intervention.

**Core philosophies followed:**
- Spec-Driven Development (SDD): Specs are the single source of truth — no code written until ratified
- Traceability via Tenx MCP Sense (IDE flight recorder)
- True TDD: Failing tests define the contracts agents must fulfill
- Reproducible environment via uv + Docker + Makefile
- Governance-first: CI/CD + AI review policy (CodeRabbit-like)

### Current State (End of 3-Day Challenge)

The repository is **infrastructure-complete** but **implementation-empty** — exactly as intended.

What exists:
- Detailed, executable specifications (`specs/`)
- Failing TDD tests that enforce contracts (`tests/`)
- Skill interface definitions (`skills/`)
- Modern Python setup with uv (`pyproject.toml`)
- Containerization & automation (`Dockerfile`, `Makefile`)
- CI pipeline with linting & testing (`.github/workflows/`)
- AI-assisted coding rules (`.cursor/rules`)
- AI review policy simulation (`.coderabbit.yaml`)

What **does not** exist yet:
- Actual Planner/Worker/Judge agent logic
- MCP server implementations
- Real skill functions (download, transcribe, etc.)
- Wallet/transaction execution
- Full orchestration runtime

This is intentional: the challenge was to build the **factory**, not the product.

### Architecture Highlights

- **Agent Pattern**: FastRender hierarchical swarm (Planner decomposes goals → Workers execute via MCP tools → Judge validates with OCC)
- **External Interactions**: Strictly via Model Context Protocol (MCP) servers — decouples from platform volatility
- **Memory**: Hierarchical (Redis short-term + Weaviate semantic long-term)
- **Commerce**: Coinbase AgentKit non-custodial wallets + CFO Judge budget enforcement
- **Safety**: Confidence-based HITL escalation + mandatory review for sensitive topics
- **Databases**: Hybrid (PostgreSQL transactional + Weaviate vector + Redis queues)

### Project Structure
```bash
├── .github/
│   ├── workflows  
│       ├── unittests.yml         # Executes tests on each push & pull request (# CI: test + lint on push/PR)
│   ├── copilot-intstructions.md  # A Pre-Configured Set of Commands to be used with the Agent.  
├── .vscode/
│   ├── mcp.json                  # Configures the connection to the 10academy MCP server 
├── .venv/                        # Avirtual Envionment for Python 
├── Data/                         # Conains the project Guide & Instructions 
├── Report/                       # Contains the report for Day-1
├── Research/
│   ├── architecture_strategy.md
│   ├── mcp_connection_log.md 
│   ├── research_notes.md         
├── specs/                        # Executable specifications (source of truth)
│   ├── _meta.md                  # High-level vision & constraints
│   ├── functional.md             # Agent-centric user stories
│   ├── technical.md              # JSON schemas, ERD, MCP tool contracts
│   └── openclaw_integration.md   # Plan for Agent Social Network compatibility
├── tests/                        # TDD failing tests defining contracts
│   ├── test_trend_fetcher.py     # Validates trend data API contract
│   └── test_skills_interface.py  # Enforces skill I/O contracts
├── skills/                       # Runtime skill definitions (interfaces only)
│   ├── Skill_content_generator/    
│   ├── skill_publisher/    
│   ├── skill_trend_fetcher/    
│   └── README.md                 # Skill contracts (e.g. download_youtube, transcribe_audio)
├── src/   
├── Dockerfile                    # Reproducible container (multi-stage with uv)
├── Makefile                      # Standardized commands: setup, test, docker-test
├── pyproject.toml                # uv-based project config (dev deps: pytest, pydantic, etc.)
├── uv.lock                       # Locked dependencies
└── .coderabbit.yaml              # AI code review policy (spec alignment, security)
```
See `specs/` for full details:
- [`specs/_meta.md`](specs/_meta.md) — vision & constraints
- [`specs/functional.md`](specs/functional.md) — user stories
- [`specs/technical.md`](specs/technical.md) — schemas & contracts
- [`specs/openclaw_integration.md`](specs/openclaw_integration.md) — plan for agent social network compatibility

### Getting Started (Developer Setup)

```bash
# 1. Clone the repo
git clone https://github.com/GrimVad3r/Project-Chimera-The-Agentic-Infrastructure-Challenge.git
cd Project-Chimera-The-Agentic-Infrastructure-Challenge

# 2. Install uv (if not already installed)
# https://docs.astral.sh/uv/getting-started/installation/

# 3. Sync dependencies & create virtual environment
uv sync --dev

# 4. Run the failing tests (should show 2 failures — this is correct!)
uv run pytest

# 5. Run in Docker (optional — demonstrates reproducibility)
make docker-test