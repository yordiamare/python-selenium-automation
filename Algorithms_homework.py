
#  sum of digits in all numbers from n to 5
def sum(n):
   return (n * (n+1)) / 2

num = int(input("Input a number: "))
print(sum(num))

#max-value
def maximum(a, b, c):
    return max(a,b,c)

n1 = int(input("input first num: "))
n2 = int(input("input second num: "))
n3 = int(input("input third num: "))

print(maximum(n1,n2,n3))

3Count odd and even numbers
def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
     current_digit = n % 10
    if current_digit % 2:
         odds += 1
    else:
        evens += 1
        n = n // 10
    return ["Evens: " + str(evens), "Odds: " + str(odds)]
num = int(input("Input a number: "))
print(count_odd_even(num))