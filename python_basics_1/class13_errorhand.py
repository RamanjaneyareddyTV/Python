# exception Handling or error handling
#try except finally
'''
arithmetic error
zerodivision error
import error
module error
key error
value error
name error
indentation error
syntax error
type error
keyboard interrupt
index error

try:
    a=1
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("this is finally")
x=-1
if x<0:
    raise Exception("below zero numbers are not allowed")'''

a='kiran'
b=1
try:
    c=a+b
    print(c)
except Exception as e:
    print(e)