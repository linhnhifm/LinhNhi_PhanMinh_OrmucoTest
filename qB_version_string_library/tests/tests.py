from checkversionstringlib import functions

# Test cases
test_cases = [
    # Test Invalid version string formats
    ("1..1", "1.2", "Error: Invalid version string: 1..1"),
    ("1.1", "1.2.", "Error: Invalid version string: 1.2."),
    ("1..1", "1.2.", "Error: Invalid version string: 1..1"),
    ("-1.1", "1.2", "Error: Invalid version string: -1.1"),
    ("1.1", "-1.2", "Error: Invalid version string: -1.2"),
    # Test version strings with same lengths with single digits each
    ("1", "2", "1 is less than 2"),
    ("2", "1", "2 is greater than 1"),
    ("1", "1", "1 is equal to 1"),
    # Test version strings with same lengths with format x.x
    ("1.1", "1.2", "1.1 is less than 1.2"),
    ("1.2", "1.1", "1.2 is greater than 1.1"),
    ("1.1", "1.1", "1.1 is equal to 1.1"),
    # Test version strings with same lengths with format x.x.x
    ("1.2.3", "1.2.4", "1.2.3 is less than 1.2.4"),
    ("1.2.4", "1.2.3", "1.2.4 is greater than 1.2.3"),
    ("1.2.3", "1.2.3", "1.2.3 is equal to 1.2.3"),
    # Test version strings with same length with format x.xx.x
    ("1.20.1", "1.20.2", "1.20.1 is less than 1.20.2"),
    ("1.20.2", "1.20.1", "1.20.2 is greater than 1.20.1"),
    ("1.20.1", "1.20.1", "1.20.1 is equal to 1.20.1"),
    # Test version strings with different lengths
    ("2.0.0.1", "2.0.0", "2.0.0.1 is greater than 2.0.0"),
    ("1.10", "1.2", "1.10 is greater than 1.2"),
    ("1.10.1", "1.10", "1.10.1 is greater than 1.10"),
    ("1.1.12", "1.2", "1.1.12 is less than 1.2"),
    # Test version strings with different lengths but are equal in value
    ("2.0", "2", "2.0 is equal to 2"),
    ("2", "2.0", "2 is equal to 2.0"),
    ("2.0.0", "2", "2.0.0 is equal to 2"),
    ("2", "2.0.0", "2 is equal to 2.0.0"),
    ("1.2.0", "1.2", "1.2.0 is equal to 1.2"),
    ("1.2", "1.2.0", "1.2 is equal to 1.2.0"),
]

for version1, version2, expected in test_cases:
    result = functions.compare_version_strings(version1, version2)
    assert result == expected, f"Expected {expected}, but got {result} for {version1} and {version2}"