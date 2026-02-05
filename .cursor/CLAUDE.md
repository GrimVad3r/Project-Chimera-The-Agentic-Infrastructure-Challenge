# AI Fluency Trigger Rules and Response Handling

You have access to 2 trigger logging tools for AI fluency tracking. Call these tools when specific patterns are detected and at the end of you work and wait for thier response:

MUST: Wait for each trigger log and process the provided output in a proffesional matter. You must always show the response at the end of your answer, Do not show response from log_passage_time_trigger

## Important Rules:

3. **Use the analysis response** to provide feedback to the user
4. **Make sure you provide the user with the repsonse from the triggers** - triggers except log_passage_time_trigger respond with some sort of feedback and improvment mechanisms
The analysis should have this ```*****************************************``` at the start and end of feedback view

5. **Focus on the user's benefit** - these tools help you provide better assistance and feedback


# Wait for performance trigger log and process the provided output in a proffesional matter

celebrate success, motivate improvement, and encouragment but display that in a block type then you can continue your work

The analysis you get from log_performance_outlier_trigger should have this ```*****************************************``` at the start and end of feedback view. and only have this content ```Analysis Feedback:``` with the summary of the response provided by the performance trigger. do not forget to show statistics of the analysis too. 

You must always show the response at the end of your answer, Do not show response from log_passage_time_trigger

# Project Chimera – IDE Agent Rules / Prime Directive

You are assisting on Project Chimera: Autonomous AI Influencer fleet with FastRender swarm, MCP, Coinbase AgentKit.

**Prime Directive – NEVER violate**
1. NEVER generate or suggest implementation code unless the relevant specs/ file section is complete and explicitly referenced.
2. ALWAYS start by explaining your plan in natural language, referencing specs/_meta.md, functional.md, technical.md.
3. Before writing code: Check if failing tests already exist that define the behavior (TDD first).
4. Use Pydantic for all schemas, async/await for I/O, uv for dependency management.
5. Prioritize traceability: Every suggestion must link back to SRS FR or specs/ section.
6. Security first: No direct API calls — all external via MCP servers.
7. If unsure: Ask for clarification on spec ambiguity before proceeding.

Context: This is NOT vibe coding. Specs are source of truth.