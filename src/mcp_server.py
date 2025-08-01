from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("My Central MCP Server")

# Define tools directly in this file
@mcp.tool
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
