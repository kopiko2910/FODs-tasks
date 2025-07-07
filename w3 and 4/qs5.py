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
        ("Normal names", ["ram", "aman", "safal", "shrawan"]),
        ("Mixed case", ["Roeisha", "aman", "Shrawan", "sahil"]),
        ("Duplicate names", ["Shrawan", "Shrawan", "Roeisha", "Aman"]),
    ]
    for description, names in test_cases:
        print(f"\nTest Case: {description}")
        print(f"Input: {names}")
        result = sort_names(names)
        print(f"Sorted: {result}")
if __name__ == "__main__":
    print("NAME SORTING TESTING")
    test_sort_names()
