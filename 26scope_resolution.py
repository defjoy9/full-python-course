# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# variable scope v

def func1(): # a is local to func1
    a = 1
    print(a)

def func2(): # b is local to func2
    b = 2
    print(b)

func1()
func2()

def func1(): # enclosed
    x = 1

    def func2():
#        x= 2
        print(x)
    func2()

# x is global
def func1(): # a is local to func1
    print(x)

def func2(): # b is local to func2
    print(x)

x = 3

# built-in

from math import e

def func1():
    print(e)

e = 3 # global e
func1()