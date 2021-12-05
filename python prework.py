
# Question 1)
def hello_name(username):
    username = input("username".upper())
    print ("hello"+ username + "!")
    print (hello_name(username))

#Question 2)
def first_odds():
 numbers = range (101)
 range (0,101)
 for number in numbers :
        if number % 2 != 0 : 
            print (number)
#Question 3
def max_num_in_list(a_list):
 maxnum=0
 for number in a_list:
    if number > maxnum:
      maxnum=number
 return maxnum

 #Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
      return True 
    if a_year %4 != 100:
      return True
    if a_year%400==0:
       return True
    elif  a_year % 4!=0:
           return False 
    elif a_year %4 == 100:
         return False
    else: a_year %400 !=0
    return False 
    
#Question 5
def is_consecutive(a_list):

 sorted(1)==list(range(min(1)),max(1)+(1))
if sum(1) == max:
  True
if sum(1) != max:
  False