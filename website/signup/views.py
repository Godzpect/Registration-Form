from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
cr=''
# Create your views here.
def signupaction(request):
    global fn, ln, s, em, pwd, cr
    if request.method == 'POST':
        m=sql.connect(host='localhost',user='root',passwd='pass123', database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="course_name":
                cr=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,cr,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,"signup_page.html")