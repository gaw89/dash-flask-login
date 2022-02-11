# Integration of Dash with Flask-Login

### Intro
#### Dash-Flask-Login is a [Dash](https://github.com/plotly/dash) to allow integration with the popular [Flask-Login](https://github.com/maxcountryman/flask-login) for user session management.  

Dash-Admin is intended to be plug and play!  Providing user authentication should be as simple as:

```
auth = FlaskLoginAuth(dash_app)
```

### Documentation

For now, please look at ```usage_dash_flask_login.py``` for an example of using login/logout forms created as separate Dash apps.  Look at ```usage_dash_flask_login_with_default_views.py``` to see an example with the default login/logout forms provided by the package.

### Installation

Dash-Flask-Login can be installed via ```pip install dash-flask-login```.

# WARNING:
## This package is provided without any warranty.  The responsibility of securely storing user data is the sole responsibility of the developer.  The creator of this package will not be held liable for any breach of security while using the package.
