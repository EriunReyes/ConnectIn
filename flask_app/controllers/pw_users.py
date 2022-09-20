from flask_app import app 
from flask import render_template, request, session, redirect, flash
from flask_app.models.pw_user import PrivateW_user
from flask_app.models.pw_message import PrivateW_message
import requests, os


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

#REGISTRATION
@app.route('/register_user', methods=['POST'])
def register_user():
    # pw_hash = bcrypt.generate_password_hash(request.form['password']) #assigning the hash method to hash our password
    # print(pw_hash)
    if not PrivateW_user.validate_user(request.form): # If validation goes wrong it will redirect to the main page
        return redirect('/')
    data = {                                        #Here we request all our information from our form with the name attribute.
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email':  request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])                        #With this.->We're hashing our password.
        }
    user_id = PrivateW_user.save(data) 
    session['user_id'] = user_id 
    return redirect('/connections') #

# LOGIN
@app.route('/loginn')
def login_template():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    user_in_db = PrivateW_user.get_by_email(request.form)
    # if user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password",'login')
        return redirect("/loginn")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/loginn')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    return redirect('/connections')



#DASHBOARD
@app.route('/dashboard') 
def dashboard():
    if 'user_id' not in session: 
        return redirect('/') 
    data = {
        'id': session['user_id']
    }
    user = PrivateW_user.get_one(data) 
    messages = PrivateW_message.get_user_messages(data)
    users = PrivateW_user.get_all()
    return render_template('dashboard.html',user = user, messages = messages, users = users ) 



#HOME PAGE
@app.route('/connections') 
def connections():
    if 'user_id' not in session: 
        return redirect('/') 
    data = {
        'id': session['user_id']
    }
    user = PrivateW_user.get_one(data) 
    messages = PrivateW_message.get_user_messages(data)
    users = PrivateW_user.get_all()
    return render_template('connections.html',user = user, messages = messages, users = users ) 



#POST
@app.route('/post')
def post():
    if 'user_id' not in session: 
        return redirect('/') 
    data = {
        'id': session['user_id']
    }
    user = PrivateW_user.get_one(data) 
    messages = PrivateW_message.get_user_messages(data)
    users = PrivateW_user.get_all()
    return render_template("profile.html", user = user, messages = messages, users = users)



#COMMUNITY
@app.route('/community')
def community():
    all_users = PrivateW_user.get_all()
    return render_template("community.html", all_users = all_users)

@app.route('/user/new')
def new():
    if 'user_id' not in session: 
        return redirect('/') 
    data = {
        'id': session['user_id']
    }
    # user = PrivateW_user.get_one(data) 
    return render_template("create.html")

#COMMUNITY-FORM
@app.route('/user/create',methods=['POST'])
def creating():
    print(request.form)
    PrivateW_user.save1(request.form)
    return redirect('/community')



#EDIT
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=PrivateW_user.get_one(data))


#SHOW
@app.route('/user/read_on/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("read_one.html",user=PrivateW_user.get_one(data))



#UPDATE
@app.route('/user/update',methods=['POST'])
def update():
    PrivateW_user.update(request.form)
    return redirect('/community')


# DELETE
@app.route('/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    PrivateW_user.destroy(data)
    return redirect('/community')


#API 
@app.route('/api')
def api():
    return render_template('api.html')


@app.route('/get_user', methods=['POST'])
def api_form():
    headers = os.environ.get("KEY")
    title = request.form['title']
    explanation = request.form['explanation']
    hdurl = request.form['hdurl']
    url = f'https://api.nasa.gov/planetary/apod?api_key={headers}'
    response = requests.get(url)
    print(response.json())
    session['title'] = response.json()['title']
    session['explanation'] = response.json()['explanation']
    session['hdurl'] = response.json()['hdurl']
    return redirect('/api')


#LOGOUT
@app.route('/logout') 
def logout():
    session.clear()
    return redirect('/')