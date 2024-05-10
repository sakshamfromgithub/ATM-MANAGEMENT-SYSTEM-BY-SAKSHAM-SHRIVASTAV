#WELCOME TO ATM MANAGEMENT SYSTEM CREATED BY SAKSHAM SHRIVASTAV


import random
import time
import datetime


def title():
    try:
        print("WELCOME TO ATM MANAGEMENT SYSTEM CREATED BY SAKSHAM SHRIVASTAV\n ")
        print('\n[please enter ac no.21520 or 13070]\n')
        ac = int(input("enter your 5 digit a/c no."))
        print("checking...\n ")
        acdict = {21520: "Name - Saksham Shrivastav\na/c no. = 21520" , 13070: "Name - Pankaj kumar\na/c no. = 13070"}
        time.sleep(2)

        if ac == 21520:
            print(f"account details found\n{acdict[21520]}\n")
            acno()

        elif ac == 13070:
            print(f"account details found\n{acdict[13070]}")
            acno()
        else:
            print("invalid input! \nPlease enter a valid input🙂 ")
    except ValueError:
        print("\ninvalid input ! \n please enter valid a/c no.\n\n")
        title()


def moneytrans():
    acnum = int(input("enter receiver a/c no."))
    print('\n[please enter "barb0sadrep" or "BARB0SADREP"]\n')
    ifsc = input("enter receiver ifsc code=")
    print("**CHECKING BANK DETAILS...**")
    time.sleep(2)
    if ifsc == "BARB0SADREP" or "barb0sadrep":
        print("\n****BANK DETAILS FOUND**\n ")
        print("\nBANK NAME - BANK OF BARODA\tBRANCH - SADREPUR")
        amount = int(input("enter amount : "))
        mPin = int(input("enter your mPin for security reason :"))
        print('checking mpin..........')
        time.sleep(2)
        if mPin == 3098:
            confirmation = input("are you sure for transfer money type yes/no\n")
        if confirmation == "yes":
            print('intializing payments....')
            time.sleep(2)
            print(
                "transaction successful for rupees \n\n thanks for using mobile bank \n\t\t have a nice day \n do more oprations\n")
            title()
        elif confirmation == "no":
            print("transection canceled !\n try again...")
            title()

        else:
            print("transection canceled !\n try again...")
            title()
    else:
        print("bank not found please try again ")
        title()


def cashdep():
    amount = int(input("enter amount : "))
    print('please enter 3098')
    mPin = int(input("enter your mPin for security reason :"))
    if mPin == 3098:
        print('intializing payment.......')
        time.sleep(3)
        print("transaction successful for rupees ", amount,
              "\n\n thanks for using mobile bank \n\t\t have a nice day\ndo more oprations\n")
        title()
    else:
        print("invalid mPin \n\n Please try again...\n")
        title()

def acno(): 
 try:
    i = int(input(
        "enter operation do you perform \n\n PRESS 1 FOR CASH WITHDRAWAL \n PRESS 2 FOR MONEY TRANSFER \n PRESS 3 FOR CHECK BALANCE :"))
    if i == 1:
        print("you have selected cash withdrawal ")
        cashdep()

    if i == 2:
        print("you have selected money transfer ")

        moneytrans()
    if i == 3:
        mpn = int(input("enter your mpin : "))
        print("checking mpin....")
        time.sleep(2)
        if mpn == 3098:
            print("fetching your balance....")
            time.sleep(4)
            current_datetime = datetime.datetime.now()
            bal = random.randint(1000,100000)
            print(f"\nas on {current_datetime.strftime('%Y-%m-%d %H:%M:%S')} the clear balance in your account is rupees {bal}\ndo more operations\n")
            title()

        else:
            print('\ninvalid input! please enter valid input\n')
            title()

 except ValueError:
        print('\ninvalid input! please enter valid a/c no.\n')
        title()

#DRIVER CODE
try:
    acdict = {21520: "Name - Saksham Shrivastav\na/c no. = 21520",
              13070: "Name - Pankaj kumar\na/c no. = 13070"}
    print("WELCOME TO ATM MANAGEMENT SYSTEM CREATED BY SAKSHAM SHRIVASTAV \n")
    print('\n[please enter ac no.21520 or 13070]\n')
    ac = int(input("enter your 5 digit a/c no."))
    print("checking...\n ")
    time.sleep(2)
    if ac == 21520:
        print(f"account details found\n{acdict[21520]}\n")
        acno()
    elif ac == 13070:
        print(f"account details found\n{acdict[13070]}\n")
        acno()
    else:
        print("account not found \n please try again\n")
        title()
except ValueError:
    print('\ninvalid input! please enter valid a/c no.\n')
    title()