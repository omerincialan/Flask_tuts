from Corey_v2_package.flask_app import app_, db_




if __name__ == '__main__':
    with app_.app_context():
        db_.create_all()
        app_.run(debug=True)



#    DB CONTEXT
    #with app.app_context():
        #db.create_all()
        #user = User(username="testuserr", email="testtt@example.com", password="password")
        #db.session.add(user)
        #db.session.commit()
        #db.drop_all()


