import datetime
def welcome():
    """Function to Dislpay welcome message"""
    print("\n************************************************\n Hello and Welcome to library management system\n************************************************\n") #print statement
def valid_value():
    """Function to Dislpay enter valid value message"""
    print("\n**********************************************\n The entered value is invalid please try again\n**********************************************\n") #print statement
def ty_three():
    """Function to Dislpay thank you message"""
    print("\n************************************************\n Thankyou for using my library management system\n************************************************\n") #print statement
def now_borrow():
    """Function to Dislpay now you will  borrow message"""
    print("\n****************************\n You will now borrow a book\n****************************\n") #print statement
def now_return():
    """ Function toDislpay now you will  return message"""
    print("\n****************************\n You will now return a book\n****************************\n") #print statement
def error_book():
    """Function to Display invalid book id"""
    print("\n************************************\n Please provide a valid Book ID !!!\n************************************\n") #print statement
    print("\n************************************\n Try again with a different book ID\n************************************\n") #print statement
def n_avilable_book():
    """Function to Display out of stock"""
    print("\n***********************\n Book out of stock !!!\n***********************\n") #print statement
def avilable_display():
    """Function to Dislpay Book is available """
    print("\n***********************\n Book is available !!!\n***********************\n") #print statement
def ty_alt():
    """Function to Display thank you message after borrowing a book"""
    print("\n*****************************************************\n            Thankyou for borrowing book/books\n Be sure to return it within 10 days or pay the fine\n*****************************************************\n") #print statement    
def fine():
    """Function to Display thank you message after returning a book late"""
    print("\n******************************************************************\n                Thankyou for returning the book\n You have returned the book late so you will have to pay the fine\n      If you want to return another book enter 2 down below\n******************************************************************\n") #print statement    
def thankyou():
    """Function to Display thank you message after returning a book in time"""
    print("\n**********************************************************************************************\n                               Thankyou for returning the book\n If you want to return another book enter 2 down below, enter 1 to borrow and enter 3 to exit\n**********************************************************************************************\n") #print statement    
def invalid_dt_bookid():
    """Function which Displayes ID should be a integer between 1-5 when execption occer while assigning book ID"""
    print("\n***********************************\n ID should be a integer between 1-5\n***********************************\n") #print statement    
def invalid_dt():
    """Function which Displayes when Enter a integer value when execption occer while assigning value"""
    print("\n***********************\n Enter a integer value\n***********************\n") #print statement

def one_d_list():
    """Convert the text file to 1D list"""
    file = open("data.txt","r")
    '''Initializing lists'''
    dd_list = []
    data_list = []
    for line in file:
        line = line.replace("\n","") #Replacing '\n' with empty siring 
        dd_list.append(line.split(",")) #Converting to 2D list
    '''converting 2D list to 1D list'''
    for i in range(len(dd_list)):
        for j in range(len(dd_list[i])):
            data_list.append(dd_list[i][j])
    return data_list
def display_book(d_list):
    """Displays values of dictionary in a table. Takes dictionary as prremeter"""
    '''Column name'''
    print("---------------------------------------------------------------------") #Border line 
    print("Book Id         Book Name            Author       Quantity   Price") #Column name
    print("---------------------------------------------------------------------")#Border line
    '''Data of table'''
    print("   ",d_list[0],"     ",d_list[1]," ",d_list[2],"    ",d_list[3],"   ",d_list[4]) #details of with book ID 1
    print("   ",d_list[5],"     ",d_list[6]," ",d_list[7],"      ",d_list[8],"   ",d_list[9]) #details of with book ID 2
    print("   ",d_list[10],"    ",d_list[11],"",d_list[12],"     ",d_list[13],"   ",d_list[14]) #details of with book ID 3
    print("   ",d_list[15],"           ",d_list[16],"        ",d_list[17],"    ",d_list[18],"   ",d_list[19]) #details of with book ID 5
    print("   ",d_list[20],"        ",d_list[21],"    ",d_list[22],"    ",d_list[23],"   ",d_list[24])#details of with book ID 5
    print("---------------------------------------------------------------------")#Border line
def continue_borrow(D_list,display_book,total_cost,name,booksName):
    """To calculate total cost and all the books borrowed"""
    add = True #Initializing add
    book_cost , bookName = borrow_book(D_list) #Calling borrow_book function and assigning the returned value to book_cost and bookName
    total_cost += float(book_cost) #Adding book_cost of borrowed book and assigning to total_cost
    booksName += bookName+"\n" #Joining bookName of borrowed book and assigning it to booksName
    while add == True:
        YN = input("If tou want to borrow a another book type 'y', else type any onthe word or letter :")#Taking YN as input from the users
        if YN == "y":
            book_cost , bookName = borrow_book(D_list) #Calling borrow_book function and assigning the returned value to book_cost and bookName
            total_cost += float(book_cost) #Adding book_cost of borrowed book to total_cost
            booksName += bookName+"\n" #Joining bookName of borrowed book to booksName
        else:
            ty_alt() #alling ty_alt function
            break
    return total_cost, booksName
def borrow_book(data_list):
    """Function which decreases quantity, displays books, returns price and bookName"""
    '''Initializing price, bookName, flag, vld, vld1'''
    price = 0
    bookName = ""
    flag = True
    vld = True
    vld1 = True
    '''Exception handling'''
    while vld == True:
        try:
            bookID = int(input("Enter the book Id of the book you want to borrow:")) #Taking book ID as input from the users
            break 
        except:
            invalid_dt_bookid()#Calling invalid_dt function
    while flag == True:
        if bookID == 1:
            qnt = int(data_list[3]) #Assigning the 3 index data_list to qnt
            if qnt > 0:
                avilable_display() #Calling avalable_display function
                remove_book(bookID,qnt,data_list) #Calling remove_book function
                display_book(data_list) #Calling display_book functin
                price = cost(data_list,bookID) #Calling cost function 
                bookName = book_name(data_list,bookID) #Calling book_name function
                break
            else:
                n_avilable_book() #Calling n_avilable_book function
                while vld1 == True:
                    try:
                        bookID = int(input("Enter the book Id of a another book you want to borrow:")) #Taking book ID as input from the users
                        break
                    except:
                        invalid_dt_bookid()#Calling invalid_dt function
        elif bookID == 2:
            qnt = int(data_list[8]) #Assigning the 8 index data_list to qnt
            if qnt > 0:
                avilable_display()#Calling avalable_display function
                remove_book(bookID,qnt,data_list) #Calling remove_book function
                display_book(data_list) #Calling display_book functin
                price = cost(data_list,bookID) #Calling cost function
                bookName = book_name(data_list,bookID)#Calling book_name function
                break
            else:
                n_avilable_book() #Calling n_avilable_book function
                while vld1 == True:
                    try:
                        bookID = int(input("Enter the book Id of a another book you want to borrow:"))#Taking book ID as input from the users
                        break
                    except:
                        invalid_dt_bookid() #Calling invalid_dt function
        elif bookID == 3:
            qnt = int(data_list[13])#Assigning the 13 index data_list to qnt
            if qnt > 0:
                avilable_display()#Calling avalable_display function
                remove_book(bookID,qnt,data_list) #Calling remove_book function
                display_book(data_list)#Calling display_book functin
                price = cost(data_list,bookID)#Calling cost function
                bookName = book_name(data_list,bookID)#Calling book_name function
                break
            else:
                n_avilable_book() #Calling n_avilable_book function
                while vld1 == True:
                    try:
                        bookID = int(input("Enter the book Id of a another book you want to borrow:")) #Taking book ID as input from the users
                        break
                    except:
                        invalid_dt_bookid() #Calling invalid_dt function
        elif bookID == 4: 
            qnt = int(data_list[18])#Assigning the 18 index data_list to qnt
            if qnt > 0:
                avilable_display()#Calling avalable_display function
                remove_book(bookID,qnt,data_list)#Calling remove_book function
                display_book(data_list)#Calling display_book functin
                price = cost(data_list,bookID) #Calling cost function
                bookName = book_name(data_list,bookID) #Calling book_name function
                break
            else:
                n_avilable_book() #Calling n_avilable_book function
                while vld1 == True:
                    try:
                        bookID = int(input("Enter the book Id of a another book you want to borrow:")) #Taking book ID as input from the users
                        break
                    except:
                        invalid_dt_bookid() #Calling invalid_dt function
        elif bookID == 5:
            qnt = int(data_list[23])#Assigning the 23 index data_list to qnt
            if qnt > 0:
                avilable_display() #Calling avalable_display function
                remove_book(bookID,qnt,data_list)#Calling remove_book function
                display_book(data_list) #Calling display_book functin
                price = cost(data_list,bookID) #Calling cost function
                bookName = book_name(data_list,bookID)#Calling book_name function
                break
            else:
                n_avilable_book() #Calling n_avilable_book function
                while vld1 == True:
                    try:
                        bookID = int(input("Enter the book Id of a another book you want to borrow:"))#Taking book ID as input from the users
                        break
                    except:
                        invalid_dt_bookid()#Calling invalid_dt function
        else:
            error_book()
            break
    return price , bookName

def remove_book(bookID,quantity,data_list):
    """Update textfile and data list when borrowed"""
    '''Initializing qnt1,qnt2,qnt3,qnt4,qnt4'''
    qnt1 = data_list[3]
    qnt2 = data_list[8]
    qnt3 = data_list[13]
    qnt4 = data_list[18]
    qnt5 = data_list[23]
    file = open("data.txt","w")
    if bookID == 1:
        qnt1 = int(data_list[3]) - 1 #Updating variable qnt1
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+str(qnt1)+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 2:
        qnt2 = int(data_list[8]) - 1 #Updating variable qnt2
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+str(qnt2)+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 3:
        qnt3 = int(data_list[13]) - 1 #Updating variable qnt3
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+str(qnt3)+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 4:
        qnt4 = int(data_list[18]) - 1 #Updating variable qnt4
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+str(qnt4)+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 5:
        qnt5 = int(data_list[23]) - 1 #Updating variable qnt5
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+str(qnt5)+",$14.00")
    file.close()
    fnl_qnt = quantity-1 #Calculating quantity afrer borrow
    if bookID == 1:
        data_list[3] = str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
    elif bookID == 2:
        data_list[8] = str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
    elif bookID == 3:
        data_list[13] =  str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
    elif bookID == 4:
        data_list[18] = str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
    elif bookID == 5:
        data_list[23] = str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
def cost(data_list,bookID):
    """Retuens the price of the book borrowed"""
    if bookID == 1:
        price = data_list[4] #Assigning the 4 index data_list to price
        price = price.replace("$","") #Replacing $ with empty string 
    elif bookID == 2:
        price = data_list[9] #Assigning the 9 index data_list to price
        price = price.replace("$","") #Replacing $ with empty string
    elif bookID == 3:
        price = data_list[14] #Assigning the 14 index data_list to price
        price = price.replace("$","") #Replacing $ with empty string
    elif bookID == 4:
        price = data_list[19]#Assigning the 19 index data_list to price
        price = price.replace("$","") #Replacing $ with empty string
    elif bookID == 5:
        price = data_list[24]#Assigning the 24 index data_list to price
        price = price.replace("$","") #Replacing $ with empty string
    return price    
def book_name(data_list,bookID):
    """Returns book name which is borrowed"""
    bookName = "" #Initializing bookName
    if bookID == 1:
        bookName = data_list[1]#Assigning the 1 index data_list to bookName
    elif bookID == 2:
        bookName = data_list[6]#Assigning the 6 index data_list to bookName
    elif bookID == 3:
        bookName = data_list[11]#Assigning the 11 index data_list to bookName
    elif bookID == 4:
        bookName = data_list[16]#Assigning the 16 index data_list to bookName
    elif bookID == 5:
        bookName = data_list[21]#Assigning the 21 index data_list to bookName
    return bookName               
def b_bill(total_cost,name,booksName):
    """Write bill in a qnique file"""
    dnt = datetime.datetime.now()#Returns current date and time
    '''Creatimg unique name for file generation'''
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    randomValue = minute+second+microsecond
    '''File handling'''
    file = open("borrow_bill/b_"+name+randomValue+".txt","w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("Price of the book/books borrowed: $"+str(total_cost)+"\n")
    file.write("Date and Time of borrow: "+str(dnt)+"\n")
    file.write("Name of the book/books borrowed: \n"+booksName)
    file.close()
def return_book(data_list, display_book,name):
    """Function to take book ID. If valid ID is entered call other functions else call error function"""
    '''initializing boolean variables'''
    flag = True
    vld = True
    vld1 = True
    '''Exception handling'''
    while vld == True:
        try:
            bookID = int(input("Enter the book Id of the book you are going to return:")) #Taking bookID as input from users
            break 
        except:
            invalid_dt_bookid()#Calling invalid_dt_bookid
    while vld == True:
        try:
            days = int(input("Enter the number of days you borrowed the book:")) #Taking days as input from users
            break
        except:
            invalid_dt() #Calling invalid_dt function
    fine_yn(days,data_list,name,bookID)#Calling fine_yn function
    while flag == True:
        if bookID == 1:
            qnt = int(data_list[3]) #Assigning the 3 index data_list to qnt
            add_book(bookID,qnt,data_list) #Calling add_book function 
            display_book(data_list) #Calling display_book functin
            break
        elif bookID == 2:
            qnt = int(data_list[8]) #Assigning the 8 index data_list to qnt
            add_book(bookID,qnt,data_list)#Calling add_book function 
            display_book(data_list)#Calling display_book functin
            break
        elif bookID == 3:
            qnt = int(data_list[13])#Assigning the 13 index data_list to qnt
            add_book(bookID,qnt,data_list)#Calling add_book function 
            display_book(data_list)#Calling display_book functin
            break
        elif bookID == 4:
            qnt = int(data_list[18])#Assigning the 18 index data_list to qnt
            add_book(bookID,qnt,data_list)#Calling add_book function 
            display_book(data_list)#Calling display_book functin
            break
        elif bookID == 5:
            qnt = int(data_list[23]) #Assigning the 23 index data_list to qnt
            add_book(bookID,qnt,data_list)#Calling add_book function 
            display_book(data_list)#Calling display_book functin
            break
        else:
            error_book()#Calling error_book functin
            break
def add_book(bookID,quantity,data_list):
    """Function to update textfile and data list when borrowed"""
    '''Initializing qnt1,qnt2,qnt3,qnt4,qnt4'''
    qnt1 = data_list[3]
    qnt2 = data_list[8]
    qnt3 = data_list[13]
    qnt4 = data_list[18]
    qnt5 = data_list[23]
    '''file handling'''
    file = open("data.txt","w")
    if bookID == 1:
        qnt1 = int(data_list[3]) + 1 #Updating variable qnt1
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+str(qnt1)+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 2:
        qnt2 = int(data_list[8]) + 1 #Updating variable qnt2
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+str(qnt2)+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 3:
        qnt3 = int(data_list[13]) + 1 #Updating variable qnt3
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+str(qnt3)+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 4:
        qnt4 = int(data_list[18]) + 1 #Updating variable qnt4
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+str(qnt4)+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 5:
        qnt5 = int(data_list[23]) + 1 #Updating variable qnt5
        '''Writing updated variable in txt file'''
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+str(qnt5)+",$14.00")
    file.close()
    fnl_qnt = quantity + 1 #Calculating quantity afrer return
    if bookID == 1:
        data_list[3] = str(fnl_qnt)#Assigning fnl_qnt to the 3 index data_list
    elif bookID == 2:
        data_list[8] = str(fnl_qnt)#Assigning fnl_qnt to the 8 index data_list
    elif bookID == 3:
        data_list[13] =  str(fnl_qnt)#Assigning fnl_qnt to the 13 index data_list
    elif bookID == 4:
        data_list[18] = str(fnl_qnt)#Assigning fnl_qnt to the 18 index data_list
    elif bookID == 5:
        data_list[23] = str(fnl_qnt)#Assigning fnl_qnt to the 23 index data_list
def fine_yn(days,data_list,name,bookID):
    """Finction to determine fine needs to be payed or not"""
    if days > 10:
        r_f_bill(name,data_list,bookID,days)#Calling r_f_bill function
        fine()#Calling fine function
    else:
        r_nf_bill(name,data_list,bookID) #Calling r_nf_bill function
        thankyou() #Calling thankyou function
def r_f_bill(name,data_list,bookID,days):
    """Function to write in the txt file if returned late"""
    bookName = book_name(data_list,bookID) #Calling book_name function
    fine_amt = (days-10) * 2 #calculating fine amount
    dnt = datetime.datetime.now() #Current returns date and time
    '''Creatimg unique name for file generation'''
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    randomValue = minute+second+microsecond
    '''File handling'''
    file = open("retuen_bill/"+name+randomValue+".txt","w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("fine: $"+str(fine_amt)+"\n")
    file.write("Date and Time of return:"+str(dnt)+"\n")
    file.write("Name of the returning book: "+bookName)
    file.close()
def r_nf_bill(name,data_list,bookID):
    """Function to write in the txt file if returned in time"""
    bookName = book_name(data_list,bookID)#Calling book_name function
    fine_amt = 0 # fine is 0 because book is returned in time
    dnt = datetime.datetime.now() #Current returns date and time
    '''Creatimg unique name for file generation'''
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    randomValue = minute+second+microsecond
    '''File handling'''
    file = open("retuen_bill/r_"+name+randomValue+".txt","w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("fine: $"+str(fine_amt)+"\n")
    file.write("Date and Time of return:"+str(dnt)+"\n")
    file.write("Name of the returning book: "+bookName)
    file.close()
