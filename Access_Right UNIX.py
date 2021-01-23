#
"""
     ======================= LINUX SYSTEM ========================
    | This is File Access Right In Unix using the powerful python |
    | Key Points to remember :                                    |
    | > read is witten as r and value is to be 4                  |
    | > write is written as w and its value is 2                  |
    | > x stands for exceute and its value  is 1                  |
    | we have 3 kinds of users User, Group and all every having   |
    | levels in terms of access rights in UNIX.                   |
    | This IS Python Simulation of Acess rights       in UNIX     |
    |                               TAKE THE RISK Ciza Mihigo     |
    ==============================================================
"""

def Conv_num_txt(number =2):
    #print("enter Your Number:")
    number= str(number)
    if len(number)==3:
        print("{0} = User/Admin Access Right" .format(number[0]))
        #idenitifying access rights for the User
        i_num =int(number[0])
        if 4 <= i_num <= 7 :
            read = i_num - 4
            user ="r"
            if read >= 2:
                read -= 2
                user +="w"
                if read >= 1:
                    read -=1
                    user += "x"
            print(user)
        elif 2 <= i_num < 4 :
            read = i_num - 2
            user ="w"
            if read >= 1:
                read -=1
                user += "x"
            print(user)
        elif 1 <= i_num < 2:
            read= i_num-1
            user = ""
            if read == 0:
                user +="x"
            print(user)
        elif i_num == 0:
            user= "_ _ _"
            print(user)
            user =" "
        else:
            ("Case not involved")

        print("{0} = Group Access Right" .format(number[1]))
        #idenitifying access rights for the Group of users
        i_num =int(number[1])
        if 4 <= i_num <= 7 :
            read = i_num - 4
            group ="r"
            if read >= 2:
                read -= 2
                group +="w"
                if read >= 1:
                    read -=1
                    group += "x"
            print(group)
        elif 2 <= i_num < 4 :
            read = i_num - 2
            group ="w"
            if read >= 1:
                read -=1
                group += "x"
            print(group)
        elif 1 <= i_num < 2:
            read= i_num-1
            group = ""
            if read == 0:
                group +="x"
            print(group)
        elif i_num == 0:
            group= "_ _ _"
            print(group)
            group= " "
        else:
            pass
               
        print("{0} = All Access Right" .format(number[2]))
        #idenitifying access rights for All Users
        i_num =int(number[2])
        if 4 <= i_num <= 7 :
            read = i_num - 4
            All_u ="r"
            if read >= 2:
                read -= 2
                All_u +="w"
                if read >= 1:
                    read -=1
                    All_u += "x"
            print(All_u)
        elif 2 <= i_num < 4 :
            read = i_num - 2
            All_u ="w"
            if read >= 1:
                read -=1
                All_u += "x"
            print(All_u)
        elif 1 <= i_num < 2:
            read= i_num-1
            All_u = ""
            if read == 0:
                All_u +="x"
            print(All_u)
        elif i_num == 0:
            All_u= "_ _ _"
            print(All_u)
            All_u =" "
        else:
            pass

        print("ACCESS RIGHT:\t {0}--{1}--{2}. UNIX SYSTEM ACCESS RIGHTS".format(user,group,All_u))

    else:
        print("the length of your number should not exceed 3 charcaters.")


print("this is the simmulation of access right in UNIX OS made with Python")
print("choose the type of conversion you want (1) or (2)")
print("(1) Convert from Numeric values to text string \n(2) Convert from text to Numeric Values")

choice=input("Enter Your choice: ")
Dchoice = choice.isdigit()

if Dchoice == True:
    choice = int(choice)
    print("Numbered choice")
    if choice == 1:
        num = int(input("enter Access Right Value: "))
        Conv_num_txt(num)
    elif choice == 2:
        pass
    else:
        pass

else:
    for i in range(0,1):
        print("recommancez \nChoisir (1) ou (2):")
        choice = input()



    
