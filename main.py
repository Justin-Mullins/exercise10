'''

Exercise 10


The arguments must all be of the same type and know how to respond to the + operator.Thus,
the function should work with numbers, strings, lists, and tuples, but not with sets and dicts.

The result should be a new, longer sequence of the type provided by the parameters. So, the
result of mysum('abc', 'def') will be the string abcdef , and the result of
mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6] . Of course, it should also
still return the integer 6 if we invoke mysum(1,2,3) .

'''

def mysum(*items):
    if not items:  # If items is empty
        return ()
    else:
        output = items[0]
        for item in items[1:]:
            output += item
        return output

print(mysum(*([1, 2, 4, 5], [4, 6, 7])))
print(mysum(*('today', '0', 'car', '4', '19')))
print(mysum(*((1231, 12, 136), (5828, 853, 968))))
print(mysum(*(135, 5917, 9186, -293)))
print(mysum(*()))
