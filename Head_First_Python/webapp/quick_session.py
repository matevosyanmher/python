from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/setuser/<user>')
def set_user(user: str) -> str:
    session['user'] = user
    return "User value set to: " + session['user']


@app.route('/getuser')
def getuser() -> str:
    return "User value currently set to: " + session['user']


if __name__ == '__main__':
    app.run(debug=True)
