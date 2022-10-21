import functions
functions.welcome() #Calling welcome function 
D_list = functions.one_d_list() #Calling one_d_list function and assigning the returned value in D_list
functions.display_book(D_list) #Calling display_book function
total_cost = 0 # Initializing total_cost 
books_name = "" # Initializing books_name
flag = True # Initializing flag
while flag == True:
    print("\nEnter '1' to borrow a book\nEnter '2' to return a book\nEnter '3' to exit") #Print statement to make the users aware about the work done by the program
    valid = True
    '''Try except'''
    while valid == True:
        try:
            value = int(input("Please enter a value: ")) #Taking value from the users
            break
        except:
            functions.invalid_dt() #Calling invalid_dt function
    if value == 1:
        '''For borrow'''
        functions.now_borrow() #Calling now_borrow function
        name = input("Enter the name of the person: ") #Taking name as input from users 
        t_cost, Book_name = functions.continue_borrow(D_list,functions.display_book,total_cost,name,books_name) #Calling continue_borrow function amd assigning the returned value in t_cost, Book_name
        functions.b_bill(t_cost,name,Book_name) #Calling b_bill function
    elif value == 2:
        '''For return'''
        functions.now_return() #Calling now_return function
        r_name = input("Enter the name of the person: ") #Taking r_name as input from users 
        functions.return_book(D_list,functions.display_book,r_name) #Calling return_book function  
    elif value == 3:
        '''For exit'''
        flag == False
        functions.ty_three() #Calling ty_three function
        break
    else:
        '''if book ID is not 1,2 or 3'''
        functions.valid_value() #Calling valid_value function
