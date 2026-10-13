"""
main.py
-------
Citizen Complaint System - text menu program.

Data structure (Task 2): ONE dictionary, {complaint_id: Complaint object}.
"""

from complaint import Complaint, CATEGORIES, STATUSES, DISTRICTS
from department import Department

# Tuple of Department objects (fixed list of departments).
DEPARTMENTS = (
    Department("Water Resources Dept", ("Water", "Sanitation")),
    Department("Roads Authority", ("Roads",)),
    Department("Energy Dept", ("Electricity",)),
    Department("Health Ministry Office", ("Health",)),
)


# ---- Task 2 functions: add and display records ----------------------------
def add_complaint(complaints, complaint):
    """Store a Complaint in the dictionary using its ID as the key."""
    complaints[complaint.complaint_id] = complaint


def display_all_complaints(complaints):
    """Loop through the dictionary and display every complaint."""
    if not complaints:
        print("\nNo complaints recorded yet.")
        return
    print(f"\n--- All Complaints ({len(complaints)}) ---")
    for complaint in complaints.values():
        complaint.display_info()
        print("  " + "-" * 40)


# ---- Input helpers ---------------------------------------------------------
def choose_from(options, title):
    """Show a numbered list from a tuple and return the chosen item."""
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice. Please enter a number from the list.")


def submit_complaint(complaints):
    print("\n=== Submit a Complaint ===")
    print("PRIVACY: do NOT include your name, phone number or address.")
    category = choose_from(CATEGORIES, "Select a category:")
    district = choose_from(DISTRICTS, "Select your district:")
    while True:
        description = input("\nDescribe the problem: ")
        valid, message = Complaint.is_valid_description(description)  # static
        if valid:
            break
        print(f"  {message}")
    complaint = Complaint.create(category, district, description.strip())  # classmethod
    add_complaint(complaints, complaint)
    print(f"\nComplaint submitted. Your reference ID is: {complaint.complaint_id}")


def track_complaint(complaints):
    print("\n=== Track a Complaint ===")
    cid = input("Enter reference ID (e.g. CMP-001): ").strip().upper()
    if cid in complaints:
        print()
        complaints[cid].display_info()
    else:
        print("No complaint found with that ID.")


def department_action(complaints):
    print("\n=== Department Action ===")
    cid = input("Enter complaint ID: ").strip().upper()
    if cid not in complaints:
        print("No complaint found with that ID.")
        return
    complaint = complaints[cid]
    department = choose_from(DEPARTMENTS, "Select the department:")
    action = choose_from(("Start review", "Mark resolved"), "Select action:")
    if action == "Start review":
        print(department.review(complaint))
    else:
        print(department.resolve(complaint))


def load_demo_data(complaints):
    """Add sample complaints so the program can be demonstrated quickly."""
    samples = (
        ("Water", "Bo", "No running water in our area for two weeks."),
        ("Roads", "Kenema", "Large potholes on the main road near the market."),
        ("Electricity", "Western Area Urban", "Street lights not working at night."),
    )
    for category, district, description in samples:
        add_complaint(complaints, Complaint.create(category, district, description))
    print(f"{len(samples)} demo complaints loaded.")


def main():
    complaints = {}  # the ONE data structure: {ID: Complaint}
    menu = (
        "\n===== CITIZEN COMPLAINT SYSTEM =====\n"
        "1. Submit a complaint\n"
        "2. View all complaints\n"
        "3. Track a complaint by ID\n"
        "4. Department action (review / resolve)\n"
        "5. Load demo data\n"
        "6. Exit"
    )
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            submit_complaint(complaints)
        elif choice == "2":
            display_all_complaints(complaints)
        elif choice == "3":
            track_complaint(complaints)
        elif choice == "4":
            department_action(complaints)
        elif choice == "5":
            load_demo_data(complaints)
        elif choice == "6":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()