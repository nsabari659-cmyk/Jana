# shows = {
#     "Leo": ["10:00 AM", 230],
#     "Jailer": ["2:00 PM", 230],
#     "Vikram": ["6:00 PM", 230]
# }

# bookings = {}


# def list_shows():
#     print("\nAvailable Shows")
#     for movie, details in shows.items():
#         print(movie, "-", details[0], "- Rs.", details[1])


# def book_tickets(movie, number, *seats):
#     bookings[movie] = [number, seats]
#     print("Booking successful!")
#     print("Seats:", seats)


# def calculate_total(price, quantity, discount=0):
#     total = price * quantity
#     total = total - (total * discount / 100)
#     return total


# def loyalty_discount(price, tickets):
#     if tickets == 0:
#         return 0

#     if tickets % 2 == 0:
#         price = price * 0.95

#     return price + loyalty_discount(0, tickets - 1)


# def cancel_booking(movie):
#     if movie in bookings:
#         number = bookings[movie][0]
#         price = shows[movie][1]

#         refund = calculate_total(price, number)

#         del bookings[movie]

#         print("Booking cancelled.")
#         print("Refund: Rs.", refund)
#     else:
#         print("No booking found.")


# while True:
#     print("\n----- MOVIE TICKET BOOKING -----")
#     print("1. List Shows")
#     print("2. Book Tickets")
#     print("3. View Bookings")
#     print("4. Cancel Booking")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         list_shows()

#     elif choice == "2":
#         list_shows()

#         movie = input("Enter movie name: ").title()

#         if movie not in shows:
#             print("Movie not available.")
#             continue

#         number = int(input("Enter number of tickets: "))

#         if number <= 0:
#             print("Enter a valid number of tickets.")
#             continue

#         seats = []

#         for i in range(number):
#             seat = int(input("Enter seat number: "))
#             seats.append(seat)

#         book_tickets(movie, number, *seats)

#         price = shows[movie][1]

#         print("\nPayment Method")
#         print("1. GPay")
#         print("2. Credit Card")
#         print("3. Cash")

#         payment = input("Enter payment method: ")

#         if payment == "1":
#             total = calculate_total(price, number) + 30

#         elif payment == "2":
#             total = calculate_total(price, number, 30)

#         elif payment == "3":
#             total = calculate_total(price, number)

#         else:
#             print("Invalid payment method.")
#             continue

#         print("Total amount: Rs.", total)

#     elif choice == "3":
#         if bookings:
#             print("\nYour Bookings")

#             for movie, details in bookings.items():
#                 print("Movie:", movie)
#                 print("Number of tickets:", details[0])
#                 print("Seats:", details[1])
#         else:
#             print("No bookings available.")

#     elif choice == "4":
#         movie = input("Enter movie name to cancel: ").title()
#         cancel_booking(movie)

#     elif choice == "5":
#         print("Thank you for using Movie Ticket Booking!")
#         break

#     else:
#         print("Invalid choice! Please try again.")