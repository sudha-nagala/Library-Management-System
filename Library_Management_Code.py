import mysql.connector as a
conn = a.connect(host='sql12.freesqldatabase.com',user='sql12621331',password='1ssdLqTHym',database='sql12621331')
my_cursor=conn.cursor()
conn.commit()
#conn.close()
print('connection succesfully created')

#we are adding book
def addbook():
    book_name = input('enter book name: ')
    book_author = input('enter author name: ')
    book_code = input('enter book code: ')
    total_books = int(input('total books: '))
    subject = input('enter subject: ')
    data = (book_name, book_author, book_code, total_books, subject)
    sql = 'insert into books values (%s, %s, %s, %s, %s);'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    print('book added successfully')
    wait = input('press enter to continue')
    
    main()

#we are issuing book
def issuebook():
    sname = input('enter student name: ')
    reg_no = int(input('enter reg no: '))
    book_code = (input('enter book code: '))
    issue_date = input('enter date: ')
    data = (sname, reg_no, book_code, issue_date)
    sql = 'insert into issue values (%s, %s, %s, %s);'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    print('book issued successfully to:', sname)
    wait = input('press enter to continue')
    bookupdate(book_code, -1)
    main()

#we are returning book
def returnbook():
    sname = input('Enter student name: ')
    reg_no = int(input('Enter reg no: '))
    book_code = (input('Enter book code: '))
    return_date = input('Enter date: ')
    data = (sname, reg_no,book_code, return_date)
    sql = 'insert into return_books values (%s, %s, %s, %s);'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    print('book returned by:',sname)
    wait = input('press enter to continue')
    bookupdate(book_code, 1)

#updating about tracking of books
def bookupdate(book_code, update):
    sql_select = 'select total from books WHERE bcode = %s;'
    data = (book_code,)
    my_cursor = conn.cursor()
    my_cursor.execute(sql_select, data)
    myresult = my_cursor.fetchone()
    t = myresult[0] + update
    sql_update = 'update books SET total = %s WHERE bcode = %s;'
    data=(t,book_code)
    my_cursor.execute(sql_update, data)
    conn.commit()
    wait = input('press enter to continue')
    main()

#we delete book
def deletebook():
    book_code = input('enter book code: ')
    sql = 'delete from books WHERE bcode = %s;'
    data = (book_code,)
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    print('book deleted successfully')
    wait = input('press enter to continue')
    main()

#displays all book records
def displaybook():
    
    sql = 'select * from books;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    myresult = my_cursor.fetchall()
    for i in myresult:
        print('book_name:', i[0])
        print('book_author:', i[1])
        print('book_code:', i[2])
        print('total_books:', i[3])
        print('subject:', i[4])
        print('\n\n')
    wait = input('press enter to continue')   
    main()

#displays report about issued books
def report_issued_books():
    sql = 'select * from issue;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    myresult = my_cursor.fetchall()
    for i in myresult:
        print(myresult)
    wait = input('press enter to continue')   
    main()

#displays report about returned books
def report_return_books():
    sql = 'select * from return_books;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    myresult = my_cursor.fetchall()
    for i in myresult:
        print(myresult)
    wait = input('press enter to continue')
    main()

#calling main function
def main():
    print('''
    LIBRARY MANAGEMENT SYSTEM APPLICATION
    1. ADD BOOK
    2. ISSUE BOOK
    3. RETURN BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
    6. REPORT MENU
    7. EXIT PROGRAM
    ''')

    #select from options to perform required task
    choice = input('enter task no: ')
    
    if choice == '1':
        addbook()
    elif choice == '2':
        issuebook()
    elif choice == '3':
        returnbook()
    elif choice == '4':
        deletebook()
    elif choice == '5':
        displaybook()
    elif choice == '6':
        print('''REPORT MENU
        1. ISSUED BOOKS
        2. RETURNED BOOKS
        3. GO BACK TO MAIN MENU
        ''')
        choice = input('enter task no: ')
        if choice == '1':
            report_issued_books()
        elif choice == '2':
            report_return_books()
        elif choice == '3':
            main()
        else:
            print('please try again')
            main()
    elif choice == '7':
        print('Thank you and have a great day ahead')
    else:
        print('invalid please try again')
        main()

main()

