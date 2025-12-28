# airline-overbooking
OS project – overbooking and critical section
# Airline Overbooking – Critical Section Problem

This project demonstrates how overbooking happens in airline booking systems
due to race conditions and how it can be prevented using synchronization.

▶️ How to Run the Code
1️⃣ Project Structure

overbooking/
├── no_protection.py
└── with_protection.py

2️⃣ Requirements

Python 3.x

No external libraries required (only standard Python modules)

Check Python version:

python --version

3️⃣ Run the Code (Without Protection)

This file demonstrates overbooking caused by a race condition.

cd overbooking
python no_protection.py

4️⃣ Run the Code (With Protection)

This file demonstrates overbooking prevention using synchronization (lock).

cd overbooking
python with_protection.py

5️⃣ Notes

Both scripts simulate concurrent booking requests

The difference is the use of a lock in with_protection.py

This project illustrates read/write conflict and its solution

