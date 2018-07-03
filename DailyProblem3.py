'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

numbers = [1,2,7,-4,5,3]
score = len (numbers)
for i in range(score):
    pos = 0
    while pos < score and i != numbers[pos]:
        print("i={} / pos={} / score={}" .format(i,pos,score))
        pos+=1
        input()
    if pos > score or i == score-1:
        print(i+1)
        break

