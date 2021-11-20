## FUNCTIONS

def sum(num1, num2):

    def new_func(n1, n2):
        return n1 + n2
    return new_func(num1, num2)

total = sum(10, 20)
print(total(10,20))