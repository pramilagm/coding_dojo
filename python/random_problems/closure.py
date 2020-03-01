# #the method of binding data to a function without actually passing them as parameters is called closure.
# Closure is function object that remembers the values of enclosing scope even the variable is not in the memory
# A function which is defined inside another function is known as nested function. Nested functions are able to access variables of the enclosing scope.
# In Python, these non-local variables can be accessed only within their scope and not outside their scope.


def outerFunction(text):

    def innerFunction():
        print(text)
    innerFunction()


outerFunction('hELLO')


def outerFunction(text):

    def innerFunction():
        print(text)
    return innerFunction


obj = outerFunction('Pramila')
obj()
