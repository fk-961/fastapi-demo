import json

def load_expenses(filepath : str) -> list:
    """Load our data JSON file.

    Args:
        filepath (str): Path to our JSON file.

    Returns:
        list: Data returned in list format.
    """
    with open(filepath) as f:
        expenses = json.load(f)
    return expenses

def update_expenses(
    filepath : str,
    expenses : list
) -> None:
    """Updates the JSON dataset.

    Args:
        filepath (str): Path to our JSON file.
        expenses (list): List of expenses.
    """
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent = 4)