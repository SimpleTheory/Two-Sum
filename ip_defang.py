''' Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]". '''

# ip address is 4 blocks of num from 0-255
import random
def ipv4_generator():
    list=[]
    for i in range(4):
        list.append(str(random.randint(0,256)))
    ipv4 = '.'.join(list)
    return ipv4

def ip_defang_sol1(ipv4):
    temp=ipv4.split('.')
    defanged='[.]'.join(temp)
    return defanged

def ip_defang_sol2(ipv4):
    new_string=''
    for i in ipv4:
        if i=='.':
            new_string=new_string+ '[.]'
        else:
            new_string=new_string+i
    return new_string

def ip_defang_sol3(ipv4):
    x = ipv4.replace('.', '[.]')
    return x

a=ipv4_generator()
print(a)
print(ip_defang_sol1(a))
print(ip_defang_sol2(a))
print(ip_defang_sol3(a))



'''
Notes from Ari to James:

I did my homework in each file corresponding to the problem, I also made
generators that would make the problem, as well as an extra credit timer that would time any code you choose to input from any file, because you recommended I should find different solutions and time them. 

I ran all the code locally so everything should work. To test out
the different generators and solutions in the homework. Go to the 
corresponding file, near the bottom there should be some code commented
out that will generate the problem and print the solution, given that you
"un-comment" the code and run the file.

regarding MAIN()
  I know this is not ideal because of the re-iterating
  generator in the code which can make the results variable,
  but I hope that the generator will average out to a certain
  time which can be used as a baseline for timing the functions.
  I tried to make it without the generator and having  the input
  created by the generated be stored in a seperate text file,
  but that was too hard.

Some Other Comments:
  I wanted to put my homework in the folders but it wasn't running because
  I don't know directories or file management, like, at all.

  I still want to update some of the code here before monday, 
  partiuclarly, I spoke with my Dad about two_sum and challlenged
  him as well, he came up with a unique solution which I haven't written
  among the two_sum solutions. In anycase, please check out
  the code, since I have I have written more than enough regardless.

'''