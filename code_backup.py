
def welcome():
    """Dislpay welcome message"""
    print("*************************************\n Hello and Welcome to library system\n*************************************\n\n")
def one_d_list():
    """Convert the text file to 1D list"""
    file = open("data.txt","r")
    dd_list = []
    data_list = []
    for line in file:
        line = line.replace("\n","")
        dd_list.append(line.split(","))
    for i in range(len(dd_list)):
        for j in range(len(dd_list[i])):
            data_list.append(dd_list[i][j])
    return data_list
def display_book(d_list):
    """Displays values of dictionary in a table. Takes dictionary as prremeter"""
    '''Column name'''
    print("---------------------------------------------------------------------\nBook Id         Book Name            Author       Quantity   Price\n---------------------------------------------------------------------")
    '''Data of table'''
    print("   ",d_list[0],"     ",d_list[1]," ",d_list[2],"    ",d_list[3],"   ",d_list[4])
    print("   ",d_list[5],"     ",d_list[6]," ",d_list[7],"      ",d_list[8],"   ",d_list[9])
    print("   ",d_list[10],"    ",d_list[11],"",d_list[12],"     ",d_list[13],"   ",d_list[14])
    print("   ",d_list[15],"           ",d_list[16],"        ",d_list[17],"    ",d_list[18],"   ",d_list[19])
    print("   ",d_list[20],"        ",d_list[21],"    ",d_list[22],"    ",d_list[23],"   ",d_list[24])
    print("---------------------------------------------------------------------")
def error_book():
    """Display invalid book id"""
    print("*************************************\n Please provide a valid Book ID !!!\n*************************************\n\n")
    print("*************************************\n Try again with a different book ID \n*************************************\n\n")
def n_avilable_book():
    """Display out of stock"""
    print("*************************************\n Book out of stock !!!\n*************************************\n\n")
def avilable_display():
    print("*************************************\n Book is available !!!\n*************************************\n\n")
def avilable_book(bookID,quantity,data_list):
    qnt1 = data_list[3]
    qnt2 = data_list[8]
    qnt3 = data_list[13]
    qnt4 = data_list[18]
    qnt5 = data_list[23]
    file = open("data.txt","w")
    if bookID == 1:
        qnt1 = int(data_list[3]) - 1
        file.write("1,Nineteen Eighty-Four,George Orwell,"+str(qnt1)+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 2:
        qnt2 = int(data_list[8]) - 1
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+str(qnt2)+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 3:
        qnt3 = int(data_list[13]) - 1
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+str(qnt3)+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 4:
        qnt4 = int(data_list[18]) - 1
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+str(qnt4)+",$16.00\n5,Invinsible Man,Ralph Ellison,"+qnt5+",$14.00")
    elif bookID == 5:
        qnt5 = int(data_list[23]) - 1
        file.write("1,Nineteen Eighty-Four,George Orwell,"+qnt1+",$9.99\n2,To Kill a Mockingbird,Harper Lee,"+qnt2+",$17.99\n3,The Catcher in the Rye,J.D.Salinger,"+qnt3+",$16.99\n4,Beloved,Toni Morrison,"+qnt4+",$16.00\n5,Invinsible Man,Ralph Ellison,"+str(qnt5)+",$14.00")
    file.close()
    fnl_qnt = quantity-1
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if bookID == 1:
                data_list[3] = str(fnl_qnt)
            elif bookID == 2:
                data_list[8] = str(fnl_qnt)
            elif bookID == 3:
                data_list[13] =  str(fnl_qnt)
            elif bookID == 4:
                data_list[18] = str(fnl_qnt)
            elif bookID == 5:
                data_list[23] = str(fnl_qnt)
def cost(data_list,bookID):
    if bookID == 1:
        price = data_list[4]
        price = price.replace("$","") 
    elif bookID == 2:
        price = data_list[9]
        price = price.replace("$","")
    elif bookID == 3:
        price = data_list[14]
        price = price.replace("$","")
    elif bookID == 4:
        price = data_list[19]
        price = price.replace("$","")
    elif bookID == 5:
        price = data_list[24]
        price = price.replace("$","")
    return price    
def borrow_book(data_list):
    """Function to check if the book id entered is available or not"""
    flag = True
    bookID = int(input("Enter the book Id of the book you want to borrow:"))
    while flag == True:
        if bookID == 1:
            qnt = int(data_list[3])
            if qnt > 0:
                avilable_book(bookID,qnt,data_list)
                display_book(data_list)
                price = cost(data_list,bookID)
                bookName = book_name(data_list,bookID)
                break
            else:
                n_avilable_book()
                bookID = int(input("Enter the book Id of the book you want to borrow:"))
        elif bookID == 2:
            qnt = int(data_list[8])
            if qnt > 0:
                avilable_book(bookID,qnt,data_list)
                display_book(data_list)
                price = cost(data_list,bookID)
                bookName = book_name(data_list,bookID)
                break
            else:
                n_avilable_book(bookID,qnt)
                bookID = int(input("Enter the book Id of the book you want to borrow:"))
        elif bookID == 3:
            qnt = int(data_list[13])
            if qnt > 0:
                avilable_book(bookID,qnt,data_list)
                display_book(data_list)
                price = cost(data_list,bookID)
                bookName = book_name(data_list,bookID)
                break
            else:
                n_avilable_book()
                bookID = int(input("Enter the book Id of the book you want to borrow:"))
        elif bookID == 4: 
            qnt = int(data_list[18])
            if qnt > 0:
                avilable_book(bookID,qnt,data_list)
                display_book(data_list)
                price = cost(data_list,bookID)
                bookName = book_name(data_list,bookID)
                break
            else:
                n_avilable_book()
                bookID = int(input("Enter the book Id of the book you want to borrow:"))
        elif bookID == 5:
            qnt = int(data_list[23])
            if qnt > 0:
                avilable_book(bookID,qnt,data_list)
                display_book(data_list)
                price = cost(data_list,bookID)
                bookName = book_name(data_list,bookID)
                break
            else:
                n_avilable_book()
                bookID = int(input("Enter the book Id of the book you want to borrow:"))
        else:
            error_book()
            break
    return price , bookName
      
def continue_borrow(D_list,display_book,total_cost,name,booksName):
    book_cost , bookName = borrow_book(D_list)
    total_cost += float(book_cost)
    booksName += bookName+"\n"
    while add == True:
        YN = input("If tou want to borrow a another book type 'y':")
        if YN == "y":
            book_cost , bookName = borrow_book(D_list)
            total_cost += float(book_cost)
            booksName += bookName+"\n"
        else:
            break
    return total_cost, booksName
def book_name(data_list,bookID):
    if bookID == 1:
        bookName = data_list[1]
    elif bookID == 2:
        bookName = data_list[6]
    elif bookID == 3:
        bookName = data_list[11]
    elif bookID == 4:
        bookName = data_list[16]
    elif bookID == 5:
        bookName = data_list[21]
    return bookName
                
def bill(total_cost,name,booksName):
    import datetime
    dnt = datetime.datetime.now() 
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    randomValue = minute+second+microsecond
    file = open(name+randomValue+".txt","w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("Price of the book/books borrowed: $"+str(total_cost)+"\n")
    file.write("date and Time of borrow:"+str(dnt)+"\n")
    file.write("Name of the book borrowed:/n"+booksName)
       
welcome()
D_list = one_d_list()
display_book(D_list)
total_cost = 0
books_name = ""
flag = True
add = True
while flag == True:
    print("\n\nEnter '1' to borrow a book\nEnter '2' to return a book\nEnter '3' to exit") #Print statement to make the users aware about the work done by the program
    value = int(input("Please enter a value:")) #Taking value from the users
    if value == 1:
        avilable_display()
        name = input("Enter the name of the person:")
        t_cost, B_name = continue_borrow(D_list,display_book,total_cost,name,books_name)
        bill(t_cost,name,B_name)
    elif value == 2:
        return_book()  
    elif value == 3:
        flag == False
        #message
        break
    else:
        print("Error")
        #Error message
