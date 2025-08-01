import functools

def private_tool_access(config_value=None):
    """
    Decorator to mark a tool as having private access.
    Accepts an optional config_value.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._private_tool_access = config_value
        return wrapper
    return decorator

def write_operation(config_value=None):
    """
    Decorator to mark a tool as a write operation.
    Accepts an optional config_value.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._write_operation = config_value
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
