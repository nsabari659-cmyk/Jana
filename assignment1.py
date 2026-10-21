# balance=100000

# while True:
#     print("1. chcek Balance")
#     print("2. Deposit Money ")
#     print("3. withdraw Money")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#             print("\n------Bank Details-------")
#             print("corrent balance is :",balance)

#     elif choice =="2" :
#             print("\n -----Deposit Details------")
#             deposit = float(input("Enter the deposit money: "))

#             if deposit > 0:
#                  balance = balance + deposit
#                  print("Amount is deposit") 
#             else: 
#                 print("Amount is not fount")

#     elif choice =="3" :
#             print("\n-----withdraw-------")    
#             withdraw = float(input("Enter the withdrawal amount: "))
#             if withdraw > balance:
#                 print("Insufficient balance!")
#             else:
#                 balance = balance - withdraw

#     elif choice =="4":    
#             print("exiting from bank details ")    
#             break
#     else:
#         print("invalid choice.please enter choice(1-4)")