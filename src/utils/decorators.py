import functools
from global_config import global_config

def private_tool_access(identifier):
    """
    Decorator to mark a tool as having private access.
    Looks up configuration from global_config.tool_configs using the identifier.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        try:
            config = getattr(global_config.tool_configs, identifier)
            value = config.private_tool_access
        except (AttributeError, KeyError):
            value = None # Default value

        wrapper._private_tool_access = value
        return wrapper
    return decorator

def write_operation(identifier):
    """
    Decorator to mark a tool as a write operation.
    Looks up configuration from global_config.tool_configs using the identifier.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        try:
            config = getattr(global_config.tool_configs, identifier)
            value = config.write_operation
        except (AttributeError, KeyError):
            value = None # Default value

        wrapper._write_operation = value
        return wrapper
    return decorator

def untrusted_data(func):
    """
    Decorator to mark a tool as handling untrusted data.
    This decorator does not take arguments.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper._untrusted_data = True
    return wrapper
