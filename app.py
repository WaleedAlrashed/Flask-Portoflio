from flask import Flask,render_template,request,request,jsonify
import smtplib
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#init db
# db = SQLAlchemy(app)

#create db model
# class Users(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(200),nullable=False)
#     date_created = db.Column(db.DateTime,default=datetime.utcnow)
#     #create fun to return a string when we add new record   

#     def __repr__(self):
#         return '<Name %r>' % self.id

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

@app.route('/users',methods=['POST','GET'])
def users(): 
    title = "Users"
    if request.method == "POST":
        user_name = request.form['name']
        # new_user= Users(name = user_name)
        # commit to db
        try:
            # db.seesion.add(new_user)
            # db.session.commit()
            return redirect('/users')
        except:
            return "Error"
    else:
        return render_template("users.html",title=title)
    
@app.route('/photos',methods=['POST'])
def photos():
    data = request.get_json()
    return data

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
              
              
# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']
    

    # return jsonify('''
    #        The language value is: {}
    #        The framework value is: {}
    #        The Python version is: {}
    #        The item at index 0 in the example list is: {}
    #        The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test))
    return jsonify(
        username="waleed",
        email="wmr1210@hotmail.com",
        id=25
    )