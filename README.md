# Citizen Complaint System

**Module:** PROG211 Object-Oriented Programming 1 - Limkokwing University of Creative Technology, Sierra Leone
**Student:** Sharon Mary Ramatha Koroma | **Student ID:** 905006201
**Domain:** Government - Citizen Complaint System

## Problem
Citizens often have no simple way to report public-service problems (water, roads,
electricity, health, sanitation) or to see whether anything was done. This program
lets a citizen submit a complaint, receive a reference ID, and track its status,
while government departments review and resolve complaints.

## How to Run
Requires Python 3.8+ (no external libraries).

```bash
git clone https://github.com/[your-username]/citizen-complaint-system.git
cd citizen-complaint-system
python main.py
```

## Project Structure
| File | Purpose |
|------|---------|
| `complaint.py` | `Complaint` class + constant tuples (categories, statuses, districts) |
| `department.py` | `Department` class that acts on complaints |
| `main.py` | Menu program, dictionary storage, add/display functions |
| `LICENSE` | MIT open-source licence |

## OOP Concepts Used
- **Classes and objects:** `Complaint` and `Department`; objects are created for each complaint and department.
- **Object interaction:** `Department.review()` and `Department.resolve()` change a `Complaint`'s status.
- **Instance methods:** `update_status()`, `display_info()`, `can_handle()`, `review()`, `resolve()`.
- **Class methods:** `Complaint.generate_id()` (uses a class-level counter) and `Complaint.create()` (factory).
- **Static method:** `Complaint.is_valid_description()` validates text without needing an object.
- **Data structure:** one dictionary `{complaint_id: Complaint}` for all records, with `add_complaint()` and `display_all_complaints()`.
- **Tuples (bonus):** `CATEGORIES`, `STATUSES`, `DISTRICTS`, the `DEPARTMENTS` tuple, and `is_valid_description()` returning `(True/False, message)`.

## Digital Public Goods (DPG) Alignment
| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | Hosted publicly on GitHub under the MIT licence; anyone may use, study, and adapt it. |
| **Privacy-respecting** | No names, phone numbers, or addresses are stored. Only a reference ID, category, district, and description are kept. The program warns users and rejects descriptions that contain phone/ID-like numbers. |
| **Inclusive and accessible** | Simple numbered menus, plain-language prompts, clear error messages, and no special hardware or internet needed. All 16 districts of Sierra Leone are supported. |
| **Modular and reusable** | Separate files for each class. Another agency can add categories or departments by editing one tuple, or reuse `Complaint` in a web or mobile app. |

## Example Usage (sample input / output)
```
===== CITIZEN COMPLAINT SYSTEM =====
Choose an option (1-6): 1

Select a category:
  1. Water ...
Enter number: 1
Select your district: ... Enter number: 1
Describe the problem: No running water in our area for two weeks.

Complaint submitted. Your reference ID is: CMP-001

Choose an option (1-6): 4
Enter complaint ID: CMP-001
Select the department: 1. Water Resources Dept
Select action: 2. Mark resolved
Water Resources Dept resolved CMP-001.

Choose an option (1-6): 3
Enter reference ID (e.g. CMP-001): CMP-001
  ID          : CMP-001
  Category    : Water
  District    : Bo
  Description : No running water in our area for two weeks.
  Status      : Resolved
```

## Limitations
Data is held in memory only and is cleared when the program closes (this also
protects privacy). A future version could save records to a file or database.

## Licence
MIT - see `LICENSE`.
