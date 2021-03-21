from flask import Flask,render_template,request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():
    title = "Subscribe to my email news letter"
    return render_template("subscribe.html",title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    
    # message = "You have been subscribed to my email newsltter"
    # email_server = smtplib.SMTP("smtp.gmail.com",587)
    # email_server.starttls()
    # email_server.login("wmr121@gmail.com","")
    # email_server.sendmail("wmr121@gmail.com",email,message)
    if not first_name or not last_name or not email:
        error_statement = "All form fields are required"
        return render_template("subscribe.html",error_statement=error_statement,
                               first_name=first_name,last_name=last_name,email=email)
    title = "Thank you"
    return render_template("form.html",title=title,first_name=first_name,last_name=last_name,email=email)