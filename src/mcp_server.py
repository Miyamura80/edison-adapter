from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("My Central MCP Server")

from src.utils.decorators import private_tool_access, write_operation, untrusted_data

# Define tools directly in this file
@mcp.tool
@private_tool_access("add_tool_config")
@write_operation("add_tool_config")
@untrusted_data
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Main application entry point
def run_server():
    print("Starting MCP server...")
    # No need to load tools anymore
    print("Running server.")
    mcp.run()

if __name__ == "__main__":
    run_server()
