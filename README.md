# Apache Airlines Seat Booking System ✈️

A modular Python CLI system for managing seat reservations on Apache Airlines' flight 757.  
Built through three development phases to simulate real-world airline booking logic, data persistence, and user experience.

---

## 🚀 Features Overview

### ✅ Version 1: Basic Functionality

- **Check Seat Availability** – Verify if a specific seat is free or reserved.
- **Book a Seat** – Reserve a seat using its seat ID (e.g., 12A).
- **Cancel Booking by Reference Code** – Remove a reservation by entering its code.
- **Show Seat Layout and Booking Summary** – Print all 80 rows with reservation info.
- **Exit Program** – Cleanly exit the system.

### 🔄 Version 2: Enhanced Features

- **Display Booking Summary** – Total seat count, reserved count, and reserved seat list shown below seat layout.
- **Group Booking (Max 3 Seats)** – Book up to 3 adjacent seats with individual passenger info and reference codes.
- **Seat Preference Search** – Recommend up to 4 front-row seats based on preference:
  - `window` → A/F
  - `aisle` → C/D
  - `middle` → B/E

### 🧩 Version 3: Data Persistence & Identity-Based Booking

- **Passenger Info Collection** – Collect full name and passport number for every booking.
- **Reference Code System** – Generate unique 8-character booking code (e.g., A7Z2B1QX).
- **SQLite3 Database Integration** – All bookings are saved in `flight757_booking.db`, and persist after exit.
- **Cancel Booking by Reference Code** – Securely cancel a booking via its unique code.
- **Search Booking by Identity** – Retrieve booking details using name and passport number.

---

## 🧱 Tech Stack & Modules

| File              | Purpose                                             |
|-------------------|-----------------------------------------------------|
| `main.py`         | Main program loop and menu logic                    |
| `booking.py`      | Handles single/group booking, cancellations         |
| `seatmap.py`      | Seat map generation and display                     |
| `validation.py`   | Validates seat IDs, reference codes, passport nums  |
| `preference.py`   | Seat recommendation engine based on user preference |
| `database.py`     | SQLite connection and query management              |
| `search.py`       | Allows identity-based booking lookup                |
| `constants.py`    | Centralized config: symbols, DB name, code length   |
| `version_x_description.txt` | Documents feature changes by version     |

---
## 🗂️ Menu Structure (Version 3)
===== Apache Airlines Seat Booking System =====
   1.	Check Seat Availability
   2.	Book a Seat
   3.	Cancel Booking by Reference Code
   4.	Show Seat Layout and Booking Summary
   5.	Group Booking
   6.	Seat Preference Search
   7.	Search Booking by Name and Passport Number
   8.	Exit Program

💡 If you forgot your reference code, you can retrieve it using option 7.

## 🪑 Seat Layout

- **Aircraft:** Apache Airlines 757  
- **Configuration:** 80 rows × 6 seats (A–F)  
- **Aisle:** Appears between C and D (shown as `｜X｜`)  
- **Storage Area:** Rows 77–78, columns D/E/F (not bookable)  
- **Total Bookable Seats:** **474**

### 🔍 Legend:

- `<R>` = Reserved  
- `F` = Free  
- `S` = Storage  
- `｜X｜` = Aisle

## 🧪 Passport & Reference Format Rules

- **Passport Number:** Alphanumeric, 6–9 characters (e.g., A1234567)
- **Reference Code:** 8 uppercase letters/digits (e.g., XZ19AC7Q)

---

## 📦 Version History

| Version | Summary                                                                 |
|---------|-------------------------------------------------------------------------|
| `v1.0`  | Core system: check, book, cancel, display layout                        |
| `v2.0`  | Group booking, seat preference search, booking summary                  |
| `v3.0`  | Passenger info, reference codes, database, identity-based search        |

## 📌 Future Improvements (Optional Ideas)

- GUI version using Tkinter or PyQt
- Admin dashboard to export bookings
- Email confirmation system (via SMTP)

---

## 👨‍💻 Author

Developed by Jasper Dai, FC723 Coursework Project  
University of Glasgow / Kaplan GIC (2025)

## 🖥️ How to Run

1. Ensure Python 3.10 or later is installed.
2. Open terminal in the project directory.
3. Run the program with:
```bash
python main.py


