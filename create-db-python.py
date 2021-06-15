import datetime

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="ranjan", passwd="1234", database="ranjandb")

mycursor = mydb.cursor()


def createlog (w):
    file = open('Log.txt', 'a')
    file.write("\n" + str((datetime.datetime.now())).split(".")[0] + "-User entered :- " + str(w))
    file.close()

def resetlog():
    file = open('log.txt','w')
    file.write("")
    file.close()


while True:

    print("Welcome,Select choice")
    print("1.Addition of Data")
    print("2.Deletion of Data")
    print("3.To view Data")
    print("4.Updation of Data")
    print("5.To Exit")
    x = int(input("Enter your Choice:-"))
    #resetlog()
    createlog(x)

    if x == 1:
        sqlform = "Insert into students(name,roll) value(%s,%s)"
        while True:
            a = input("Name-")
            createlog(a)
            b = input("Roll no-")
            createlog(b)
            data = (a, b)
            mycursor.execute(sqlform, data)

            mydb.commit()
            print("Data Added Successfully")
            createlog("Data added Successfully")
            choice = input("Do you want to Continue")
            if choice == "y":
                continue
            else:
                break

    elif x == 2:
        while True:
            code = (input("Name-"))
            createlog(code)
            k = "DELETE from students WHERE name=  '{}'".format(code)
            mycursor.execute(k)
            mydb.commit()
            print("Data Deleted Successfully")
            createlog("Data Deleted Successfully")
            choice = input("Do want to Continue")
            createlog(choice)
            if choice == "y":
                continue
            else:
                break

    elif x == 3:
        while True:
            c = (input("Name-"))
            query = "Select * from students where name='{}' ".format(c)
            mycursor.execute(query)
            myresult = mycursor.fetchall()

            for row in myresult:
                print(row)
            choice = input("Do want to Continue")
            if choice == "y":
                continue
            else:
                break

    elif x == 4:
        while True:
            f = str(input("Enter Name-"))
            g = int(input("Enter new roll-"))

            # sql = "update students set roll= 20 where name= '{}'".format(f)
            sql = "update students set roll= '{}' where name= '{}'".format(g, f)
            mycursor.execute(sql)
            mydb.commit()
            print("Data Updated Successfully")
            choice = input("Do want to Continue")
            if choice == "y":
                continue
            else:
                break

    elif x == 5:
        print("Bye Bye")
        exit(0)

    else:
        print("Wrong Choice")
        exit(0)
