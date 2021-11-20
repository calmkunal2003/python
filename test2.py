## FUNCTIONS

# sum function
def sum(num1, num2):

    def new_func(n1, n2):
        return n1 + n2
    return new_func(num1, num2)

total = sum(10, 20)
print(total(10,20))


def sqr_dict():
     dict = {i:i**2 for i in range(1,21)}
     return dict
     return dict.keys() # print only keys

print(sqr_dict())