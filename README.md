# Apache Airlines Seat Booking System

**A Python-based CLI seat booking system for Apache Airlines.**  
Developed in structured phases to simulate real-world airline seat management with modular design.

---

## ✈️ Features

### ✅ Version 1: Core Functions

- **Check Seat Availability** – Check if a specific seat is free or reserved.
- **Book a Seat** – Reserve a seat using its seat ID (e.g., 12A).
- **Cancel Booked Seat** – Free a previously reserved seat.
- **Show Seat Layout and Booking Status** – Display the full 80-row seat map.
- **Exit Program** – Exit the system gracefully.

### 🔁 Version 2: Extended Features

- **Display Booking Summary**  
  → Shows total number of seats (474), number of reserved seats, and their seat IDs  
  → Automatically appears below the seat map

- **Group Booking**  
  → Book multiple seats at once (e.g., `12A 12B 12C`)  
  → If any seat is invalid/unavailable, booking is cancelled

- **Seat Preference Search**  
  → Enter preference: `window`, `aisle`, or `middle`  
  → System recommends up to 4 available front-row seats  
  → Displays: *"The system prioritizes seats in the front rows."*

---

## 📂 File Structure

| File              | Description                                      |
|-------------------|--------------------------------------------------|
| `main.py`         | Entry point, main menu logic                     |
| `booking.py`      | Booking and cancellation functions               |
| `seatmap.py`      | Initializes and prints seat layout and summary   |
| `validation.py`   | Validates seat input and booking eligibility     |
| `preference.py`   | Handles seat preference recommendation (NEW)     |
| `constants.py`    | Stores constants like symbols and layout info    |
| `version_1_description.txt` | Version 1 details (for documentation) |
| `version_2_description.txt` | Version 2 details (for documentation) |

---

## 🚧 Version 3 (Coming Soon)

### 🔧 Planned Features: Data Persistence and Database Integration

Version 3 will enhance the CLI system with real-world data handling capabilities and persistent storage using SQLite. This version corresponds to **Part B** of the project specification.

#### ✅ Planned Additions

- **🔑 Unique Booking Reference**
  - Each booking will generate a unique 8-character alphanumeric reference (e.g., `A7C9B3D2`)
  - Reference will be displayed upon successful booking
  - Reference can later be used to cancel or look up bookings

- **🧍 Passenger Information Collection**
  - Users will enter passenger details upon booking:
    - Full Name
    - Passport Number
  - This data will be stored with the booking record

- **🗃️ SQLite Database Integration**
  - All bookings will be saved in a local SQLite database
  - Data will persist between program sessions

- **❌ Cancel by Reference**
  - Bookings can be cancelled using the unique booking reference

- **🔍 (Optional) Search Bookings**
  - Search by passenger name or passport number (optional bonus feature)

---

### 📁 Upcoming File Updates for Version 3

| File                    | Purpose                                                   |
|-------------------------|-----------------------------------------------------------|
| `database.py`           | NEW – Handles SQLite3 connection and query logic          |
| `booking.py`            | Extended – Stores passenger info and generates references |
| `main.py`               | Add new menu options (e.g., cancel by reference)          |
| `constants.py`          | Add DB path and reference config                          |
| `version_3_description.txt` | NEW – Documents Version 3 features and changes        |

---

### ⏳ Development Status

| Phase        | Status     |
|--------------|------------|
| Version 1    | ✅ Completed |
| Version 2    | ✅ Completed |
| Version 3    | 🚧 In Progress |

> Version 3 is the final development stage of this project and fulfills the requirements for Part B of the FC723 specification.

---
---

## 🛠️ How to Run

1. Ensure Python 3.10 or later is installed
2. Clone or download the project folder
3. Open terminal and run:

```bash
python main.py