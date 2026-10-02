# observal-sync-demo-mcp

A tiny FastMCP server used to test Observal's GitHub webhook sync. Each push to `main`
or published release should show up as a new version of the MCP listing in Observal.

## Run

```bash
uvx --from git+https://github.com/Lokesh7025/observal-sync-demo-mcp observal-sync-demo-mcp
```

## Environment

| Variable | Description |
| --- | --- |
| `DEMO_GREETING` | Greeting prefix used by the `greet` tool |
| `DEMO_SIGNOFF` | Farewell prefix used by the `farewell` tool |
