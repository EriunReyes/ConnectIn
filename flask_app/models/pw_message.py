from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math


db = 'connection_db'
class PrivateW_message:
    # db = 'login_registration_db'
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.sender = data['sender']
        self.sender_id = data['sender_id']
        self.receiver = data['receiver']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f'{delta.days} day ago'
        elif delta.total_seconds() >=60:
            return f'{math.floor(delta.total_seconds() / 60)} minutes ago'
        else:
            return f'{math.floor(delta.total_seconds())} seconds ago'


    @classmethod  #This method helps to save our information to the db
    def save(cls, data):
        query = 'INSERT INTO messages (content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s);'
        return connectToMySQL(db).query_db(query, data)



    @classmethod #This method helps to get one specific id from the db
    def get_one(cls, data):
        query = 'SELECT * FROM messages WHERE id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    # @classmethod # This method helps to get all from our table
    # def get_all(cls):
    #     query = 'SELECT * FROM messages';
    #     result = connectToMySQL(db).query_db(query)
    #     results = []
    #     for row in result:
    #         results.append(cls(row))

    @classmethod #This method helps to delete a specifiv row from our table
    def destroy(cls, data):
        query = 'DELETE FROM messages WHERE messages.id = %(id)s;'
        return connectToMySQL(db).query_db(query, data)

    @classmethod #This method helps to get the messages from the user
    def get_user_messages(cls, data):
        query = 'SELECT users.first_name AS sender, users2.first_name AS receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id = %(id)s;'
        messages = []
        results = connectToMySQL(db).query_db(query, data)
        for message in results:
            messages.append(cls(message))
        return messages
        

