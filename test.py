for i in range (0,1000):
    mylist = list(set(str("%03d" % i)))
    if len(mylist) == 3 :
        print ((mylist))


