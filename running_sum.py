'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
'''
import random

# currently using low values to test things and find solutions
def randomized_list():
    list=[]
    for i in range(10000):
        list.append(random.randint(1,1000))
    return list

# outputs summed list
def stored_sum_solution(original_list):
    stored_sum=0
    new_list=[]
    for i, v in enumerate(original_list):
        add=original_list[i]+stored_sum
        new_list.append(add)
        stored_sum=add
    return new_list

#you cant pay me to nest the for loops and add each one manually thats absolutely not happening nope

'''
a=randomized_list()
b=stored_sum_solution(a)
print(f'OG: {a} \nSUMMED: {b}')
print(str(len(a)) + ', ' + str(len(b)))
input()
'''