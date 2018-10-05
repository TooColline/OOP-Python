from flask_bcrypt import Bcrypt

class User:

    def __init__(self, data = {}):
        self.user_id = data.get('user_id')
        self.username = data.get('username')
        self.email = data.get('email')
        self.b_crypt = Bcrypt()
        if data.get('password'):
            self.password = self.b_crypt.generate_password_hash(data.get('password')).decode('utf-8')
        
    def save(self):
        pass

class Question:

    def __init__(self, data={}):
        self.user_id = data.get('user_id')
        self.question_id = data.get('question_id')
        self.title = data.get('title')
        self.body = data.get('body')

    def save(self):
        pass

    def query(self):
        pass

class Answer:
    def __init__(self, data={}):
        self.user_id = data.get('user_id')
        self.answer_id = data.get('answer_id')
        self.question_id = data.get('question_id')
        self.answer_body = data.get('answer_body')
        self.accepted = data.get('accepted', False)

    def save(self):
        pass

class Comment:
    def __init__(self, data={}):
        self.answer_id = data.get('answer_id')
        self.question_id = data.get('question_id')
        self.comment_body = data.get('comment_body')

    def save(self):
        pass
