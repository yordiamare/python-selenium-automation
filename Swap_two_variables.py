def swap_ab(a, b):
    #temp = a
    #a = a + b
    #b = a - b
    #a = a - b
   # b = temp
    a, b = b,a
    print(f'a = {a}, b = {b}')

a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a}, b = {b}')
swap_ab(a, b)