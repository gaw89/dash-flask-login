from dash import dcc, html
from dash.dash import Dash
import pandas as pd
import plotly.express as px
from flask import Flask, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dash_flask_login import FlaskLoginAuth

server = Flask(__name__)
server.secret_key = "super secret string"

login_manager = LoginManager()
login_manager.init_app(server)

# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@server.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@server.route('/logout')
def logout():
    logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


app = Dash(name='app1', url_base_pathname='/app1/', server=server)
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

auth = FlaskLoginAuth(app)


if __name__ == '__main__':
    server.run_server(debug=True)
