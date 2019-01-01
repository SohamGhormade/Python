#TODO
Create repositories on GitHub and then clone the repo locally.
Next,push the changes daily.
This applies to C#,C++ and Python.
Argo is "language agnostic"per job description but they provide you a python list.
#this is minor actually.
Perfect practice makes perfect.
Python will help overcome .NET bias.
*Activate virtual environment*
$python3.6 -m venv my_env
$source my_env/bin/activate

#Python is pretty cool
It is concise compared to other Object Oriented Languages like C++,C# and Java:
- You do not need to import using statements
- You can define a function with fewer keystrokes
e.g
C#:
void  printNumber(int n)
{
    Console.WriteLine(n);
}

Python :
def printNumber(): # no type declaration.Pretty dope!
  print n # no semicolon ,just indent


Python is the preferred choice for interviewing(CSMojo, TechLead )
The potential *downside* is that the methods in Python do not have return types.
That means fewer keystrokes but it also means that you should make a mental note of verifying that you are returning the correct value for every method without the method signature giving you a hint.
##Downsides
No access specifiers .Mitigate by using __private_method()
No pass by reference.Mitigate by using lists,dictionaries or single values as return value.
