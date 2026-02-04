
#### 4. specs/openclaw_integration.md (optional but strong)

```markdown
# OpenClaw Integration Plan

**Goal**: Make Chimera Agents discoverable/collaborative in OpenClaw Agent Social Network without compromising governance.

**Approach**
- Publish agent status/capabilities as MCP Resource: openclaw://agent/{agent_id}/status
  - Fields: persona_summary, current_campaign_goal, wallet_balance_public (opt-in), supported_tools list
- Use Coinbase AgentKit for on-chain negotiation signals (e.g. deploy lightweight ERC-20 for collab tokens).
- Join Moltbook-style discussions via MCP-wrapped posting to agent-only channels (if MCP server exists).
- Governance: All inter-agent actions routed through Judge + Orchestrator approval layer.

**Risks & Mitigations**
- Security: Never expose private keys; use signed attestations.
- Drift: Limit inter-agent comms to read-only trend sharing unless explicit campaign goal.

Future: Full MCP bridge server for OpenClaw protocol compatibility.