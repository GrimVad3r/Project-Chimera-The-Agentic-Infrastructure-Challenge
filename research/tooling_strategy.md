# Tooling Strategy – Project Chimera

## Development-time MCP Servers (for human / IDE productivity)

These MCP servers are meant to assist the developer / IDE agent during coding, not for runtime Chimera agent behavior.

1. **git-mcp**  
   - Purpose: Version control operations (commit, diff, log, branch) directly from LLM context  
   - Transport: Stdio (local)  
   - Why: Enables agent-assisted commits with proper messages referencing specs/  
   - Status: Planned to run locally via Tenx MCP Sense integration

2. **filesystem-mcp**  
   - Purpose: Safe file read/write/list within project directory  
   - Transport: Stdio  
   - Why: Allows IDE agent to propose file changes without manual copy-paste  
   - Constraints: Restricted to project root + safety sandbox

3. **pytest-mcp** (or test-runner-mcp)  
   - Purpose: Run pytest suite and return failing test output / coverage  
   - Why: Lets agent see red-phase feedback immediately  
   - Status: To be configured or mocked

4. **search-mcp** (e.g. connected to DuckDuckGo or local docs)  
   - Purpose: Quick API/doc lookups during coding  
   - Why: Reduces context switching when implementing specs

## Separation of Concerns

- Dev MCP servers (above) → only active during human/AI coding sessions  
- Runtime Skills (see skills/README.md) → only used by Chimera agents in production

No runtime Chimera agent should have access to git-mcp or filesystem-mcp — security boundary enforced.