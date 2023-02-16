from flask import Flask,render_template,request

app=Flask(__name__)

lis=[]
@app.route("/")
def ecommerce():
    lis.append(stu)
    lis.append(stu1)
    lis.append(stu2)
    return render_template("index.html",data=lis)


class student:
    def __init__(self, name, age,purchased,amount):
        self.name=name
        self.age=age
        self.purchased=purchased
        self.amount=amount

    def mark(self):
        return self.name,self.age,self.purchased,self.amount


@app.route("/create",methods=['get','post'])
def create_object():
    if request.method == "POST":
        name=request.form.get("name")
        age=request.form.get("age")
        purchased=request.form.get("purchased")
        amount=request.form.get("amount")
        obj=student(name,age,purchased,amount)
        lis.append(obj)
    return render_template("create.html",data=lis)
        
    
stu=student("pradeep",20,"watch",2500)
stu1=student("sakthi",40,"apple",500)
stu2=student("siva",29,"headset",300)



if __name__=="__main__":
    app.run(debug=True)