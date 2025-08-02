# class Book():
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def show(self):
#         print(f"Title : {self.title}")
#         print(f"Author : {self.author}")
#         print(f"price : {self.price}")
# b1=Book("goatlife","Benyamin",500)
# b1.show()

# class Student():
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Roll-No : {self.roll_no}")
#         print(f"Marks : {self.marks}")
#     def average(self):
#         return sum(self.marks.values())/len(self.marks)
#     def grade(self):
#         avg=self.average()
#         if avg>=90:
#             return 'A'
#         elif avg>=75:
#             return 'B'
#         elif avg>=60:
#             return 'C'
#         else:
#             return 'D'
# s1=Student("Arun","57",{"math": 95, "science": 89, "english": 90})
# s2=Student("Arjun","60",{"math": 85, "science": 92, "english": 88})
# s1.display()
# print(f'Average : {s1.average():.2f}')
# print(f'Grade : {s1.grade()}')
# print()
# s2.display()
# print(f'Average : {s2.average():.2f}')
# print(f'Grade : {s2.grade()}')


# class Subjectmarks():
#     def __init__(self):
#         self.marks={}
#     def add_mark(self,subject,mark):
#         self.marks[subject]=mark
#     def get_average(self):
#         return sum(self.marks.values())/len(self.marks)
#     def get_subjects(self):
#         return self.marks

# class Student():
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#         self.subject=Subjectmarks()
#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Roll No  : {self.roll_no}")
#         print(f"\nSubject and Marks \n ")
#         for subjects,mark in self.subject.get_subjects().items():
#             print(f"{subjects:<10} : {mark}")
#     def get_grade(self):
#         avg=self.subject.get_average()
#         if avg>=90:
#              return 'A'
#         elif avg>=75:
#             return 'B'
#         elif avg>=60:
#             return 'C'
#         else:
#             return 'D'

# s1=Student('Arun',23)
# s1.subject.add_mark('science',10)
# s1.subject.add_mark("maths", 85)
# s1.subject.add_mark("English", 88)
# s1.display()
# print(f"Average : {s1.subject.get_average():.2f}")
# print(f"Grade : {s1.get_grade()}")

# class Book():
#     def __init__(self,title,author,isbn):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.available=True
#     def display(self):
#         status='available' if self.available else 'issued'
#         print(f"Title : {self.title}")
#         print(f"Author : {self.author}")
#         print(f"isbn : {self.isbn}")
#         print(f"Status : {status}")
#     def mark_unavailable(self):
#         self.available=False
#     def mark_available(self):
#         self.available=True
# class Library():
#     def __init__(self):
#         self.books=[]
#     def add_book(self,title,author,isbn):
#         new_book=Book(title,author,isbn)
#         self.books.append(new_book)
#     def issue_book(self,isbn):
#         for book in self.books:
#             if book.isbn==isbn:
#                 book.mark_unavailable()
#                 print(f"The Book {book.title} is issued")
#                 return
#         print("Book not found ! ")
        
#     def book_return(self,isbn):
#         for book in self.books:
#             if book.isbn==isbn:
#                 book.mark_available()
#                 print(f"The {book.title} has been returned")
#                 return
#         print("Book not found")
#     def remove_book(self,isbn):
#         for book in self.books:
#             if book.isbn==isbn:
#                 self.books.remove(book)
#                 print(f"The {book.title} has been removed")
#                 return
#         print("Book not found")
#     def display_books(self):
#         print("Details of all the books")
#         if not self.books:
#             print("No books avilable in the library !")
#         else:
#             for book in self.books:
#                 book.display()


# class Student():
#     def __init__(self,name,roll_no,subject):
#         self.name=name
#         self.roll_no=roll_no
#         self.subject=subject

#     def display(self):
#         print(f"\nThe name of student : {self.name}")
#         print(f"The roll no of student : {self.roll_no}")
#         print(f"The subject details of student : {self.subject}")
#         print(f"The average mark : {self.average()}")
#     def average(self):
#         return sum(self.subject.values())/len(self.subject)
# class Undergraduate(Student):
#     def __init__(self,name,roll_no,subject,year):
#         super().__init__(name,roll_no,subject)
#         self.year=year
#     def display(self):
#         super().display()
#         print(f"Year of study : {self.year}")
# class Graduate(Student):
#     def __init__(self,name,roll_no,subject,thesis_title,supervisor):
#         super().__init__(name,roll_no,subject)
#         self.thesis_title=thesis_title
#         self.supervisor=supervisor
#     def display(self):
#         super().display()
#         print(f"Thesis Title : {self.thesis_title}")
#         print(f"Supervisor : {self.supervisor}")

# g1=Graduate('Smruthi',25,{'science':67,'maths':78},"Ai in future",'Arun')
# ug1=Undergraduate('Arjun',15,{'english':77,'social':45},1)
# s1=Student('Anil',45,{'cs':29,'biology':87,})
# for s in [g1,ug1,s1]:
#     s.display()


# class Student():
#     school_name='AI Global school'
#     def __init__(self,name,roll_no,course):
#         self.name=name
#         self.roll_no=roll_no
#         self.course=course
#     def display(self):
#         print(f"\nName : {self.name}")
#         print(f"Roll No : {self.roll_no}")
#         print(f"Course : {self.course}")
#         print(f"School Name : {self.__class__.school_name}")

#     @classmethod
#     def change_school(cls,new_school_name):
#         cls.school_name=new_school_name

#     @staticmethod
#     def is_valid_name(name):
#         if name !=''and name.isalpha():
#             return True
#         else:
#             return False


    
# s1=Student('Arun',14,'cs')
# s1.display()

# s2=Student('Arjun',23,"it")
# s2.change_school('coet')     
# s2.display()

# print(Student.is_valid_name('Meena'))
# print(Student.is_valid_name(''))
# print(Student.is_valid_name('Meena23'))

# class Account():
#     def __init__(self,holder_name,acc_number):
#         self.holder_name=holder_name
#         self.acc_number=acc_number
#         self.__balance=0


#     def deposit(self,new_deposit):
#         if isinstance(new_deposit,(int,float)):
#             if new_deposit>0:
#                 self.__balance+=new_deposit
#             else:
#                 print("deposit cannot be negative ! ")
#         else:
#             print("entries cannot be blank or alphabets ! ")


#     def withdraw(self,w_amount):
#         if isinstance(w_amount,(int,float)):
#             if w_amount>0:
#                 if w_amount>self.__balance:
#                     print("Not enough amount to withdraw ! Please check your balance ")
#                 else:
#                     self.__balance-=w_amount
#             else:
#                 print(" Please enter valid number ! ")
#         else:
#             print("entries cannot be blank or alphabets ! ")


#     def check_balance(self):
#         return self.__balance
#     def display(self):
#         print(f"Account Holder Name : {self.holder_name}")
#         print(f"Account Number : {self.acc_number}")


# a1=Account('Arun',2392)
# a1.display()
# a1.deposit(450)
# print(f"Available Balance : {a1.check_balance()}")



# from datetime import datetime
# class Bank():
#     def __init__(self):
#         self.bank_name="Canara Bank Thalassery"
#         self.accounts=[]
#     def create_account(self,acc_obj):
#        if self.find_account(acc_obj.acc_no):
#            print("Account already exists with this number ! ")
#        else:   
#            self.accounts.append(acc_obj)
#            print(f"Account for {acc_obj.name} created")


#     def find_account(self,acc_no):
#         for account in self.accounts:
#             if account.acc_no == acc_no:
#                 return account
#         return None
    
#     def deposit(self,acc_no,amount):
#         acc=self.find_account(acc_no)
#         if acc:
#             acc.deposit(amount,'deposit')
#         else:
#             print("Account not found ! ")


#     def withdraw(self,acc_no,w_amount):        
#         acc=self.find_account(acc_no)
#         if acc:
#             acc.withdraw(w_amount)
#         else:
#             print("Account not found ! ")
#     def display_all_accounts(self):
#         if self.accounts:
#             for account in self.accounts:
#                 account.display()
#         else:
#             print("No accounts to display ! ")

#     def show_account_transactions(self,acc_no):
#             a=self.find_account(acc_no)
#             if a:
#                 a.show_transaction_history()
#             else:
#                 print("Please enter valid account number ! ")
#     @classmethod
#     def bank_name(cls):
#         return 'Canara Bank Thalassery'
    
# class InsufficientFundsError(Exception):
#         """Custome Exception for when Accont balance is not Enough"""
#         pass
            

# class Account():
#     def __init__(self,name,acc_no):
#         self.name=name
#         self.acc_no=acc_no
#         self.__balance=0
#         self.transactions=[]

#     def record_transaction(self,trans_type,amount):
#         rt={'type':trans_type,'amount':amount,'time':datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}
#         self.transactions.append(rt)
#     def show_transaction_history(self):
#         if not self.transactions:
#             print("No transactions yet ! ")
#         else:
#             print(f'{'Type' :<12} {'Amount':<12} {'Time'}')
#             print("-"*35)
#             for transaction in self.transactions:
#                 print(f"{transaction['type']:<12} ₹{transaction['amount']:<12}  {transaction['time']}")

#     def deposit(self,new_deposit,trans_type='deposit'):

#         if isinstance(new_deposit,(int,float)):
#             if new_deposit>0:
#                 self.__balance+=new_deposit
#                 self.record_transaction(trans_type,new_deposit)
#             else:
#                 print("deposit cannot be negative ! ")
#         else:
#             print("entries cannot be blank or alphabets ! ")


#     def withdraw(self,w_amount):
#         if isinstance(w_amount,(int,float)):
#             if w_amount>0:
#                 if w_amount>self.__balance:
#                     raise InsufficientFundsError("Not enogh Balance ! ")
#                 else:
#                     self.__balance-=w_amount
#                     self.record_transaction('withdraw',w_amount)
#             else:
#                 print(" Please enter valid number ! ")
#         else:
#             print("entries cannot be blank or alphabets ! ")

#     @property
#     def check_balance(self):
       
#        return self.__balance

    
#     def display(self):
#         print(f"Account Holder Name : {self.name}")
#         print(f"Account Number : {self.acc_no}")
#         print(f"Available Balance : {self.check_balance}")


# class SavingsAccount(Account):

#     def __init__(self,name,acc_no,interest_rate):
#         super().__init__(name,acc_no)
#         self.interest_rate=interest_rate

#     def apply_interest(self):
#             if isinstance(self.interest_rate,(int,float)):
#                  interest=self.check_balance*(self.interest_rate/100)
#                  self.deposit(interest,'interest')
#                  print(f"interest of {interest} has been applied at the rate of {self.interest_rate}")
#             else:
#                 print("Enter valid interest rate")

# class CurrentAccount(Account):

#     def __init__(self,name,acc_no,overdraft_limit):
#         super().__init__(name,acc_no)
#         self.overdraft_limit=overdraft_limit
#     def withdraw(self, w_amount):
#         if isinstance(w_amount, (int, float)) and w_amount > 0:
#             if w_amount<=self.check_balance+self.overdraft_limit:
#                 self._Account__balance-=w_amount
#                 self.record_transaction('withdraw',w_amount)
#                 print(f"{w_amount} has been deducted from your account!")
#             else:
#                 print(" Overdraft limit exceeded ! ")
#         else:
#             print("Enter valid withdraw amount ! ")

# bank = Bank()

# # Create accounts
# acc1 = SavingsAccount("Arun", 1001, 5)
# acc2 = CurrentAccount("Meena", 1002, 500)

# # Register accounts with the bank
# bank.create_account(acc1)
# bank.create_account(acc2)

# # Deposit and Withdraw
# bank.deposit(1001, 10000)
# bank.deposit(1002, 5000)

# # Apply interest to savings account
# acc1.apply_interest()

# # Try overdraft withdrawal
# bank.withdraw(1002, 900)
# bank.withdraw(1001, 100)
# # Display all accounts
# bank.display_all_accounts()
# bank.show_account_transactions(1001)
# bank.show_account_transactions(1002)

# bank.deposit(1001, 10000)
# bank.deposit(1002, 5000)
# bank.withdraw(1001, 200)
# bank.withdraw(1002, 500)

# bank.display_all_accounts()
# bank.show_account_transactions(1001)
# bank.show_account_transactions(1002)
# bank.deposit(1001, 10000)
# bank.deposit(1002, 5000)
# bank.show_account_transactions(1001)
# bank.show_account_transactions(1002)

# s1=SavingsAccount('Arun',8373,5)
# s1.display()
# s1.deposit(1000)
# print(f"Available balance :{s1.check_balance}")
# s1.withdraw(250)
# print(f"Available balance : {s1.check_balance}")
# s1.apply_interest()
# print(f"Available balance : {s1.check_balance}")
# s1.withdraw(1000)
# print(f"Available balance : {s1.check_balance}")
# print(Bank.bank_name())
# print(acc1.check_balance)
# print(s1.check_balance)

# try:
#     s1.withdraw(10000)
# except InsufficientFundsError as e:
#     print(e)


# print(Bank.bank_name())
# s2=CurrentAccount('sanal',656,2000)
# s2.display()
# s2.deposit(1000)
# print(s2.check_balance())
# s2.withdraw(3500)
# print(s2.check_balance())
# s2.withdraw(3000)



# class Employee():
#     def __init__(self,id,salary):
#         self.id=id
#         self.salary=salary

# class Manager(Employee):
#     def __init__(self,id,salary,departement):
#         super().__init__(id,salary)
#         self.departement=departement
    
#     def show(self):
#          print(f"{'ID' :<10} {'salary':<10} {'departement'}")
#          print(f"{self.id:<10} {self.salary:<10} {self.departement}")
        


# e1=Employee(25327,20000)
# m1=Manager(896,40000,"Technical")
# m1.show()


# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Child(Person):
#     def __init__(self, name, age,roll_no):
#         super().__init__(name, age)
#         self.roll_no=roll_no
#     def show(self):
#         print(f"{'Name' :<10} {'Age':<10} {'Roll No':<10}")
#         print(f"{self.name:<10} {self.age:<10} {self.roll_no}")

# p1=Person("Arun",28)
# c1=Child("Arun",28,24)
# c1.show()


# class Animal():
#     def __init__(self):
#         pass
#     def make_sound(self):
#         print(f'I am a Animal ')
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__()
#         self.name=name
#     def make_sound(self):
#         print(f'Name : {self.name}  \nSound : Bark! ')
# a1=Animal()
# a1.make_sound()
# d1=Dog('Rocky')
# d1.make_sound()

# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         raise NotImplementedError("Subclass must implement this method")
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__()
#         self.radius=radius
#     def area(self):
#         print(f'Area : {3.14*self.radius**2}')
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         super().__init__()
#         self.l=l
#         self.b=b
#     def area(self):
#         print(f"Area : {self.l*self.b}")

# s1=Shape()
# c1=Circle(5)
# c1.area()
# r1=Rectangle(5,3)
# r1.area()

# class MathHelper():
#     @classmethod
#     def add(cls,a,b):
#         return a+b

# class Animal():
#     def __init__(self):
#         self.a=[]
#     def add(self,animal_obj):
#         if animal_obj in self.a:
#             print("Already added !")
#         else:
#             self.a.append(animal_obj)
#             print("Object is added to Animal class")
# class Dog():
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"Name : {self.name}")



# d1=Dog("rocky")
# d1.show()
# a1=Animal()
# a1.add(d1)
# class Car():
#     def __init__(self):
#         self.car_list=[]
#     def show():
#        print("show car")

# class Engine():
#     def __init__(self,cc,type,ein):
#         self.cc=cc
#         self.type=type
#         self.ein=ein
#     def show(self):
#         print(f"CC : {self.cc} \nType : {self.type} \nEIN : {self.ein}")

# class C():
   
#     def show(self):
#        print("class c")


# class D(Engine,C):
#     def __init__(self, cc, type, ein):
#        super().__init__(cc, type, ein)
       

# d1=D(390,'2 stroke',3546)
# d1.show()

# from abc import ABC,abstractmethod


# class A(ABC):
#     @abstractmethod
#     def show(self):
#         pass

# class B(A):
#     def t(self):
#         print("B")

# class C(A):
#     def why(self):
#         print("C")

# class D(B, C):
#     pass


# d = D()
# d.show()
# print(D.__mro__)
# print(D.__mro__)


# import json


# class JSONMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__)
    
# class User(JSONMixin):
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email


# user=User('arun',28,'arun22@gmail.com')
# print(user.to_json())


# from abc import ABC,abstractmethod
# import json

# class Library(ABC):
#     """ Base class for all library items"""

#     @abstractmethod
#     def show(self):
#         pass

# class BookNotAvailableError(Exception):
#     """ custome exception when book is not available"""
#     def __init__(self, message='Book not available!'):
#         super().__init__(message)

# class JSONMixin:
#     def to_json(self):
#         return json.dump(self.__dict__,indent=4)


    
# class Book(Library,JSONMixin):
#     total_books=0
#     def __init__(self,title,author,isbn):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         total_books+=1
#     def show(self):
#         print(f"Title : {self.title} \nAuthor : {self.author} \nisbn : {self.isbn}")

#     @classmethod
#     def total_books(cls):
#         return cls.total_books

#     @staticmethod
#     def isbn_valid(isbn):
#         return len(isbn)==13 and isbn.isdigit()
    

# class User(JSONMixin,Library):
#     def __init__(self,name,email):
#         super().__init__()
#         self.name=name
#         self.email=email
#         self.books=[]
#     def show(self):
#         print(f"Name : {self.name}\nemail : {self.email}\n")
#         for book in self.books:
#             book.show()
        


# b1=Book('Goatlife','Benyamin',6474)
# u1=User('Arun','arun123@gmail.com')
# b1.show()
# u1.show()

# class Book():
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return f"Title : {self.title}, Author : {self.author}, Pages : {self.pages} "
    
#     def is_long(self):
#         return self.pages>500


# class Ebook(Book):
#     def __init__(self, title, author, pages,file_size):
#         super().__init__(title, author, pages)
#         self.file_size=file_size

#     def is_large_file(self):
#         return self.file_size>100
    
#     def __str__(self):
#         return f"Title : {self.title}, Author : {self.author}, Pages : {self.pages}, File Size : {self.file_size}"
# class Vector():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
   
#     def __str__(self):
#         return f"Vector{self.x,self.y}"
    
# c1=Vector(5,6)
# c2=Vector(4,9)
# c3=c1+c2
# print(c3.x,c3.y)
# # c4=str(c3)
# print(c3)

# b1=Book("Goatlife",'Benyamin',300)
# print(b1)
# print(b1.is_long())
# b2=Book("life",'Binu',600)
# print(b2.is_long())
# e1=Ebook('hello','arun',600,700)
# print(e1.is_large_file())
# print(e1)

# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         print(f"Annual Salary : {self.salary*12}")

# class Manager(Employee):
#     def __init__(self, name, salary,departement):
#         super().__init__(name, salary)
#         self.departement=departement

#     def annual_salary(self):
#         print(f"Annual Salary : {(self.salary*12)+(self.salary*12)*(10/100)}")

# e1=Employee('arun',20000)
# e1.annual_salary()
# m1=Manager('Ajil',45000,'Technical')
# m1.annual_salary()

# class Product():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def apply_discount(self,percent):
#         self.price-=(self.price)*(percent/100)
#         print(f"Discount Price : {self.price}")
# class ElectronicProduct(Product):
#     def __init__(self, name, price,warranty_years):
#         super().__init__(name, price)
#         self.warranty_years=warranty_years
#     def apply_discount(self,percent):
#         if percent>30:
#             print("Discount might be too much for electronic product ! ")
#         super().apply_discount(percent)
        

# p1=Product('Phone',15000)
# p1.apply_discount(8)
# e1=ElectronicProduct('earphone',650,1)
# e1.apply_discount(35)


# class Person():
#     def __init__(self,age):
#         self._age=age


#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self,new_age):
#         if new_age<0:
#             raise ValueError("Age cannot be negative")
#         self._age=new_age


# p1=Person(24)
# print(p1.age)
# p1.age=1
# print(p1.age)

# class Product():
#     def __init__(self,price):
#         self._price=price
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self,new_price):
#         if new_price<0:
#             raise ValueError("Price cannot be negative")
#         self._price=new_price

# p1=Product(500)
# print(p1.price)
# p1.price=300
# print(p1.price)
# p1.price=700
# print(p1.price)


# class  Employee():
#     def __init__(self,name,salary):
#         self._name=name
#         self._salary=salary
#     @property
#     def salary(self):
#         return self._salary
#     @salary.setter
#     def salary(self,new_salary):
#         if new_salary<0:
#             raise ValueError("salary cannot be negative")
#         self._salary=new_salary

#     def give_raise(self,percentage):
#         if percentage<=0:
#             raise ValueError("Percentage cannot be 0 or negative")
#         self._salary+=self._salary*(percentage/100)
#         print(f"Salary has been raised at the rate of {percentage}%")
#     def __str__(self):
#         return f"Name : {self._name}, Salary : {self._salary}"
    
# e1=Employee('Arun',10000)
# print(e1.salary)
# e1.salary=7000
# e1.give_raise(4)
# print(e1.salary)
# print(e1)
# e1.give_raise(0)


# class Rectangle():
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height

#     def area(self):
#         print(f'Area : {self.width*self.height}')
#     @classmethod
#     def square(cls,x):
#         if isinstance(x,int):
#             return cls(x,x)
#         else:
#             print("Enter only integer values ! ")
#     @staticmethod
#     def is_square(rect):
#         return rect.width==rect.height
              
         
#     def __str__(self):
#         return f"Width : {self.width} , Height : {self.height}"
    

# r1=Rectangle(6,8)
# r1.area()
# print(r1.square(2))

# print(r1)
# print(Rectangle.is_square(r1))
            
# r1 = Rectangle(6, 8)
# r1.area()

# r_new = Rectangle.square(2)
# print(r_new)

# print(Rectangle.is_square(r_new))


# class Author():
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f" Name Of Author : {self.name}"

# class Book():
#     def __init__(self,title,author_obj):
#         self.title=title
#         self.author_obj=author_obj

#     def __str__(self):
#         return f"Title : {self.title} , Name Of Author : {self.author_obj.name}"
    
#     def show(self):
#         print(self)


# a1=Author('Aryn')
# print(a1)
# b1=Book('GoatLife',a1)
# print(b1)
# b1.show()

# class Engine():
#     def __init__(self,horsepower):
#         self.horsepower=horsepower

#     def __str__(self):
#         return f"HorsePower : {self.horsepower}"

# class Car():
#     def __init__(self,model,engine_obj):
#         self.model=model
#         self.engine_obj=engine_obj
#     def __str__(self):
#         return f"Model : {self.model} , HorsePower : {self.engine_obj}"
    
#     def show(self):
#         print(self)
    

# e1=Engine(790)
# print(e1)
# c1=Car('Bike',e1)
# print(c1)
# c1.show()


# class Library():
#     def __init__(self,name):
#         self.name=name
#         self.books=[]

#     def add_book(self,book_obj):
#         if book_obj in self.books:
#             print("book alreday added to library ! ")
#         else:
#             self.books.append(book_obj)
        
#     def __str__(self):
#         return f"Name : {self.name} ,\nBook Details : {' , '.join([str(book) for book in self.books if self.books])}".rstrip() 
    
#     def show_books(self):
#         print(self)

    


# class Book():
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"title : {self.title} , Author : {self.author}"
    
# l1=Library('Thalassery')
# b1=Book('Goatlife','Benyamin')
# b2=Book('life','amin')
# l1.add_book(b1)
# l1.add_book(b2)
# print(b1)
# print(b2)
# print(l1)
# l1.show_books()

# class Bank():
#     def __init__(self,account_holder_name,account_number):
#         self.account_holder_name=account_holder_name
#         self.account_number=account_number
#         self._balance=0
    
#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self,new_balance):
#         if new_balance<0:
#             raise ValueError("Balance cannot be  negative amount ! ")
#         self._balance=new_balance

#     def deposit(self,deposit):
#         if deposit<0:
#             raise ValueError("Cannot deposit negative amount ! ")
#         self._balance+=deposit
    

#     def withdraw(self,withdraw_amount):
#         if withdraw_amount>self.balance:
#             raise ValueError("Not enough balance ! ")
#         self._balance-=withdraw_amount

#     def __str__(self):
#             return f"Account Holder Name : {self.account_holder_name}\nAccount Number : {self.account_number}\nBalance : {self.balance} "



# b1=Bank('Arun',84647)
# b1.deposit(6000)
# print(b1.balance)
# b1.withdraw(2500)
# print(b1.balance)
# print(b1)


# class Student():
#     def __init__(self,name,roll_number,grades):
#         self.name=name
#         self.roll_number=roll_number
#         self.grades=grades
#         self.mark_to_grade={'A+':100,
#                        'A':90,
#                        'B+': 85,
#                        'B': 80,
#                        'C+': 75,
#                        'C': 70,
#                        'D+': 65,
#                        'D': 60,
#                        'F': 50}

    
#     def grade(self,score):
#         if score >= 90:
#             return 'A'
#         elif score >= 80:
#             return 'B'
#         elif score >= 70:
#             return 'C'
#         elif score >= 60:
#             return 'D'
#         else:
#             return 'F'
        
#     @property    
#     def find_average(self):
#         average=sum(self.mark_to_grade[g] for g in self.grades)/len(self.grades)
#         return self.grade(average)

    
#     def add_grade(self,grade):
#         for g in grade:
#             if isinstance(g,str) and g in self.mark_to_grade:
#                 self.grades.append(g)
#             else:
#                 print("enter correct grades ! ")

#     def __str__(self):
#         return f"Name : {self.name}\nRoll No. : {self.roll_number}\nGrades : {self.grades}"


# s1=Student('Arun',45,['A','B','C+','A+'])
# s1.add_grade(['D','C'])
# print(s1)
# print(s1.find_average)

# class Rectangle():
#     def __init__(self,width,height):
#         self.height=height
#         self.width=width

#     @property
#     def perimeter(self):
#         return 2*(self.height+self.width)

#     @property
#     def area(self):
#         return self.height*self.width
#     @classmethod
#     def square(cls,x):
#         if isinstance(x,int):
#             return cls(x,x)
#         else:
#             raise ValueError("Only integer values are accepted ! ")
        
#     def __str__(self):
#         return f"Height : {self.height} , Width : {self.width}"
            
# r1=Rectangle(4,6)
# print(r1.perimeter)
# print(r1.area)
# r2=Rectangle.square(5)
# print(r2)
# print(r1)

# class Vehicle():
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#     def __str__(self):
#         return f"Make : {self.make} , Model : {self.model}"
    
# class Car(Vehicle):
#     def __init__(self, make, model,no_of_doors,is_sports_car):
#         super().__init__(make, model)
#         self.no_of_doors=no_of_doors
#         self.is_sports_car=is_sports_car

#     def __str__(self):
#         return super().__str__()+f", Number of doors : {self.no_of_doors} , Is it a sports car : {self.is_sports_car}"
        
        

# v1=Vehicle('honda','city')
# print(v1)
# c1=Car('hyuindai','creta',4,'no')
# print(c1)

# class LibraryMember():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.list_of_borrowed_books=[]
#     def add_new_book(self,book_title):
#         self.list_of_borrowed_books.append(book_title)

#     def return_book(self,book_title):
#         if book_title in self.list_of_borrowed_books:
#             self.list_of_borrowed_books.remove(book_title)
#         else:
#             raise ValueError("Book not borrowed from here ! ")
            
#     def __str__(self):
#         return f"Name : {self.name} , Age : {self.age} , Borrowed Books : {self.list_of_borrowed_books}"
    

    
# l1=LibraryMember('Arun',23)
# l1.add_new_book("Goatlife")
# l1.add_new_book("Life of pi")
# print(l1)
# l1.return_book("Goatlife")
# print(l1)


# class Employee():
#     def __init__(self,name,employee_id):
#         self.name=name
#         self.employee_id=employee_id
        

#     def calculate_pay(self):
#         return 0
    
    

#     def __str__(self): 
#         return f"Name : {self.name} , Employee ID :{self.employee_id} ,Monthly Salary : {self.calculate_pay()} "
    
    
    
# class HourlyEmployee(Employee):
#     def __init__(self, name, employee_id,hourly_rate,hours_worked):
#         super().__init__(name, employee_id)
#         self.hourly_rate=hourly_rate
#         self.hours_worked=hours_worked
    

#     def calculate_pay(self):
#         return self.hourly_rate*self.hours_worked
    
#     def __str__(self):
#         return f"[Hourly]  Name : {self.name} , Employee ID :{self.employee_id} , Hourly Rate : {self.hourly_rate} , Hours Worked : {self.hours_worked} , Salary : {self.calculate_pay()}"
    
    


    
# class SalariedEmployee(Employee):
#     def __init__(self, name, employee_id,monthly_salary):
#         super().__init__(name, employee_id)
#         self.monthly_salary=monthly_salary

#     def calculate_pay(self):
#         return self.monthly_salary
    

#     def __str__(self):
#         return f"[salaried]  Name : {self.name} , Employee ID :{self.employee_id} , Monthly Salary : {self.calculate_pay()} "
    

# class PayrollSystem():
#     def __init__(self):
#         self.employees=[]
        
#     def add_employee(self,employee_obj):
#         if employee_obj in self.employees:
#             raise Exception("Object already added ! ")
#         self.employees.append(employee_obj)
       
#     def show(self):
#         for e in self.employees:
#             print(e)




# e1=Employee('Vineeth',5464)
# print(e1)
# h1=HourlyEmployee('Arun',883,500,20)
# s1=SalariedEmployee('Amal',564,25000)
# p1=PayrollSystem()
# p1.add_employee(e1)
# p1.add_employee(s1)
# p1.add_employee(h1)
# print(h1)
# print(s1)
# p1.show()



# from math import pi
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     def __init__(self):
#         super().__init__()
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         super().__init__()
#         if width<=0 or height<=0:
#             raise ValueError("Width and height cannot be negative or 0  ! ")
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*self.height
#     def perimeter(self):
#         return 2*(self.height+self.width)
    
#     def __str__(self):
#         return f"[Rectangle]  Width : {self.width} , Height : {self.height} , Area : {self.area():.2f} , Perimeter :  {self.perimeter():.2f}"

# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__()
#         if radius<=0:
#             raise ValueError("Radius cannot be negative or 0  ! ")
#         self.radius=radius

#     def area(self):
#         return pi*self.radius**2
#     def perimeter(self):
#         return 2*pi*self.radius
    
#     def __str__(self):
#         return f"[Circle]  Radius : {self.radius} , Area : {self.area():.2f} , Perimeter :  {self.perimeter():.2f}"



# shapes=[Rectangle(6,7),Circle(8),Rectangle(9,4)]
# for shape in shapes:
#     print(shape)


# from abc import ABC,abstractmethod
# class Animal(ABC):
#     def __init__(self,name,species):
#         super().__init__()
#         self.name=name
#         self.species=species

#     @abstractmethod
#     def sound(self):
#         pass
#     def __str__(self):
#         return f"Name : {self.name} , Species : {self.species}"

#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name!r},species={self.species!r})"
    


# class Lion(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)

#     def sound(self):
#         return f" GRRrrrrr......"
    
#     def __str__(self):
#         return f"Lion - "+super().__str__()+f", Sound : {self.sound()}"
    
    
    
# class Elephant(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)

#     def sound(self):
#         return f"Eella phaant  ..la......"
    
#     def __str__(self):
#         return f"Elephant - "+super().__str__()+f", Sound : {self.sound()}"
    
    
    

# class Monkey(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)

#     def sound(self):
#         return f"MOoooonnnkeyyyyyy......"
    
#     def __str__(self):
#         return f"Monkey - "+super().__str__()+f", Sound : {self.sound()}"
    
    
    
# class Zoo():
#     def __init__(self):
#         self.name='Banglore zoo'
#         self.location="Banglore"
#         self.list_of_animals=[]

#     def add_animal(self,animal_obj):
#         if animal_obj in self.list_of_animals:
#             raise ValueError("Object already added ! ")
#         self.list_of_animals.append(animal_obj)
    
#     def show_all_animals(self):
#         if self.list_of_animals:
#             for a in self.list_of_animals:
#                 print(a)

#     def make_all_sound(self):
#         if self.list_of_animals:
#             for a in self.list_of_animals:
#                 print(a.sound())

#     def __repr__(self):
#             return f"{self.__class__.__name__}(name={self.name!r},location={self.location!r},List of animals={self.list_of_animals!r})"

# l1=Lion('Panthera','Leo')
# print(l1)
# print(l1.sound())
# e1=Elephant('Elephas','maximus')
# print(e1)
# print(e1.sound())
# m1=Monkey('Macaca','maca')
# print(m1)
# print(m1.sound())
# z1=Zoo()
# z1.add_animal(l1)
# z1.add_animal(e1)
# z1.add_animal(m1)
# z1.show_all_animals()
# z1.make_all_sound()
# print(repr(l1))
# print(repr(m1))
# print(repr(z1))


# def greet(name):
#     return f"hello,{name}!"
# def custom_greet(func):
#     return func("Arun")

# print(custom_greet(greet))

# def announce(func):
#     def wrapper(*args,**kwargs):
#         print("Befor the function ! ")
#         func(*args,**kwargs)
#         print("After the function ! ")
#     return wrapper
# @announce
# def msg():
#     print("Announcing hello! ")

# msg()

# def repeat(n):
#     def decorator(func):
#         def wrapped(*args,**kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapped
#     return decorator

# @repeat(3)
# def msg(name):
#     print(f"Hello {name}")
        
# msg('arun')

# def repeat_and_announce(n,msg):
#     def decorator(func):
#             def wrapped(*args,**kwargs):
#                 for i in range(n):
#                     print(msg)
#                     func(*args,**kwargs)
#             return wrapped
#     return decorator

# @repeat_and_announce(2, "Running hello...")
# def say_hello():
#     print("Hello!")

# say_hello()

# import time
# def time_it(func):
#     def wrapper(*args,**kwargs):
#         print(f"function {func.__name__} started.....")
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(f"function {func.__name__} ended.....")
#         print(f"elapsed time : {end-start:.4f} seconds")
#         return end-start
#     return wrapper




# @time_it
# def example_function():
#     for _ in range(1000000):
#         _=2**0.5
# elapsed=example_function()


# def log_return(func):
#     def wrapper(*args,**kwargs):
#         print(f"calling function {func.__name__}")
#         print(f"Arguments : {args},{kwargs}")
#         result=func(*args,**kwargs)
#         print(f"return :{result}")
#         return result
#     return wrapper





# @log_return
# def multiply(a, b):
#     return a * b

# multiply(5,6)


# def memorize(func):
#    cache={}
#    def wrapper(*args):
#        if args in cache:
#             print(f"Returning cached result for {args}")
#             return cache[args]
#        result=func(*args)
#        cache[args]=result
#        return result   
#    return wrapper



# @memorize
# def fibonacci(n):
#     if n==0:
#         return n
#     elif n==1:
#         return[0,1]
#     else:
#         series=fibonacci(n-1).copy()
#         series.append(series[-1]+series[-2])
#         return series

# print(fibonacci(5))
# fibonacci(3)
# fibonacci(9)
# fibonacci(5)
# fibonacci(3)

# class EvenCounter():
#     def __init__(self,n):
#         self.current=2
#         self.end=n

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current<=self.end:
#             num=self.current
#             self.current+=2
#             return num
#         else:
#             raise StopIteration


# e=EvenCounter(20)
# for i in e:
#     print(i)

# class Fibonacci():
#     def __init__(self,n):
#         self.a=0
#         self.b=1
#         self.count=0
#         self.end=n
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count>=self.end:
#             raise StopIteration
#         value=self.a
#         self.a,self.b=self.b,self.b+self.a
#         self.count+=1
#         return value
        
        



# f=Fibonacci(10)
# for i in f:
#     print(i)
          

# class EvenNumber():
#     def __init__(self,n):
#         self.n=n
#         self.start=2

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start<=self.n:
#             num=self.start
#             self.start+=2
#             return num
#         else:
#             raise StopIteration
        
# e=EvenNumber(100)
# for _ in e:
#     print(_)

# class ReverseList():
#     def __init__(self,number_list):
#         self.number_list=number_list
#         self.n=len(number_list)-1


#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.n>=0:
#             num=self.number_list[self.n]
#             self.n-=1
#             return num
#         else:
#             raise StopIteration
        
# r=ReverseList([4,2,5,6,1,5])
# for _ in r:
#     print(_)


# class SkipIterator():
#     def __init__(self,number_list):
#         self.number_list=number_list
#         self.n=len(number_list)
#         self.i=0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.i<self.n:
#             num=self.number_list[self.i]
#             self.i+=2
#             return num
#         else:
#             raise StopIteration
        
# s=SkipIterator([4,2,5,6,1,5])
# for _ in s:
#     print(_)


# def even_number_generators(n):
#     i=2
#     print("printing even number")
#     while(i<=n):
#         yield i
#         i+=2

# def odd_number_generators(n):
#     i=1
#     print("printing odd number")
#     while(i<=n):
        
#         yield i
#         i+=2

# def combine(n):
#     yield from even_number_generators(n)
#     yield from odd_number_generators(n)

# for i in combine(8):
#     print(i)

# def reverse_list(l):
#     n=len(l)-1

#     while(n>=0):
#         yield l[n]
#         n-=1
# for n in reverse_list([2,3,1,6,2,5,3]):
#     print(n)

# def fibonacci(n):
#     a=0
#     b=1
#     count=1
#     while(count<=n):
#         yield a
#         a,b=b,a+b
#         count+=1

# for n in fibonacci(10):
#     print(n)

# class CountIterator:
#     def __init__(self, n):
#         self.n = n
#         self.i = 1

#     def __iter__(self):
#         print("Iterator __iter__ called")
#         return self

#     def __next__(self):
#         print(f"__next__ called: current = {self.i}")
#         if self.i <= self.n:
#             val = self.i
#             self.i += 1
#             return val
#         else:
#             print("StopIteration raised")
#             raise StopIteration

# # Manual loop
# it = CountIterator(3)
# iter_obj = iter(it)        # triggers __iter__
# print(next(iter_obj))      # triggers __next__ (prints 1)
# print(next(iter_obj))      # prints 2
# print(next(iter_obj))      # prints 3
# print(next(iter_obj))      # triggers StopIteration


# def count_generator(n):
#     print("Generator started")
#     i = 1
#     while i <= n:
#         print(f"Yielding {i}")
#         yield i
#         i += 1
#     print("Generator exhausted")

# # Manual loop
# gen = count_generator(3)
# iter_obj = iter(gen)       # creates generator object
# print(next(iter_obj))      # prints "Yielding 1" and returns 1
# print(next(iter_obj))      # prints "Yielding 2" and returns 2
# print(next(iter_obj))      # prints "Yielding 3" and returns 3
# print(next(iter_obj))      # prints "Generator exhausted", then StopIteration
# import os
# print("Looking in:", os.getcwd())


# def read_line(file_path):
#     with open(file_path,"r") as f:
#         for line in f:
#             yield line

# def non_empty_line(lines):
#     for line in lines:
#         if line.strip():
#             yield line

# def strip_line(lines):
#     for line in lines:
#         yield line.strip()

# def to_uppercase(lines):
#     for line in lines:
#         yield line.upper()


# def pipeline(file_path):
#     lines= read_line(file_path)
#     lines=non_empty_line(lines)
#     lines=strip_line(lines)
#     yield from to_uppercase(lines)

# for l in pipeline(r"C:\Users\gokul\OneDrive\Desktop\python\oop.txt"):
#     print(l)

from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Decorated")
#         return func()
#     return wrapper

# @greet
# def greet():
#     """Greets the user"""
#     print("Hello!")

# print(greet.__name__)   # ✅ 'greet'
# print(greet.__doc__)    # ✅ 'Greets the user'


# from functools import wraps

# def decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print("hello")
#         print(f"[log] function :{func.__name__}")
#         func(*args,**kwargs)
#     return wrapper



# def logger(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"[log] function1 :{func.__name__}")
#         result=func(*args,**kwargs)
#         return result.upper()
#     return wrapper



# @decorator
# @logger
# def greet():
#     """greeting the user"""
#     print("greeeeeeettt!    >>>")
#     return 'greet'
# greet()
# print(greet.__name__)
# print(greet.__doc__)


# from functools import wraps

# def repeat(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             result=[]
#             for _ in range(n):
#                 print(f"Run {_ + 1}")
#                 result.append(func(*args,**kwargs))
#             return result
#         return wrapper
#     return decorator

# @repeat(10)
# def greet(x):
#     print('Greet ! ')
#     return x**5


# print(greet(8))
# print(greet.__name__)
# import time 

# class Timer():
#     def __enter__(self):
#         self.start=time.time()
#         print("Timer has started..... ..")
#         return self
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         self.tt=time.time()-self.start
#         print(f"Timer has ended,time taken for the process to complete :{self.tt:.4f} seconds")
#         if exc_type:
#             print("An exception occured!")
#             print("Type:", exc_type)
#             print("Message:", exc_val)
#             return True
        

# with Timer():
#     for _ in range(10000000):
#         1/0
# import time
# from contextlib import contextmanager
# @contextmanager
# def timer():
#     start=time.time()
#     print("Timer has started..... ..")
#     yield
#     tt=time.time()-start
#     print(f"Timer has ended,time taken for the process to complete :{tt:.4f} seconds")

# with timer():
#      for _ in range(10000000):
#         pass


# def logger(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"[LOG] calling function :{func.__name__} ")
#         return func(*args,**kwargs)
#     return wrapper

# @logger
# def non_empty_lines(lines):
#     for line in lines:
#         if line.strip():
#             yield line

# @logger
# def strip_lines(lines):
#     for line in lines:
#         yield line.strip()

# @logger
# def to_upper(lines):
#     for line in lines:
#         yield line.upper()

# def pipeline(file):
#     lines = non_empty_lines(file)
#     lines = strip_lines(lines)
#     lines = to_upper(lines)
#     return lines

# @contextmanager
# def filereader(file_path):
#     f=open(file_path,"r")
#     try:
#         yield f
#     finally:
#         f.close()

# with filereader("oop.txt") as file:
#     for line in pipeline(file):
#         print(line)

# from contextlib import contextmanager                                    #contextmanager and decorator combined
# from functools import wraps
# import os
# import time
# log_file=os.path.join(os.path.dirname(__file__),"log.txt")

# def log_to_file_decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         with open(log_file,'a') as f:
#             result=func(*args,**kwargs)
#             f.write(f'\nfunction name : {func.__name__}\nArgs: {args}, Kwargs : {kwargs}\nReturn value : {result}\n')
#             return result
#     return wrapper


# @contextmanager
# def log_timer(task_name="Unnamed task"):
#     start=time.time()
#     try:
#         yield 
#     finally:
#         elapsed_time=(time.time())-start
#         with open(log_file,"a") as f:
#             f.write(f"[TIMER] {task_name} , Execution time : {elapsed_time:.4f}seconds\n")
        
        


# @log_to_file_decorator
# def multiply(a,b):
#     return a*b



# with log_timer("multiplying 5 and 9"):
#     print(multiply(5,9))



# with timer():
# with log_timer():
#     for _ in range(1000000):
#         _*2


# @log_to_file_decorator
# def greet(name,msg="hello"):
#     return f"{msg},{name}"

# greet("Arun",msg="hi")
# greet("Alice")


# def divide(a,b):
#     try:
#         print("starting operations..")
#         result=a/b
#     except ZeroDivisionError:
#         print("zero division error")
#     else:
#         print("division successfull!")
#         print(f"Result : {result}")
#     finally:
#         print("Mission successful")
        
    
# divide(4,0)
# class InsufficientFunds(Exception):
#     pass


# def withdraw(balance,W_amount):
#     if W_amount>balance:
#         raise InsufficientFunds(" you don't have enough money in your account")
#     else:
#         print("withdraw successful")
#         balance-=W_amount
#         return balance
# try:
#     withdraw(40000,600)
# except Exception as e:
#     print(f"Exception caught : {e}")

# from functools import reduce
# cube=lambda x:x**3
# sum=lambda x,y:x+y
# even=lambda x: x%2==0
# print(cube(4))
# print(sum(4,6))
# print(even(8))

# nums=[2, 3, 4, 5]
# num2=[1, 5, 10, 20]
# num3=[1, 2, 3, 4, 5, 6]
# num4=[4, 15, 2, 20, 3]
# num5=[1, 2, 3, 4]
# num6=[3, 7, 1, 9, 5]
# evenfilter=list(filter(lambda x:x%2==0,num3))
# greaterthan10=list(filter(lambda x:x>10,num4))
# add10=list(map(lambda x:x+10,num2))
# cubes=list(map(cube,nums))
# print(cubes)
# print(add10)
# print(evenfilter)
# print(greaterthan10)
# m=reduce(lambda x,y:x*y,num5)
# mx=reduce(lambda x,y:max(x,y),num6)
# print(m)
# print(mx)

# from functools import reduce
# lines = ["  Apple", "", "Banana", "  ORANGE  ", "apple", "banana", "  "]
# line=list(filter(lambda x:x.strip(),lines))
# lin=list(map(lambda x:x.strip(),map(lambda x:x.lower(),line)))
# seen=set()
# unique=list(filter(lambda x:not(x in seen or seen.add(x)),lin))
# print(sorted(unique))

# emails = [
#     " alice@example.com  ",
#     "BOB@EXAMPLE.COM",
#     "charlie@example.com",
#     "bob@example.com",
#     "noatsymbol.com",
#     "ALICE@example.com",
#     " daniel@example.com"
# ]
# filtered_email=list(filter(lambda x:'@' in x,emails))
# strip_email=list(map(lambda x:x.strip(),map(lambda x:x.lower(),filtered_email)))
# seen=set()
# remove_duplicate_email=sorted(list(filter(lambda x:not(x in seen or seen.add(x)),strip_email)))
# print(remove_duplicate_email)