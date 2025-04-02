
# ✈️ Apache Airlines Seat Booking System

This project is a command-line seat booking system for Apache Airlines, designed to simulate real-world airline reservation operations in a simplified format using Python.

---

## 🎯 Project Objectives

- Practice modular software development
- Implement database-backed data persistence
- Apply object-oriented programming in Python
- Develop a user-friendly CLI booking interface

---

## 🚦 Core Features

- View seat availability
- Book and cancel seat reservations
- Show seat layout and booking status
- Group booking for up to 3 adjacent seats
- Seat preference recommendation (window, aisle, middle)
- Search booking by name and passport number
- Auto-generated 8-character alphanumeric reference code
- Persistent storage using SQLite database

---

### 🧱 Version 4: Full OOP Refactoring

- **Class-Based Architecture** – All functional modules are now refactored into dedicated Python classes.
- **Main Controller: `BookingSystem`** – The system now runs through a centralized class that manages all modules.
- **Improved Modularity** – Clear separation of concerns across:
  - `BookingManager` for reservations
  - `SeatMap` for seat layout
  - `DatabaseManager` for data persistence
  - `Validator` for input validation
  - `SeatPreference` and `SearchManager` for extended features
- **Better Maintainability** – Easier to expand, debug, and integrate new features in the future.
- **Documented Classes** – Each module includes docstrings and inline comments for academic clarity.

---

## 🧱 Tech Stack & Modules (OOP Version 4)

| File                      | Purpose                                             |
|---------------------------|-----------------------------------------------------|
| `booking_system.py`       | Main control class: handles user flow and dispatch |
| `booking_manager.py`      | Manages booking, group booking, and cancellation   |
| `seat_map.py`             | Seat layout generation and display logic           |
| `seat_preference.py`      | Recommends seats based on user preference          |
| `search_manager.py`       | Searches booking by identity                       |
| `database_manager.py`     | All SQLite operations encapsulated in class        |
| `validator.py`            | Static methods for input validation                |
| `constants.py`            | Global constants (DB path, symbol keys)            |

---

## 📦 Version History

### ✅ Version 1
- Implemented basic menu-driven CLI structure
- Seat map using 2D list with status indicators
- 5 basic features: view, book, cancel, layout, exit

### ✅ Version 2
- Added booking summary display
- Group booking for up to 3 seats
- Seat preference search (front row priority)

### ✅ Version 3
- Added data persistence with SQLite
- Booking reference generation (8-char code)
- Identity-based booking search

### ✅ Version 4
- Refactored entire system using OOP
- Modularized all components into classes

---

## 🗂️ Database Schema

```sql
CREATE TABLE passengers (
    reference_code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    passport_number TEXT NOT NULL,
    seat_id TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
```

---

## 🔧 How to Run

1. Ensure Python 3.10+ is installed
2. Install `sqlite3` (usually bundled with Python)
3. Run the project via:
```bash
python booking_system.py
```

---

## 👨‍💻 Author

This project was developed as part of the FC723 coursework.
All code is version-controlled using GitHub and follows academic best practices.

