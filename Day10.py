# This is the project that makes calculator
def format_name():
    f_name = input("what is your first name? \n").capitalize()
    l_name = input("what is your last name name? \n").capitalize()
    return(f"{f_name} {l_name}")

#%%
# The lecture uses title or at least in pycharm the title doesn't work
def format_name2(f_name, l_name):
    f_name = f_name.capitalize()
    l_name= l_name.capitalize()
    return(f"{f_name} {l_name}")
#%%
format_name2("MOSA", "RAHIMI")
#%%
def format_name3(f_name, l_name):
    if f_name == "" or l_name == 0:
        return "no name or info provided"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Result: {f_name} {l_name}"
#%%
format_name3("", "")

#%%
def is_leap(year):
    if year % 4 == 0:
        if year %100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """"This is a doc string."""
    if month >12 or month <1:
        return f"sorry! invalid data"
    month_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month -1]
        

#TODO don't change the code below:
year = int(input("enter a year: "))
month = int(input("enter a month: "))
days = days_in_month(year, month)
print(days)

#%%
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n1

def multiplication(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiplication,
    "/":division
}

num1 = int(input("what is the first number? \n"))
num2 = int(input("what is the second number? \n"))

for ops in operation:
    print(ops)
    
ops_symbol= input("Pick an operation from above! \n ")

num2 = int(input("what is the second number? \n"))

calculation_function = operation[ops_symbol]

answer = calculation_function(num1, num2, )

print(f"{num2} {ops_symbol} {num2} = {answer}")


#%%
for i in operation:
    print(i)
#%%
