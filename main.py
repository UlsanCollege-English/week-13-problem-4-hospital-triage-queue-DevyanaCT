def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Priority:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.
    """

    if k <= 0 or not patients:
        return []

    # Sort by (severity, arrival_order)
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Take top k and return their names
    return [p["name"] for p in sorted_patients[:k]]


if __name__ == "__main__":
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2))
