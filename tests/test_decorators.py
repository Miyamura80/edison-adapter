import pytest
from src.mcp_server import mcp as mcp_server
from src.utils.decorators import private_tool_access, write_operation, untrusted_data

@pytest.mark.asyncio
async def test_decorator_attributes_on_add_tool():
    """
    Tests that the decorators add the correct attributes to the 'add' tool.
    """
    add_tool = await mcp_server.get_tool('add')
    add_tool_func = add_tool.fn

    assert hasattr(add_tool_func, '_private_tool_access')
    assert hasattr(add_tool_func, '_write_operation')
    assert hasattr(add_tool_func, '_untrusted_data')

@pytest.mark.asyncio
async def test_decorator_argument_values():
    """
    Tests that the decorator attributes have the correct values from the arguments.
    """
    add_tool = await mcp_server.get_tool('add')
    add_tool_func = add_tool.fn

    assert add_tool_func._private_tool_access == True
    assert add_tool_func._write_operation == True
    assert add_tool_func._untrusted_data == True

def test_decorators_with_no_arguments():
    """
    Tests that the decorators use None as the value when no arguments are passed.
    """
    @private_tool_access()
    @write_operation()
    def dummy_func():
        pass

    assert dummy_func._private_tool_access == None
    assert dummy_func._write_operation == None

def test_decorators_with_arguments():
    """
    Tests that the decorators correctly store the arguments passed to them.
    """
    @private_tool_access(config_value="admin")
    @write_operation(config_value={"level": 5})
    def dummy_func():
        pass

    assert dummy_func._private_tool_access == "admin"
    assert dummy_func._write_operation == {"level": 5}
