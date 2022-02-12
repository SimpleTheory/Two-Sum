import running_sum

array = running_sum.randomized_list()

def builtin_sort(array):
    array.sort()

#########################################

'''
How am I going to let the computer know the binary

1111
0110
1000
0101
0011
0110

for index in list
    bin->string

for num in range longest num    
    for index in list
        if string[num]==1
        list+=[list.pop(index))
'''
#-----------------
'''
Tried to make an efficient sorting system for numbers
The idea is to make them binary
Then to metaphorically line the them up in files each according to its place like
 10
000
010
111
Then go through each number in the list with a file if it is 1 pop it up to the end of the list then go to the next file and repeat

So with this

Original list | 1st run through:
001             11(1)
010             00(1)
000             01(0)             
100             00(0)
111             10(0)

2nd:
0(1)0
1(1)1
0(0)1
0(0)0
1(0)0

3rd:
1 00
1 11
0 10
0 01
0 00



'''
def binator(array):
    longest_num=1
    for index in range(len(array)):
        s = array[index]
        s = bin(s)
        s = str(s)
        s=s.split('0b')
        s=s[1]
        array[index]=s

        if len(array[index])>longest_num:
            longest_num=len(array[index])

    return array, longest_num

def bin_sort(longest_num, bin_list):
    for num in range(-1, -1*longest_num+1, -1):
        for index in range(len(bin_list)):
            #if exists
            try:
                if bin_list[index][num] == '1':
                    bin_list.append(bin_list[index])
                    bin_list.remove(bin_list[index])
            except:
                pass
    return bin_list


def unbinate(bin_list):
    a = bin_list
    for index in range(len(bin_list)):
        a[index]=int(a[index], 2)
    return a

#----------

# gives binary list as well as longest number


bin, longnum = binator(array)

# sorts list
c=bin_sort(longnum, bin)
b=unbinate(c)

# converts back to integers and prints
print(c)
print(b)


