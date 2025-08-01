import pytest
from fastmcp import Client
from src.mcp_server import mcp as mcp_server

@pytest.mark.asyncio
async def test_add_tool_functionality():
    """
    Tests that the 'add' tool on the MCP server works correctly.
    """
    # The mcp_server is imported directly, and we can test it in-memory
    async with Client(mcp_server) as client:
        result = await client.call_tool("add", {"a": 2, "b": 3})
        assert result.data == 5

        result = await client.call_tool("add", {"a": -1, "b": 1})
        assert result.data == 0
