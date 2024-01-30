"""
- Helpers functions by Sotiris
- get_endpoint(module_name: str) -> str  *(module.sub_module -> /module/sub_module)*
"""

def get_endpoint(module_name: str) -> str:
    """
    This function generates an endpoint from a given module name.

    Parameters:
    module_name (str): The name of the module for which the endpoint is to be created.
                       It is expected to be a string with parts separated by dots.

    Returns:
    str: The created endpoint. It is a string that starts with a slash, followed by the parts of the module name
         (except the last part) separated by slashes. All underscores in the module name are replaced with dashes.

    Example:
    If the input is "module.sub_module.function", the function will print:
    "Will create end point for : module.sub_module.function"
    "Created endpoint : /module/sub-module"
    And it will return "/module/sub-module"
    """

    print(f"Will create end point for : {module_name}")
    blueprint_path = module_name.split(".")
    blueprint_path.pop()
    end_point = f'/{"/".join(blueprint_path)}'.replace("_", "-")
    print(f"Created endpoint : {end_point}")
    return end_point
