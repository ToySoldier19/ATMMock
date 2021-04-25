# register
#     - first name, last name, email, password
#     - generate new user account
    
# login
#     - account no, email, password




atmDenominations = [500,1000,2000,5000]
import random

database = {
    7779148913: ['El', 'Rey', 'lhanray96@yahoo.com', 'Esty09', 425876 ],
    4176269384: ['Rey', 'Lugero', 'lhanray96@gmail.com', 'King01', 523843],
    3686669776: ['Larry', 'Dee', 'deeciouslarry987@yahoo.com', 'Dee987', 635262 ]
    }   

def init(): 
    print("Welcome to King's Bank")
        
    accountyn = int(input("Do you have an account with us?: 1 (yes) 2(no) \n"))
    
    if(accountyn == 1): 
        login()
    elif(accountyn == 2):
        register()
    else:
        print("You have selected an Invalid Option.")
        init()
        
def login():
    print("*****Login to your Account*****")
      
    UserAccountNo = int(input("Enter Your Account Number \n"))
    password = input("Enter Your Password \n")
        
    for accountNo, userDetails in database.items():
        if(accountNo == UserAccountNo):
            if(userDetails[3] == password):
                bankOperations(userDetails)
                
            elif(userDetails[3] != password):
                print("Incorrect Password")
                login()
                
    else:
        if(accountNo != UserAccountNo):
            print("Incorrect Account Number")
            login()

  
def register():
    print("***** PLEASE REGISTER *****")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("Input your email address \n")
    password = input("Create your password \n")
    
    accountNo = generatebankaccount()
    newAccBal = 0
    database[accountNo] = [ first_name, last_name, email, password, 0 ]
    
    print("Your Account has been created successfully.")
    print("This is your account no: %d" % accountNo)
    print("Please keep it safe")
    print("Your Account Balance is %d" % newAccBal)
    print("** *** **** *** **")    
    login()

def bankOperations(user):
    
    print("Welcome %s %s " % ( user[0], user[1] ) )
    
    selectedOps = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3)Check Balance (4) Logout (5) Exit \n"))
    
    if(selectedOps == 1):
        depositOp(user)
    
    elif(selectedOps == 2):
        withdrawalOp(user)
        
    elif(selectedOps == 3):
        checkAccBal(user)

    elif(selectedOps == 4):
        logout(user)
    
    elif(selectedOps == 5):
        print("Thank You for Banking with us.")
        exit()
    
    else:       
        print("Invalid Option Selected")
        bankOperations(user)
    
def withdrawalOp(user):
    print('Enter Amount To Withdraw')
    for i in atmDenominations:
        print(atmDenominations.index(i) +1, end=' ')
        print(" ",i)
    
    accBalance = user[4]
    selectedAmount = float(input('Please enter an Amount \n'))

    if(selectedAmount in atmDenominations):
        print('Transaction Completed. Please take your Cash')
        newBalance = accBalance - selectedAmount 
        print('Your new balance is %d' % newBalance)
        newTrx = int(input("Do you want to perform another transaction? (1) Yes (2) No \n"))
        
        if(newTrx == 1):
            bankOperations(user)
        elif(newTrx == 2):
            logout(user)
        
    else:
        print('Invalid Entry, please try again')
    
def depositOp(user):
    print('Enter Amount To Deposit')
    for i in atmDenominations:
        print(atmDenominations.index(i) +1, end=' ')
        print(" ",i)
    
    accBalance = user[4]
    selectedAmount = float(input('Please enter an Amount \n'))

    if(selectedAmount in atmDenominations):
        print('Transaction Completed')
        newBalance = selectedAmount + accBalance
        print('Your new balance is %d' % newBalance)
        newTrx = int(input("Do you want to perform another transaction? (1) Yes (2) No \n"))
        
        if(newTrx == 1):
            bankOperations(user)
        elif(newTrx == 2):
            logout(user)
        
    else:
        print('Invalid Entry, please try again')
    
    
def checkAccBal(user):
        print('Your account balance is %d' % user[4])
        print('Thank you for Banking with us')
        newTrx = int(input("Do you want to perform another transaction? (1) Yes (2) No \n"))
        
        if(newTrx == 1):
            bankOperations(user)
        elif(newTrx == 2):
            logout(user)
    
def logout(user):    
    confirmLogout = int(input("Are you sure you want to logout? (1) Yes (2) No \n"))
                        
    if (confirmLogout == 1):
        login()
    elif(confirmLogout == 2):
        bankOperations(user)
    else:
        print("Invalid Input")
        logout(user) 
    
def generatebankaccount():
    
    return random.randrange(1111111111,9999999999)
    




### KB BANKING SYS ###
init()
