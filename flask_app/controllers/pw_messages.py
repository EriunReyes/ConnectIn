from flask_app import app
from flask_app.models.pw_user import PrivateW_user
from flask_app.models.pw_message import PrivateW_message
from flask import render_template, redirect, session, flash, request

@app.route('/post_message', methods=['POST']) #Here we create a route with the post method in our form
def post_message(): #Here we create the def 
    if 'user_id' not in session: #Here if user_id is not in session. Redirect back to the first route.
        return redirect('/') 
    
    data = {    #Here we are requesting the information from our models class.
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id'],
        'content': request.form['content']
    }

    PrivateW_message.save(data)  #Here if user_id is in session->Call this method and return to the dashboard
    return redirect('/dashboard')


@app.route('/destroy/message/<int:id>') #Here it's created a route to delete the specific id row from a table
def destroy_message(id):
    data = {   #here we are calling the id from the models
        'id': id 
    }

    PrivateW_message.destroy(data) #Here the destroy function is running and redirecting to the data
    return redirect('/dashboard')
