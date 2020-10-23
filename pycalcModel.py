# The Model handles the business logic, in this case,
# the business logic deals with math calculations

# create a global constant to handle errors:
ERROR_MSG = 'ERROR!'

def evaluateExpression(expression):
    # create a function that evaluates math expressions from user
    try:
    # use eval() to evaluate a string as an expression and return the result if successful
        result = str(eval(expression, {}, {}))
    except Exception:
    # if unsuccessful, return the error message
        result = ERROR_MSG

    return result

def greet():
    print('hello from pyCalcModel')

# greet()
#print('hello from evaluateExpression')
