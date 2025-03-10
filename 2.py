# WAP to print uppercase of every even character of the string.
def myfunc(s):
    print(s)
    # converting string into list 
    l=list(s)
    print("list is ",l)
    for u in range(len(l)):
        if u%2==0:
            l[u]=l[u].upper()
    # now joining the list
    return ''.join(l)

s=input("Enter a string ")
print (myfunc(s))

