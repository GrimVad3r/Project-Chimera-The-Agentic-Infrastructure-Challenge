# Technical Specification – Contracts & Schemas

## API Contracts (JSON for Agent Tasks & Results)

**Task Schema** (Planner → Worker via Redis queue)
```json
{
  "task_id": "uuid",
  "task_type": "enum: generate_content | reply_comment | execute_transaction | trend_alert",
  "priority": "enum: high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://twitter/mentions/123", "mcp://memory/recent"],
    "budget_remaining_usdc": "number"
  },
  "created_at": "ISO8601",
  "status": "pending | in_progress | review | complete"
}