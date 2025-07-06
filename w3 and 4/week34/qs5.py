#this program uses Function to sort a list of names alphabetically (case-insensitive)
def sort_names(names):
    """Function to sort a list of names alphabetically (case-insensitive)"""
    if not isinstance(names, list):
        return "Input must be a list of names"
    if not names:
        return []
    return sorted(names, key=lambda x: x.lower())
def test_sort_names():
    test_cases = [
        ("Normal names", ["Alice", "bob", "Charlie", "dave"]),
        ("Mixed case", ["Zoe", "alex", "Beth", "mike"]),
        ("Empty list", []),
        ("Single name", ["John"]),
        ("Duplicate names", ["Alice", "bob", "Alice", "charlie"]),
        ("Non-list input", "Not a list"),
        ("Numbers as names", ["1", "10", "2", "20"]),
        ("Special characters", ["O'Reilly", "Smith-Jones", "André"])
    ]
    for description, names in test_cases:
        print(f"\nTest Case: {description}")
        print(f"Input: {names}")
        result = sort_names(names)
        print(f"Sorted: {result}")
if __name__ == "__main__":
    print("NAME SORTING TESTING")
    print("-------------------")
    test_sort_names()
