from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = ''
mno = ''
ur_role = ''


# Create your views here.
def user_reg(request):
    global fn, ln, em, pwd, mno, ur_role
    if request.method == "POST":
        # To conncet mysql DB
        m = sql.connect(host="localhost", user="root", passwd="Mypassword", database='mysqldb')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "mobile_number":
                mno = value
            if key == "user_role1":
                ur_role = value

        c = "insert into user_details Values('{}','{}','{}','{}','{}','{}')".format(fn, ln, em, pwd, mno, ur_role)
        cursor.execute(c)
        m.commit()

    return render(request, "insuranceapp/register_page.html")


em = ''
pwd = ''


def user_login(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Mypassword", database='mysqldb')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from user_details where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, "insuranceapp/error.html")
        else:
            return render(request, "insuranceapp/welcome.html")

    return render(request, "insuranceapp/login_page.html")
