# class Employee:
#     def __init__(self,name,age):
#             self.name=name
#             self._age=age

# class SubEmployee(Employee):
#       def show_age(self):
#             print("Age:", self._age)

# emp=SubEmployee("Akshay", 25)
# print(emp.name)
# print(emp._age)
# emp.show_age()
# # emp_1=Employee("Aravind",23)
# # print(emp_1.age)


# class BankAccount:
#     def __init__(self):
#         self.balance=1000

#     def _show_balance(self):
#         print(f"Balance: ₹{self.balance}")

#     def __update_balance(self,amount):
#         self.balance+=amount

#     def deposit(self,amount):
#         if amount>0:
#             self.__update_balance(amount)
#             self._show_balance()
#         else:
#             print("Invalid deposit amount!")


# account=BankAccount()
# account._show_balance()
# # account.__update_balance(500)
# account.deposit(500)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self._marks=marks

#     def _display_marks(self):
#         print("Marks:", self._marks)

# class Result(Student):
#     def show_result(self):
#         print("Student Name:", self.name)
#         print("Student Marks:", self._marks)
#         self._display_marks()

# r=Result("Aravind",85)
# r.show_result()


# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance

#     def _show_balance(self):
#         print(f"Balance:{self.balance}")

#     def __update_balance(self,amount):
#         self.balance+=amount

#     def deposit(self,amount):
#         self.__update_balance(amount)
#         print(f"Balance : {self.balance}")

# class Account(BankAccount):
#     def view(self):
#         self._show_balance()

# acc=Account(50000)
# acc.view()
# acc.deposit(2000)
# # acc._show_balance()
        


# class Student:
#     def __init__(self):
#         self._marks=90
#         print(self._marks)

# class Result(Student):
#     def show(self):
#         print(self._marks)


# r=Result()
# r.show()
# a=Student()





# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Student Name:",self.name,self.age)

# s=Student("Rahul",18)
# s.display
# print("student name",s.name)
# print("student age",s.age)


# class Student:

#     def get_data(self):
#         self.name=input("Enter student name:")

#     def display(self):
#         print("Student Name:",self.name)
#         print("Student Age:",self.age)

# s=Student()
# s.get_data()
# s.dispaly()



# 1

# class Student:
#     def __init__(self):
#         self.__name__ = " "
#         self.__marks__ =0

#     def set_details(self,name,marks):
#         self.__name=name
#         self.__marks=marks

#     def _display_marks(self):
#         print("Student Name:", self.__name)
#         print("Student Marks:", self.__marks)
        

# r=Student()
# r.set_details("Aravind",85)
# r._display_marks()

        
# 2

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Deposited:", amount)
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def display(self):
#         print("Balance:", self.__balance)


# b1 = BankAccount()
# b1.deposit(5000)
# b1.withdraw(2000)
# b1.display()


# 3

# class Employee:
#     def __init__(self):
#         self.__name=""
#         self.__salary=0

#     def set_details(self,name,salary):
#         self.__name=name
#         self.__salary=salary

#     def display_salary(self):
#         print("Employee Name:",self.__name)
#         print("Employee Salary:",self.__salary)

# r=Employee()
# r.set_details("Aravind",25000)
# r.display_salary()


# 4

# class Product:
#     def __init__(self):
#         self.__product_name=" "
#         self.__price=0

#     def set_details(self,product_name,price):
#         self.__product_name= product_name
#         self.__price=price

#     def update(self,new_price):

#         self.__price=new_price
#         s.display()

#     def display(self):
#         print("Product Name:", self.__product_name)
#         print("Price:", self.__price)

# s=Product()
# s.set_details("Laptop",50000)
# s.display()
# s.update(45000)

