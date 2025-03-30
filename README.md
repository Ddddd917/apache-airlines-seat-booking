# Apache Airlines Seat Booking System

**Version 1.0 – Core CLI Application**

This is the first functional release of the Apache Airlines Seat Booking System.  
It is developed using Python and simulates a seat reservation system for the Burak757 aircraft.  
The system runs in a command-line interface (CLI) and is fully modularized.

---

## ✈️ Features

- **Check Seat Availability** – Check if a specific seat is available for booking.
- **Book a Seat** – Reserve an available seat.
- **Cancel Booked Seat** – Free a previously reserved seat.
- **Show Seat Layout and Booking Status** – Display a formatted layout of 80 rows and seat availability.
- **Exit Program** – Safely exit the system.

---

## 🧩 File Structure

| File            | Description                                  |
|-----------------|----------------------------------------------|
| `main.py`       | Program entry point and menu interface       |
| `booking.py`    | Handles booking and cancellation logic       |
| `seatmap.py`    | Initializes and prints the seat map          |
| `validation.py` | Validates seat input and availability        |
| `constants.py`  | Stores configuration constants and symbols   |
| `version.txt`   | Version description and release notes        |

---

## 🛠️ How to Run

1. Make sure Python 3.10 or later is installed.
2. Place all `.py` files in the same folder.
3. Open your terminal or command prompt.
4. Run the following command:

```bash
python main.py