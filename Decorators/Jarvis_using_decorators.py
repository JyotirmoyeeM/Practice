"""
So let's first understand what a constructor is, then we will move to decorators, and then we will move on to generators.
Till the time I didn't study these topics, these three sounded like something very advanced, alien-like, and new. Well, not only have I used it already, but also, according to their definition, it's way too simple as well. It's because of my low efforts, I fluked my interviews over this stupid, stupid question, which I already knew, used. 
When we learn Python with oops concept, we already understand that after the creation of a class, there is a requirement for the  creation of an object, 
So we can use the methods written in class in our objects.
But the thing is, every time we create an object, we need to initialise it as well, so there comes our constructor,

it's this special method __init__()

So basically, before we define methods inside classes, we define a object's attributes in an initialization method using constructor

def __init__(self) --- which is default constructor
or def __init__(self, parameters) --- which is parameterised constructore,

parameterised one used for objects that come with their own parameter.

Now, what is a decorator? 
See, sometimes you will create a method or function. But later, you will want to add more functionality to it or beautify it. But the thing is, in real life, where a full, lengthy line of code application is made, to add something, we really just want to add something, not change, not edit, just add. That's where decorators come into action.
You declare a decorator function ...or said additional functionality function, inside which you define a wrapper method/ function, inside which you write your additional functionality that you wanted to get added
or decorate the original function
Then what you do, you define this decorate function above the original function, then inside this decorate function, you return a wrapper method, then  just before your original function,
You add a symbol "@" and then you call your decorator function, and then voila, changes to the original have been added.
"""
def Jarvis_perfecting(func):
    def wrapper(*args, **kwargs):
        name = input("Name: ")
        if name.lower() == "jamie":
            print()
            print("OWNER RECOGNISED.")
            print()
            print("Welcome back Madam. How can i help you today?")
            print()
            task =input()
            print()
            print("Task understood. Innitaiting....")
            return func(task, *args, **kwargs )
        else:
            print()
            print(f"DETECTED INTRUDER. \nEnabling alarm systems,..")
    return wrapper
@Jarvis_perfecting
def Jarvis(task):
    print(f"Received Task: {task}")
    print()
    print("Curent Status: [Innitialising....]")
    print()
    print("Curent Status: [Processing...]")
    print()
    print("Curent Status: [Successful]")
    print()
    print(f"Message : {task} excuted successfully")

result = Jarvis()
if result:
    print(result)
