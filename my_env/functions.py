# this is a python function
# use def keyword
# "else if" becomes "elif"
def sign(x):
   if(x > 0):
       return 'positive'
   elif x < 0:
        return 'negative'
   else:
        return 'zero'

for x in [-1,0,1]:
  print(sign(x))

# use class keyword to define a class in python

class Greeter(object):
   # define a constructor --note the constructor name
   def __init__(self,name):# pass self(this)
    self.name = name # create an instance variable

   def greet(self, loud = False):
     # if condition has no brackets in Python
     if loud:
        print('HELLO, %s!' %(self.name.upper()))
     else:
        print('Hello, %s' % self.name)


g = Greeter('Fred')
g.greet()  # prints "Hello, Fred!"
g.greet(True)# prints "HELLO, FRED!"