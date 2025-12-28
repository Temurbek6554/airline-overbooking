import threading
import time

available_seats = 1
lock = threading.Lock()

def book_ticket(user):
    global available_seats
    print(f"{user} attempting to book...")

    with lock:  # Critical Section protected
        if available_seats > 0:
            time.sleep(1)
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
