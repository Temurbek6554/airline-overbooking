import threading
import time

# Shared resource
available_seats = 1

def book_ticket(user):
    global available_seats
    print(f"{user} checking seats...")
    
    if available_seats > 0:
        time.sleep(1)  # Simulate delay (database/network)
        available_seats -= 1
        print(f"{user} successfully booked a seat!")
    else:
        print(f"{user} failed to book. No seats available.")

threads = []

for user in ["User A", "User B"]:
    t = threading.Thread(target=book_ticket, args=(user,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final available seats:", available_seats)
