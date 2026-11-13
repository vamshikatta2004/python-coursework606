# #FUNCTIONS IN PYTHON
 # example 

#  def number():
#     if i in range(1,11):
#         print(i)

# number()
# number()

#for prime number

# def factors(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1
#     if c>2:
#         print("not prime")
#     else:
#         print("prime")

# factors(int(input("Enter a number: ")))

#SIMPLE METHOD using return fuction

# def factors(n):
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return "not a prime number"
#     return "prime number"

# print(factors(int(input("Enter a number: , , , "))))

#sum of digits of a number

# def sum_of_digits(n):
#     sum=0
#     while n>0:
#         sum+=n%10
#         n//=10
#     return sum

# print(sum_of_digits(3546))

#reverse of a number

# def reverse(n):
#     rev=0
#     while n>0:
#         rev=rev*10+n%10
#         n//=10
#     return rev

# print(reverse(int(input("Enter a number: "))))

#output: Enter a number: 123445
#544321

#ARUGMENTS IN PYTHON

#POSITIONAL ARGUMENTS

# def display(name,email,password):
#     print("Name: ",name)
#     print("Email: ",email)
#     print("Password: ",password)

# display("John Doe", "john@example.com", "password123")


# output:
# Name:  John Doe
# Email:  john@example.com
# Password:  password123

#KEYWORD ARGUMENTS

# def display(name,email,password):
#     print("Name: ",name)
#     print("Email: ",email)
#     print("Password: ",password)

# display(name="John Doe", email="john@example.com", password="password123")
# display( email="jane@example.com",name="Jane Smith", password="password456")

#output:
# Name:  John Doe
# Email:  john@example.com
# Password:  password123
# Name:  Jane Smith
# Email:  jane@example.com
# Password:  password456

# DEFAULT ARGUMENTS

# def display(name,email,password, country=None):
#     print("Name: ",name)
#     print("Email: ",email)
#     print("Password: ",password)
#     print("Country: ",country)

# display("John Doe", "john@example.com", "password123")
# display("Jane Smith", "jane@example.com", "password456", "Canada")

#output:
# Name:  John Doe
# Email:  john@example.com
# Password:  password123
# Country:  None
# Name:  Jane Smith
# Email:  jane@example.com
# Password:  password456
# Country:  Canada

#   VARIABLE LENGTH ARGUMENTS

# def display(*n):
#     print(n)
# display(1, 2, 3, 4, 5)
# display(2,4,6,8,10,12)
# display(1,3,5,7,9,11)

#output:
# (1, 2, 3, 4, 5)   
# (2, 4, 6, 8, 10, 12)
# (1, 3, 5, 7, 9, 11)

#KEYWORD VARIABLE LENGTH ARGUMENTS

# def display(**n):
#     print(n)

# display(n1=1, n2=2, n3=3, n4=4, n5=5)
# display(n1=1,n3=3,n5=5)
# display(n2=2,n4=4)

#output:
# {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4, 'n5': 5}
# {'n1': 1, 'n3': 3, 'n5': 5}
# {'n2': 2, 'n4': 4}

# TO STORE DATA AND HIGH TO LOW MARKS FOR THREE STUDENTS THROUGH USER INPUT

# def highestmark(data):
#     max  = 0
#     res = ''
#     for i in data:
#         if data[i]>max:
#             max= data[i]
#             res= i

#     print(f"THE HIGHEST MARKS {res}:{max}")

# data={}

# for i in range(3):
#         name=input("Enter the name of student: ")
#         marks=int(input("Enter the marks of student: "))
#         data[name]=marks

# highestmark(data)  

#output:
# Enter the name of student: RAVI
# Enter the marks of student: 42
# Enter the name of student: RAMU
# Enter the marks of student: 56
# Enter the name of student: RAHUL
# Enter the marks of student: 99
# THE HIGHEST MARKS RAHUL:99

#LOWEST MARKS

# def lowestmark(data):
#     min = 100
#     res = ''
#     for i in data:
#         if data[i]<min:
#             min=data[i]
#             res=i
#     print(f"THE LOWEST MARKS {res}:{min}")

# data={}

# for i in range(3):
#     name=input("Enter the name of student: ")
#     marks=int(input("Enter the marks of student: "))
#     data[name]=marks

# lowestmark(data)  

#output:
# Enter the name of student: RAHUL
# Enter the marks of student: 30
# Enter the name of student: RAJU
# Enter the marks of student: 40
# Enter the name of student: RAHUL
# Enter the marks of student: 56
# THE LOWEST MARKS RAJU:40