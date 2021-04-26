import ast
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash
)
import requests
from requests.models import ConnectionError, InvalidURL
from express.host.controller import get_host, host


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    if get_host():
        return redirect(url_for("main.host"))
    return render_template('login.html')

@auth.route('/signup')
def signup():
    if get_host():
        return redirect(url_for("main.host"))
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    if get_host():
        return redirect(url_for("main.host"))
    return 'Logout'

@auth.route('/token')
def token():
    if get_host():
        return redirect(url_for("main.host"))
    return render_template('token.html')

@auth.route('/update/password')
def password():
    if get_host():
        return redirect(url_for("main.host"))
    return render_template('update_password.html')

@auth.route('/delete/user')
def delete():
    if get_host():
        return redirect(url_for("main.host"))
    return render_template('delete.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    try:
        _host = host()
        host_name = _host.name

        email = request.form.get('email')
        password = request.form.get('password')

        param = {
            "email":email,
            "passw":password
        }
    
        response = requests.post(
            host_name+'/api/users/auth/signup',
            json=param,
            verify=False
        )
        
        dict_tag = response.content.decode("UTF-8")
        resp = ast.literal_eval(dict_tag)
        status_code = response.status_code

        if status_code > 399:
            inf = resp['inf']
            flash("Error: "+str(status_code)+", "+inf, "error")
            return redirect(url_for('auth.signup'))

        _email= resp['data'][0]['email']
        uid = resp['data'][0]['uid']
    
        return render_template('signup_details.html', email=_email,uid=uid)
    except ConnectionError:
        flash("Error: Connection refused, verify your host", "error")           
        return redirect(url_for('auth.signup'))
    except InvalidURL:
        flash("Error: Invalid host, verify your host", "error")           
        return redirect(url_for('auth.signup'))
   
 
@auth.route('/login', methods=['POST'])
def login_post():
    try:
        _host = host()
        host_name = _host.name

        email = request.form.get('email')
        password = request.form.get('password')
        
        param = {
            "email":email,
            "passw":password
        }

        response = requests.post(
            host_name+'/api/users/auth/login',
            json=param,
            verify=False
        )
    
        dict_tag = response.content.decode("UTF-8")
        resp = ast.literal_eval(dict_tag)
        status_code = response.status_code
        

        if status_code > 399:
            inf = resp['inf']
            flash("Error: "+str(status_code)+", "+inf, "error")
            return redirect(url_for('auth.login'))
    
        email= resp['data'][0]['email']
        uid = resp['data'][0]['uid']
        token = resp['data'][0]['token']

        return render_template('profile_detail.html', email=email, uid=uid, token=token)
    except ConnectionError as e:
        flash("Error: Connection refused, verify your host", "error")           
        return redirect(url_for('auth.login'))
    except InvalidURL:
        flash("Error: Invalid host, verify your host", "error")           
        return redirect(url_for('auth.login'))


@auth.route('/token', methods=['POST'])
def token_post():
    try:    
        _host = host()
        host_name = _host.name

        email = request.form.get('email')
        password = request.form.get('password')
    
        param = {
            "email":email,
            "passw":password
        }

        response = requests.post(
            host_name+'/api/users/auth/token',
            json=param,
            verify=False
        )
    
        dict_tag = response.content.decode("UTF-8")
        resp = ast.literal_eval(dict_tag)
        status_code = response.status_code

        if status_code > 399:
            inf = resp['inf']
            flash("Error: "+str(status_code)+", "+inf, "error")
            return redirect(url_for('auth.token'))
    
        token = resp['data'][0]['token']
        refresh = resp['data'][0]['refreshToken']
        expires = resp['data'][0]['expiresIn']
    
        return render_template("token_detail.html", token=token, refresh=refresh, expires=expires)
    except ConnectionError as e:
        flash("Error: Connection refused, verify your host", "error")           
        return redirect(url_for('auth.token'))
    except InvalidURL:
        flash("Error: Invalid host, verify your host", "error")           
        return redirect(url_for('auth.token'))



@auth.route('/update/password', methods=['POST'])
def update_password():
    try:
        _host = host()
        host_name = _host.name

        email = request.form.get('email')
        password = request.form.get('password')
        password_new = request.form.get('password_new')

        param = {
            "email":email,
            "passw":password,
            "passw_new":password_new
        }

        response = requests.put(
            host_name+'/api/users/auth',
            json=param,
            verify=False
        )

        dict_tag = response.content.decode("UTF-8")
        resp = ast.literal_eval(dict_tag)
        status_code = response.status_code
    
        if status_code > 399:
            inf = resp['inf']
            flash("Error: "+str(status_code)+", "+inf, "error")
            return redirect(url_for('auth.update_password'))
    
        flash("Success: Password updated", 'success')
        return redirect(url_for('auth.login'))
    
    except ConnectionError as e:
        flash("Error: Connection refused, verify your host", "error")           
        return redirect(url_for('auth.update_password'))
    except InvalidURL:
        flash("Error: Invalid host, verify your host", "error")           
        return redirect(url_for('auth.update_password'))


@auth.route('/delete/user', methods=['POST'])
def delete_user():
    try:
        _host = host()
        host_name = _host.name

        email = request.form.get('email')
        password = request.form.get('password')
    
        param = {
            "email":email,
            "passw":password,
        }

        response = requests.delete(
            host_name+'/api/users/auth',
            json=param,
            verify=False
        )

        dict_tag = response.content.decode("UTF-8")
        resp = ast.literal_eval(dict_tag)
        status_code = response.status_code

        if status_code > 399:
            inf = resp['inf']
            flash("Error: "+str(status_code)+", "+inf, "error")
            return redirect(url_for('auth.delete_user'))
    
        flash("Success: User deleted", 'success')
        return redirect(url_for('auth.login'))

    except ConnectionError as e:
        flash("Error: Connection refused, verify your host", "error")           
        return redirect(url_for('auth.delete_user'))
    except InvalidURL:
        flash("Error: Invalid host, verify your host", "error")           
        return redirect(url_for('auth.delete_user'))
