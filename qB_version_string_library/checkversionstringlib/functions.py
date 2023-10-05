"""
Question B: 
The goal of this question is to write a software library that accepts 2 version string as input and 
returns whether one is greater than, equal, or less than the other. 
As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of. 
"""
from itertools import zip_longest

# Helper function
def validate_version_string(version_str):
    components = version_str.split('.')
    if not all(component.isdigit() for component in components):
        raise ValueError(f"Invalid version string: {version_str}")
    return list(map(int, components))

# Main function
"""
Please note, our assumption based on the question is that a valid version string must contain only numbers (digits 0-9) separated by periods.
"""
def compare_version_strings(version1, version2):
    try:
        v1 = validate_version_string(version1)
        v2 = validate_version_string(version2)
    except ValueError as e:
        return f"Error: {e}"
        
    for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
        if rev1 == rev2:
            continue

        if rev1 < rev2:
            return f"{version1} is less than {version2}"
        elif rev1 > rev2:
            return f"{version1} is greater than {version2}"

    return f"{version1} is equal to {version2}"