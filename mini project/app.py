from flask import Flask, render_template, request, url_for
app=Flask(__name__)

app.route("/")
def home():
    return render_template("index.html")

app.route("/login",method=["GET"])
def login():
    Name=request.args.get("Name")
    Age=request.args.get("Age")
    Department=request.args.get("Department")
    if(Name=='praveen' and Age=='18'):
        return render_template("home.html")
    else:
        return "<h2>Your detials are incorrect</h2>"
    
app.route("/details",method=["POST"])
def details():
    Name=request.form("Name")
    Age=request.form("Age")
    Department=request.form("Department")
    if(Name=='praveen' and Age=='18'):
        return render_template("home.html", Name=Name, Age=Age, Department=Department)
    else:
        return "<h2>Your detials are incorrect</h2>"
    
if __name__=="__main__":
    app.run(debug=True)
    

    

