import random
#https://replit.com/@JamesClare/Ari19thJan#Ari's%20Hw%20for%20Lesson/two_sum.py

#add dad's solution
#make timer and UI to choose what to time

# 2sum problem generator -- returns array, target
def generator():
    length_of_list=1001
    target=random.randint(3, 6000)
    hash_table={}
    array=[]
    target_reach=False
    index_of_array=0

    # until list is desired length
    while len(array) <= length_of_list:

        # generate random number
        iterative_num_value=random.randint(1,5999)

        # check for duplicate, if there's a duplicate go back and make new number
        if iterative_num_value in hash_table:
            continue

        # check to see if solution already exists
        counter=target-iterative_num_value
        if counter in hash_table:
            if target_reach==True:
                continue

        # add number to list
        else:
            if target_reach==False:
                if counter in hash_table:
                    if iterative_num_value+counter==target:
                        print(f'{iterative_num_value} + {counter} is equal to {target} this is in gen initial')
                        target_reach=True
            hash_table[iterative_num_value]=index_of_array
            index_of_array += 1
            array.append(iterative_num_value)

    # if no solution has been found yet
    if target_reach==False:
        # remove last list entry
        array.remove(array[length_of_list-1])

        # random list selection to generate (a valid) counter from it
        rand=random.randint(0,length_of_list-2)
        while array[rand]>=target and target/2!=array[rand]:
            rand = random.randint(0, length_of_list - 1)
        # add to list and shuffle
        array.append(target - array[rand])
        random.shuffle(array)

    return array, target

# returns both indeces and explanatory string
def BIG_O(array, target):
    for index, val in enumerate(array):
        for i in range(len(array)):
            if i>index:
                if array[index]+array[i]==target:
                    return index, i, \
                           f'BIG O: The arrays\'s #{index} index (which is {array[index]}) + array\'s #{i} index (which is {array[i]}) = {target}.'
                    #print(f'A LOOP: {a[index]} + {a[i]} = {b}')
                    #print(f'({index}, {i}) ')

# returns both indeces and explanatory string
def hashtable(array, target):
    hashtable={}
    for index, value in enumerate(array):
        counter=target-value
        if counter in hashtable:
            return index, hashtable[counter], \
                   f'MOST EFFICIENT: The arrays\'s #{index} index (which is {array[index]}) ' \
                   f'+ array\'s #{hashtable[counter]} index (which is {counter}) = {target}.'
        else:
            hashtable[value]=index

#################-----------------

'''
a, b = generator()
print(BIG_O(a, b))
print(hashtable(a, b))
'''


