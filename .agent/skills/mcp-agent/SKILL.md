---
name: mcp-agent
description: Use when connecting to external tools, databases, APIs, or SaaS (Slack, GitHub, Brave Search) via Model Context Protocol (MCP).
metadata:
  version: 1.1.0
  priority: high
---

# MCP AGENT (Smithery)

## PROTOCOL
- **Discovery**: Check Smithery for existing servers before building custom integrations.
- **Logic**: Outcome-focused tools (`create_pr_with_tests`) over atomic API calls.
- **Data**: Max 15 items per response (enforce pagination). Use `rtk` proxies for filtering.
- **Naming**: `provider_action_resource` (e.g., `postgresql_query_table`).
- **Install**: `npx -y @smithery/cli install <server-name>`.

## SAFETY
- Enforce `sec-ops` rules; prefer idempotent actions.
