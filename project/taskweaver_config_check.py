"""
    This script checks if the modules listed in the taskweaver_config.json 
    are available and could be extended to check theother settings as well.
"""
import json

def get_allowed_modules():
    with open('./project/taskweaver_config.json', 'r') as f:
        config = json.load(f)
    return config['code_interpreter']['allowed_modules']

allowed_modules = get_allowed_modules()

# Check if the modules are available
unavailable_modules = []  # Create an empty list to store not available modules

for module in allowed_modules:
    try:
        __import__(module)
        print(f'"{module}",')
    except ImportError:
        unavailable_modules.append(module)  # Add not available module to the list

print(f"\n\nUnavailble modules:\n {unavailable_modules}\n")