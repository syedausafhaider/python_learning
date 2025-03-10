# 3. WAP to find the sum of elements in a list.
import functools
def find_sum_in_list1(l):
    sum=0
    for i in range(len(l)):# for i in l:
        sum+=l[i]
    return sum

def find_sum_in_list2(l):
    return sum(l)

def find_sum_in_list3(l):
    return functools.reduce(lambda i,j:i+j,l)

l=[10,20,30,40,50,60]
print ("Using func 1 : ",find_sum_in_list1(l))
print ("Using func 2 : ",find_sum_in_list2(l))
print ("Using func 3 : ",find_sum_in_list3(l))

