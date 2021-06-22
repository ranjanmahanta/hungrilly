import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="ranjan", passwd="1234", database="hungrily")

if mydb:
    print("Connection Successful")

else:
    print("Connection Unsuccessful")

mycursor =mydb.cursor()

def addition(sqlform,data):
    mycursor.execute(sqlform, data)
    mydb.commit()
    print("Data Added Successfully")


def deletion(a):
    mycursor.execute(a)
    mydb.commit()
    print("Data Deleted Successfully")

def view(query):
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

def updation(sql):
    mycursor.execute(sql)
    mydb.commit()
    print("Data Updated Successfully")

print("Welcome,Select your choice")
print("1.Admin")
print("2.Users")
print("3.Vendor")
print("4.Delivery")
y = int(input("Enter your Choice:-"))
if y == 1:
    while True:
        print("1.Addition of Data")
        print("2.Deletion of Data")
        print("3.To view Data")
        print("4.Updation of Data")
        print("5.To Exit")
        x = int(input("Enter your Choice:-"))

        if x == 1:
            sqlform = "Insert into Admin(name,email,password,admin_Contact_num,admin_profile_pic) values(%s,%s,%s,%s,%s)"
            while True:
                a = input("Name-")
                b = input("email-")
                c = input("password-")
                d = input("Contact Number-")
                e = input("Admin profile pic-")
            # c = input()

                data = (a, b, c, d ,e)
                addition(sqlform,data)
                break
        elif x == 2:
            while True:
                code = (input("e-mail-"))
                k = "DELETE from Admin WHERE email=  '{}'".format(code)
                deletion(k)
                break
        elif x == 3:
            while True:
                c = (input("email-"))
                query = "Select * from Admin where email='{}' ".format(c)
                view(query)
                break
        elif x == 4:
            while True:
                f = str(input("Enter email-"))
                g = str(input("Enter new password-"))

                # sql = "update students set roll= 20 where name= '{}'".format(f)
                sql = "update Admin set password= '{}' where email= '{}'".format(g, f)
                updation(sql)
                break
        elif x == 5:
            print("Bye Bye")
            exit(0)

        else:
            print("Wrong Choice")
            exit(0)

if y == 2:
    while True:
        print("1.Addition of User-Data")
        print("2.Deletion of User-Data")
        print("3.To view User-Data")
        print("4.Updation of User-Data")
        print("5.To Exit")
        x = int(input("Enter your Choice:-"))

        if x == 1:
            sqlform = "Insert into Users(name,email,password,user_address,user_contact_num,user_profilepic) values(%s,%s,%s,%s,%s,%s)"
            while True:
                a = input("Name-")
                b = input("email-")
                c = input("password-")
                d = input("Address-")
                e = input("Contact Number-")
                f = input("Users profile pic-")


                data = (a, b, c, d ,e,f)
                addition(sqlform,data)
                break

        elif x == 2:
            while True:
                code = (input("e-mail-"))
                k = "DELETE from Users WHERE email=  '{}'".format(code)
                deletion(k)
                break
        elif x == 3:
            while True:
                c = (input("email-"))
                query = "Select * from Users where email='{}' ".format(c)
                view(query)
                break
        elif x == 4:
            while True:
                f = str(input("Enter email-"))
                g = str(input("Enter new password-"))

                # sql = "update students set roll= 20 where name= '{}'".format(f)
                sql = "update Users set password= '{}' where email= '{}'".format(g, f)
                updation(sql)
                break
        elif x == 5:
            print("Bye Bye")
            exit(0)

        else:
            print("Wrong Choice")
            exit(0)

if y == 3:
    while True:
        print("1.Addition of Vendor-Data")
        print("2.Deletion of Vendor-Data")
        print("3.To view Vendor-Data")
        print("4.Updation of Vendor-Data")
        print("5.To Exit")
        x = int(input("Enter your Choice:-"))

        if x == 1:
            sqlform = "Insert into Vendor(name,email,password,vendor_contact_num,vendor_profilepic) values(%s,%s,%s,%s,%s)"
            while True:
                a = input("Name-")
                b = input("email-")
                c = input("password-")
                d = input("Contact Number-")
                e = input("Vendor profile pic-")

                data = (a, b, c, d ,e)
                addition(sqlform,data)
                break

        elif x == 2:
            while True:
                code = (input("e-mail-"))
                k = "DELETE from Vendor WHERE email=  '{}'".format(code)
                deletion(k)
                break
        elif x == 3:
            while True:
                c = (input("email-"))
                query = "Select * from Vendor where email='{}' ".format(c)
                view(query)
                break
        elif x == 4:
            while True:
                f = str(input("Enter email-"))
                g = str(input("Enter new password-"))

                # sql = "update students set roll= 20 where name= '{}'".format(f)
                sql = "update Vendor set password= '{}' where email= '{}'".format(g, f)
                updation(sql)
                break
        elif x == 5:
            print("Bye Bye")
            break

        else:
            print("Wrong Choice")
            exit(0)

if y == 4:
    while True:
        print("1.Addition of Delivery-Data")
        print("2.Deletion of Delivery-Data")
        print("3.To view Delivery-Data")
        print("4.Updation of Delivery-Data")
        print("5.To Exit")
        x = int(input("Enter your Choice:-"))

        if x == 1:
            sqlform = "Insert into Delivery(name,email,password,delivery_range,delivery_contact_num,delivery_profile_pic) values(%s,%s,%s,%s,%s,%s)"
            while True:
                a = input("Name-")
                b = input("email-")
                c = input("password-")
                d = input("Delivery Range-")
                e = input("Contact Number-")
                f = input("Delivery profile pic-")

                data = (a, b, c, d, e, f)
                addition(sqlform, data)
                break

        elif x == 2:
            while True:
                code = (input("e-mail-"))
                k = "DELETE from Delivery WHERE email=  '{}'".format(code)
                deletion(k)
                break
        elif x == 3:
            while True:
                c = (input("email-"))
                query = "Select * from Delivery where email='{}' ".format(c)
                view(query)
                break
        elif x == 4:
            while True:
                f = str(input("Enter email-"))
                g = str(input("Enter new password-"))

                # sql = "update students set roll= 20 where name= '{}'".format(f)
                sql = "update Delivery set password= '{}' where email= '{}'".format(g, f)
                updation(sql)
                break
        elif x == 5:
            print("Bye Bye")
            exit(0)

        else:
            print("Wrong Choice")
            exit(0)