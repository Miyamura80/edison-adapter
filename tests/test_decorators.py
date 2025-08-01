import pytest
from src.mcp_server import mcp as mcp_server
from src.utils.decorators import private_tool_access, write_operation, untrusted_data
from global_config import global_config

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
async def test_decorator_yaml_config_values():
    """
    Tests that the decorator attributes have the correct values from the YAML config.
    """
    add_tool = await mcp_server.get_tool('add')
    add_tool_func = add_tool.fn

    assert add_tool_func._private_tool_access == global_config.tool_configs.add_tool_config.private_tool_access
    assert add_tool_func._write_operation == global_config.tool_configs.add_tool_config.write_operation
    assert add_tool_func._untrusted_data == True

def test_decorators_with_invalid_identifier():
    """
    Tests that the decorators use None as the value when an invalid identifier is passed.
    """
    @private_tool_access("invalid_identifier")
    @write_operation("invalid_identifier")
    def dummy_func():
        pass

    assert dummy_func._private_tool_access == None
    assert dummy_func._write_operation == None

def test_decorators_with_missing_attribute():
    """
    Tests that the decorators use None as the value when the attribute is missing from the config.
    """
    # We need to add a temporary config to global_config for this test
    global_config.tool_configs.temp_config = type('obj', (object,), {})()

    @private_tool_access("temp_config")
    @write_operation("temp_config")
    def dummy_func():
        pass

    assert dummy_func._private_tool_access == None
    assert dummy_func._write_operation == None

    # cleanup
    del global_config.tool_configs.temp_config
