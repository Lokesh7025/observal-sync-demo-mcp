"""Demo MCP server used to test Observal's GitHub webhook sync."""

import os

from fastmcp import FastMCP

mcp = FastMCP("observal-sync-demo", instructions="Small demo tools for testing registry sync.")

GREETING = os.environ.get("DEMO_GREETING", "Hello")


@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting for the given name, using DEMO_GREETING if set."""
    return f"{GREETING}, {name}!"


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
