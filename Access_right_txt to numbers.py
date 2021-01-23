###################################################################################
# Now we are to convert access right of UNIX operating system from Text to        #
# its normal form in a numercial way.                                             #
# We will be using Python lists to collect a string after conversion & thereafter #
# we will be looking at single string conversion using keys:                      #
#           => r := 4                                                             #
#           => w := 2                                                             #
#           => x := 1
#      We still use user group and all for access a file in UNIX
####################################################################################

def Text_To_Num(Your_text):
    #enter your text
    li =list(Your_text.split("--"))
    return li


choice = int(input("Make a choice \t one(1)from numbers to text or (2) text to numbers access Rights\n"))
#remeber that the file access_Right UNIX.py is having the option one(1) 
''' so here we will be exectuting otion
number  two'''
if choice == 2:
    print("Text To Numerical U N I X Access Right in Python\n----------------\t-----------------------")
    string = str(input("Enter The word form of your Unix File \nNotice: separator used is -- \nCase sensitive Upper case not Included use lower case\nThe form is rwx--rx--rwx THE ORDER IS IMPORTANT: "))
    lis = list(Text_To_Num(string))
    _User = str(lis[0])
    _Group = str(lis[1])
    _All = str(lis[2])

    print("1. {0} is User \n2. {1} is Group\n3. {2} is All".format(_User,_Group,_All))
    if len(_User) == 3:
        #means we have READ, WRITE, AND EXECUTE
        if _User[0] =="r" and _User[1] == "w" and _User[2] == "x" :
            VarUser = 4 + 2 + 1
        else:
            VarUser=str("This is not possible. We are not allowed using other caracters\nThan (r) (w) (x)\nNo space, No ! > < ? : |\\ and other letters are allowed ")
        #The order is important
        
    elif len(_User) == 2:
        #means we use can either have rw or rx or even wx . make sure that the order is 
        # always RWX if not R order is WX and so on.
        if _User[0] == "r" and _User[1] == "w":
            VarUser = 4 + 2
        elif _User[0] =="r" and _User[1] == "x":
            VarUser = 4 + 1
        elif _User[0] =="w" and _User[1] == "x":
            VarUser = 2 + 1
        else:
                VarUser = str("This case is not possible")

    elif len(_User) == 1:
        if _User =="r":
            VarUser = 4
        elif _User == "w":
            VarUser = 2
        elif _User =="x":
            VarUser = 1
        else:
            VarUser = str("no other caracter except (r) (w) or (x) is allowed!")
    elif len(_User) == 0:
        VarUser = 0
    else:
        VarUser = str("Values can't go beyond or above 3 possibilities for Simple Unix permission. TRY LATER")
    print("User: \t")
    print(VarUser)

    if len(_Group) == 3:
        # we have READ, WRITE, AND EXECUTE
        if _Group[0] =="r" and _Group[1] == "w" and _Group[2] == "x" :
            VarGroup = 4 + 2 + 1
        else:
            VarGroup=str("This is not possible. We are not allowed using other caracters\nThan (r) (w) (x)\nNo space, No ! > < ? : |\\ and other letters are allowed ")
        #The order is important very important otherwise the error code will be provided
        
    elif len(_Group) == 2:
        
        if _Group[0] == "r" and _Group[1] == "w":
            VarGroup = 4 + 2
        elif _Group[0] =="r" and _Group[1] == "x":
            VarGroup = 4 + 1
        elif _Group[0] =="w" and _Group[1] == "x":
            VarGroup = 2 + 1
        else:
                VarGroup = str("This case is not possible")

    elif len(_Group) == 1:
        if _Group =="r":
            VarGroup = 4
        elif _Group == "w":
            VarGroup = 2
        elif _Group =="x":
            VarGroup = 1
        else:
            VarGroup = str("no other caracter except (r) (w) or (x) is allowed!")
    elif len(_Group) == 0:
        VarGroup = 0
    else:
        VarGroup = str("Values can't go beyond or above 3 possibilities for Simple Unix permission. TRY LATER")
    print("Group: \t")
    print(VarGroup)

    if len(_All) == 3:
        #means we have READ, WRITE, AND EXECUTE
        if _All[0] =="r" and _All[1] == "w" and _All[2] == "x" :
            VarAll = 4 + 2 + 1
        else:
            VarAll=str("This is not possible. We are not allowed using other caracters\nThan (r) (w) (x)\nNo space, No ! > < ? : |\\ and other letters are allowed ")
        #The order is important
        
    elif len(_All) == 2:
        #means we use can either have rw or rx or even wx . make sure that the order is 
        # always RWX if not R order is WX and so on.
        if _All[0] == "r" and _All[1] == "w":
            VarAll = 4 + 2
        elif _All[0] =="r" and _All[1] == "x":
            VarAll = 4 + 1
        elif _All[0] =="w" and _All[1] == "x":
            VarAll = 2 + 1
        else:
                VarAll = str("This case is not possible")

    elif len(_All) == 1:
        if _All =="r":
            VarAll = 4
        elif _All == "w":
            VarAll = 2
        elif _All =="x":
            VarAll = 1
        else:
            VarAll = str("no other caracter except (r) (w) or (x) is allowed!")
    elif len(_All) == 0:
        VarAll = 0
    else:
        VarAll = str("Values can't go beyond or above 3 possibilities for Simple Unix permission. TRY LATER")
    print("User: \t")
    print(VarAll)
    print("")
    if len(str(VarUser)) >10:
        VarUser = "0"
    if len(str(VarGroup)) >10:
        VarGroup = "0"
    if len(str(VarAll)) >10:
        VarAll = "0"
    print("User {0} Group {1} All {2}".format(VarUser,VarGroup,VarAll))
else:
    print("this choice is not required.")