from code import interact
from pyexpat import features
import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pymysql
from datetime import date
from django.core.files.storage import FileSystemStorage
#from torch import qr

#from sqlalchemy import engine_from_config
# Create your views here.
con=pymysql.connect(host="localhost",user="root",password="",database="db_expert")
c=con.cursor()
def mainhome(request):
    s="select cusId from subscription where expDate<(select sysdate())"
    c.execute(s)
    data=c.fetchall()
    print(data)
    for d in data:
        s="update subscription set status='Expired' where cusId='"+str(d[0])+"'"
        c.execute(s)
        con.commit()
    return render(request,"mainhome.html")
def login(request):
    if request.POST :
       uname=request.POST.get("t1") 
       passw=request.POST.get("t2") 
       qry="select usertype from login where username='"+str(uname)+"' and password='"+str(passw)+"'"
       c.execute(qry)
       data=c.fetchall()
       request.session["uname"]=uname
       if(data[0][0]=="admin"):
           return HttpResponseRedirect("/adminhome")
       elif(data[0][0]=="Cust"):
           return HttpResponseRedirect("/cushome")
       elif(data[0][0]=="Expert"):
           return HttpResponseRedirect("/experthome") 
       else:
           msg="invalid username or password"


    return render(request,"login.html")
def cusreg(request):
    msg=""
    if request.POST :
        name=request.POST.get("t3")
        lname=request.POST.get("txtLname")
        email=request.POST.get("t4")
        mob=request.POST.get("t5")
        uname=request.POST.get("t1")
        passw=request.POST.get("t2")
        house=request.POST.get("house")
        place=request.POST.get("place")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        qry="insert into login (`username`,`password`,`usertype`) values('"+str(uname)+"','"+str(passw)+"','Cust')"
        
        qry1="insert into custreg(`name`,`email`,`mob`,`username`,`house`,`place`,`district`,`state`,`pin`,`lname`,`regDate`) values('"+str(name)+"','"+str(email)+"','"+str(mob)+"','"+str(uname)+"','"+str(house)+"','"+str(place)+"','"+str(district)+"','"+str(state)+"','"+str(pin)+"','"+str(lname)+"',(select sysdate()))"
        try:
            c.execute(qry1)
        except:
            msg="Registration failed"
        else:
            try:
                c.execute(qry)
            except:
                msg="Sorry some error occured"
            else:
                msg="Registration successfull"
        con.commit()
        return HttpResponseRedirect("login/")
    return render(request,"cusreg.html",{"msg":msg})
def expertreg(request):
    if request.POST :
        name=request.POST.get("t3")
        email=request.POST.get("t4")
        mob=request.POST.get("t5")
        exp=request.POST.get("t6")
        area=request.POST.get("t7")
        uname=request.POST.get("t1")
        passw=request.POST.get("t2")
        qry="insert into login (`username`,`password`,`usertype`) values('"+str(uname)+"','"+str(passw)+"','Expert')"
        c.execute(qry)
        qry1="insert into expert(`name`,`email`,`mob`,`username`,`area`,`exp`,`regDate`) values('"+str(name)+"','"+str(email)+"','"+str(mob)+"','"+str(uname)+"','"+str(exp)+"','"+str(area)+"',(select sysdate()))"
        c.execute(qry1)
        con.commit()
    return render(request,"expertreg.html")

def addvehicle(request):
    qry1="select * from company"
    c.execute(qry1)
    data=c.fetchall()

    if request.POST :
        name=request.POST.get("t1")
        cid=request.POST.get("t2")
        model=request.POST.get("t3")
        type=request.POST.get("t4")
        fuel=request.POST.get("t5")
        torque=request.POST.get("t6")
        hp=request.POST.get("t7")
        colors=request.POST.get("t8")
        price=request.POST.get("t9")
        ground=request.POST.get("t10")
        tyre=request.POST.get("t11")
        img=request.POST.get("t12")
        myfile=request.FILES.get("t12")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        qry="insert into vehicle (`name`,`cmpid`,`model`,`type`,`fuel`,`torque`,`hp`,`colors`,`price`,`groundclearence`,`tyrsize`,`image`,`regDate`) values('"+str(name)+"','"+str(cid)+"','"+str(model)+"','"+str(type)+"','"+str(fuel)+"','"+str(torque)+"','"+str(hp)+"','"+str(colors)+"','"+str(price)+"','"+str(ground)+"','"+str(tyre)+"','"+str(uploaded_file_url)+"',(select sysdate()))"
        c.execute(qry)
        con.commit()
    return render(request,"vehicle.html",{"data":data})

def company(request):
    msg=""
    if request.POST :
        name=request.POST.get("t1")
        myfile=request.FILES.get("file")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        qry="insert into company (`name`,`logo`) values('"+str(name)+"','"+str(uploaded_file_url)+"')"
        try:
            c.execute(qry)
        except:
            msg="Sorry some error occured"
        else:
            msg="Company added"
        con.commit()
    qry="select * from company"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"company.html",{"msg":msg,"data":data})
def adminviewcus(request):
    qry="select * from custreg"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminviewcus.html",{"data":data})
def adminviewexpert(request):
    qry="select * from expert"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminviewexpert.html",{"data":data})
def adminviewvehicle(request):
    qry="select * from vehicle"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminviewvehicle.html",{"data":data})
def adminreview(request):
    qry="select expertreview.*,expert.name,vehicle.name from expertreview,expert,vehicle where expertreview.status='submitted' and expertreview.exp_id=expert.id and expertreview.vid=vehicle.id"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminreview.html",{"data":data})
def adminreviewmore(request):
    rid=request.GET.get('id')
    qry=f"select * from reviewchild where reviewid='{rid}'"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminreviewmore.html",{"data":data,"rid":rid})
def adminupdatereview(request):
    rid=request.GET.get('id')
    qry=f"update expertreview set status='Approved' where reviewid='{rid}'"
    c.execute(qry)
    con.commit()
    return HttpResponseRedirect("/adminreview")
def adminhome(request):
    return render(request,"adminhome.html")
def deletevehicle(request):
     id=request.GET.get("id")
     qry="update from vehicle where id='"+str(id)+"'"
     c.execute(qry)
     con.commit()
     return HttpResponseRedirect("/adminviewvehicle")
def expertviewvehicle(request):
    qry="select * from vehicle"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"expertviewvehicle.html",{"data":data})
def expcardetails(request):
    cid=request.GET.get("id")
    qry="select * from vehicle where id='"+cid+"'"
    c.execute(qry)
    car=c.fetchall()
    return render(request,"expcardetails.html",{"car":car})
def expertreview(request):
    msg=""
    vid=request.GET.get("id")
    uname=request.session["uname"]
    qry="select id from expert where username='"+str(uname)+"'"
    print(qry)
    c.execute(qry)
    data=c.fetchall()
    id=data[0][0]
    qry="select count(*) from expertreview where vid='"+str(vid)+"' and exp_id='"+str(id)+"'"
    c.execute(qry)
    d=c.fetchone()
    if d[0]>0:
        msg="Review already added"
    else:
        qry="select * from questions"
        c.execute(qry)
        datas=c.fetchall()
    if request.POST :
            buy=request.POST.get("txtBuy")
            avoid=request.POST.get("txtAvoid")
            review=request.POST.get("txtOverall")
            rating=request.POST.get("rating")

            
            qry1="insert into expertreview (`review`,`rating`,`exp_id`,`date`,`vid`,`why_buy`,`why_avoid`,`status`) values('"+str(review)+"','"+str(rating)+"','"+str(id)+"',(select sysdate()),'"+str(vid)+"','"+buy+"','"+avoid+"','submitted')"
            c.execute(qry1)
            con.commit()
            qry="select max(reviewid) from expertreview"
            c.execute(qry)
            d=c.fetchone()
            reviewid=d[0]
            s="select * from questions"
            c.execute(s)
            questions=c.fetchall()
            for i in questions:
                nm="point"+str(i[0])
                val=request.POST[nm]
                nm="ans"+str(i[0])
                ans=request.POST[nm]
                s="insert into reviewchild(reviewid,question,answer,rating) values('"+str(reviewid)+"','"+i[1]+"','"+ans+"','"+str(val)+"')"
                c.execute(s)
                con.commit()
            msg="Review added"

    return render(request,"expertreview.html",{"msg":msg,"datas":datas})
def experthome(request):
    return render(request,"experthome.html")
def expertviewreviews(request):
    uname=request.session["uname"]
    qry="select ev.reviewid,ev.review,ev.rating,ex.name,ex.mob,ex.email,vh.id,vh.name from expertreview ev join expert ex on(ev.exp_id=ex.id) join vehicle vh on(vh.id=ev.vid) where ex.username='"+str(uname)+"'"

    c.execute(qry)
    data=c.fetchall()
    return render(request,"expertviewreviews.html",{"data":data})
def custviewvehicle(request):
    qry="select * from vehicle"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"custviewvehicle.html",{"data":data})
def serachcustviewvehicle(request):
    if request.POST :
        name=request.POST.get("t1")
        qry="select * from vehicle where name like '%"+str(name)+"%'"
        c.execute(qry)
        data=c.fetchall()
        return render(request,"searchcustviewvehicle.html",{"data":data})
    return render(request,"searchcustviewvehicle.html")

def cusviewreviews(request):
    
    qry="select ev.reviewid,ev.review,ev.rating,ex.name,ex.mob,ex.email,vh.id,vh.name from expertreview ev join expert ex on(ev.exp_id=ex.id) join vehicle vh on(vh.id=ev.vid) where ev.status='Approved'"

    c.execute(qry)
    data=c.fetchall()
    return render(request,"cusviewviewreviews.html",{"data":data})
def cushome(request):
    return render(request,"cushome.html")
def custcardetails(request):
    cid=request.GET.get("id")
    qry="select * from vehicle where id='"+cid+"'"
    c.execute(qry)
    car=c.fetchall()
    uname=request.session["uname"]
    qry=f"select count(*) from subscription where cusId in(select id from custreg where username ='{uname}')"
    print(qry)
    c.execute(qry)
    d=c.fetchone()
    print(d[0])
    status=""
    if int(d[0])>0:
        qry=f"select status from subscription where cusId in(select id from custreg where username ='{uname}')"
        print(qry)
        c.execute(qry)
        d=c.fetchone()
        status=d[0]
    else:
        qry=f"select status from subscription where cusId in(select id from custreg where email ='{uname}')"
        c.execute(qry)
        d=c.fetchone()
        status=d[0]
    count=0
    qry="select count(*)  from reviewchild where reviewid in(select reviewid from expertreview where vid='"+str(cid)+"')"
    c.execute(qry)
    d=c.fetchone()
    count=d[0]
    score=0
    engine=""
    ride=""
    interior=""
    feature=""
    if count>0:
        score=generate_data(cid)

        

        qry="select avg(rating) from reviewchild where question='Engine and performance' and reviewid in(select reviewid from expertreview where vid='"+cid+"')"
        c.execute(qry)
        d=c.fetchone()
        engine=d[0]
        qry="select avg(rating) from reviewchild where question='Ride and handling' and reviewid in(select reviewid from expertreview where vid='"+cid+"')"
        c.execute(qry)
        d=c.fetchone()
        ride=d[0]
        qry="select avg(rating) from reviewchild where question='Interior space and comfort' and reviewid in(select reviewid from expertreview where vid='"+cid+"')"
        c.execute(qry)
        d=c.fetchone()
        interior=d[0]
        qry="select avg(rating) from reviewchild where question='Features and equipment' and reviewid in(select reviewid from expertreview where vid='"+cid+"')"
        c.execute(qry)
        d=c.fetchone()
        feature=d[0]

    return render(request,"custcardetails.html",{"car":car,"score":score,"engine":engine,"ride":ride,"interior":interior,"feature":feature,"count":count,"status":status})

def generate_data(vid):
    import pymysql
    import csv
    import sys

    db_opts = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'db_expert'
    }

    db = pymysql.connect(**db_opts)
    cur = db.cursor()

    sql = "SELECT review from expertreview where vid='"+str(vid)+"' and status='Approved'"
    csv_file_path = 'expertreviewapp/static/data/dataset.csv'

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        db.close()
# Continue only if there are rows returned.
    if rows:
    # New empty list called 'result'. This will be written to a file.
        result = list()

    # The row name is the first entry for each entity in the description tuple.
        column_names = list()
        for i in cur.description:
            column_names.append(i[0])

        result.append(column_names)
        for row in rows:
            result.append(row)

    # Write result to file.
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
    else:
        sys.exit("No rows found for query: {}".format(sql))
    score=analyse()
    return score

def analyse():
    import csv
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import pandas as pd
    import re
    analyser = SentimentIntensityAnalyzer()
    # print(analyser)
    def print_sentiment_scores():
        lst=[]
        dataset = pd.read_csv('expertreviewapp/static/data/dataset.csv', delimiter = ',')
        f=open('expertreviewapp/static/data/dataset.csv')
        reader=csv.reader(f)
        lines=len(list(reader))
        print(lines)
        corpus = []
        corpusn = []
        print("dataset")
        
    
        cnt=0
        cntn=0
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        pos=0
        neg=0
        neu=0
    
        for i in range(0,lines-1):  
            review = re.sub('[^a-zA-Z0-1]', ' ', dataset['review'][i])
            
            cor=0
           
            vadersenti = analyser.polarity_scores(review)
            if vadersenti["compound"] >= 0.5:
                    pos=pos+1
            elif vadersenti["compound"] <= -0.5:
                    neg=neg+1
            else:
                    neu=neu+1
            
            print(i)
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(vadersenti)
            cnt=cnt+vadersenti['pos']
            cntn=cntn+vadersenti['neg']
            corpus.append(cnt)
            corpusn.append(cntn)
            
        print("Scores")
        print("************************")
        print("Pos=",pos)
        print("Neg=",neg)
        print("Neu=",neu)
        print("************************")
        corpus.append(cnt)
        corpusn.append(cntn)

        lst.append(corpus)
        lst.append(corpusn)
        print(lst)
        return(lst)

        
    
    score=print_sentiment_scores()
    return score
def adminreport(request):
    customer=""
    expert=""
    vehicle=""
    review=""
    if request.POST:
        type=request.POST['type']
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        if type=="Customer":
            qry=f"select * from custreg where regDate between '{sdate}' and '{edate}'"
            print(qry)
            c.execute(qry)
            customer=c.fetchall()
        if type=="Expert":
            qry=f"select * from expert where regDate between '{sdate}' and '{edate}'"
            c.execute(qry)
            expert=c.fetchall()
        if type=="Vehicle":
            qry=f"select * from vehicle where regDate between '{sdate}' and '{edate}'"
            c.execute(qry)
            vehicle=c.fetchall()
        if type=="Review":
            qry=f"select expertreview.*,expert.name,vehicle.name from expertreview,expert,vehicle where expertreview.status='Approved' and expertreview.exp_id=expert.id and expertreview.vid=vehicle.id and expertreview.date between '{sdate}' and '{edate}'"
            c.execute(qry)
            review=c.fetchall()
    return render(request,"adminreport.html",{"customer":customer,"expert":expert,"vehicle":vehicle,"review":review})

def expertprofile(request):
    uname=request.session["uname"]
    if request.POST :
        name=request.POST.get("t3")
        email=request.POST.get("t4")
        mob=request.POST.get("t5")
        exp=request.POST.get("t6")
        area=request.POST.get("t7")
        qry1="update expert set `name`='"+str(name)+"',`email`='"+str(email)+"',`mob`='"+str(mob)+"',`area`='"+str(exp)+"',`exp`='"+str(area)+"' where username='"+str(uname)+"'"
        print(qry1)
        c.execute(qry1)
        con.commit()
    qry=f"select * from expert where username='{uname}'"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"expertprofile.html",{"data":data})

def cusprofile(request):
    msg=""
    uname=request.session["uname"]
    if request.POST :
        name=request.POST.get("t3")
        lname=request.POST.get("txtLname")
        email=request.POST.get("t4")
        mob=request.POST.get("t5")
       
        house=request.POST.get("house")
        place=request.POST.get("place")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        qry1="update custreg set `name`='"+str(name)+"',`email`='"+str(email)+"',`mob`='"+str(mob)+"',`house`='"+str(house)+"',`place`='"+str(place)+"',`district`='"+str(district)+"',`state`='"+str(state)+"',`pin`='"+str(pin)+"',`lname`='"+str(lname)+"' where username='"+uname+"'"
        try:
            c.execute(qry1)
        except:
            msg="Sorry som error occured"
        else:
            msg="Updation successfull"
        con.commit()
    qry=f"select * from custreg where username='{uname}'"
    print(qry)
    c.execute(qry)
    data=c.fetchall()
    return render(request,"cusprofile.html",{"msg":msg,"data":data})

def adminplan(request):
    msg=""
    if request.POST:
        plan=request.POST['plan']
        duration=request.POST['duration']
        rate=request.POST['rate']
        qry=f"insert into plan(planName,duration,rate,status) values('{plan}','{duration}','{rate}','1')"
        c.execute(qry)
        con.commit()
    qry=f"select * from plan where status='1'"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"adminplan.html",{"msg":msg,"data":data})

def commonplan(request):
    qry=f"select * from plan where status='1'"
    c.execute(qry)
    data=c.fetchall()
    return render(request,"commonplan.html",{"data":data})

def planselect(request):
    planid=request.GET.get("id")
    amt=request.GET.get("amt")
    uname=request.session["uname"]
    qry="Select id from custreg where username='"+uname+"'"
    print(qry)
    c.execute(qry)
    d=c.fetchone()
    rid=d[0]
    qry=f"select duration from plan where planId='{planid}'"
    c.execute(qry)
    d=c.fetchone()
    duration=int(d[0])*30
    qry=f"insert into subscription(planId,cusId,subDate,expDate,status) values('{planid}','{rid}',(select sysdate()),(SELECT DATE_ADD((select sysdate()), INTERVAL '{duration}' DAY)),'Active')"
    c.execute(qry)
    con.commit()
    return HttpResponseRedirect("/payment?amt="+str(amt))

def payment(request):
    amt=request.GET.get("amt")
    if request.POST:
        return HttpResponseRedirect("/cussubscription")
    return render(request,"payment.html",{"amt":amt})

def cussubscription(request):
    uname=request.session["uname"]
    qry="select subscription.subId,plan.planName,plan.duration,plan.rate,subscription.subDate,subscription.expDate,subscription.status from subscription,plan where subscription.planId=plan.planId and subscription.cusId in (select id from custreg where username='"+uname+"')"
    c.execute(qry)
    print(qry)
    data=c.fetchall()
    return render(request,"cussubscription.html",{"data":data})