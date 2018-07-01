'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
numbers = [4,7,3,5,9,34,53,68,24]
k =int(input("Enter the  main number:"))
score = len (numbers)
for  i  in range(score):
    for a in range(i,score):
        if a != i:
            value = i + a
            if  k == value:
                print ("{} + {} is {}" .format(i,a,k))
