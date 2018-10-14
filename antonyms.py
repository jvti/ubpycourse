a={}
while True:
    word=input("\nenter your desired word:   ")
    if word in a:
        print (a[word])
    elif word in a.values():
        for i in a:
            if a[i]==word:
                print(i)
    else:
        print ("\n I dont know the antony of ",word)
        flag=input("\ndo you know?(y/N)   ")
        if flag == "y" or flag == "Y":
             a[word]=input(u"\nwhat is it:   ")
        else:
             print("\nOK, thanks")
        
