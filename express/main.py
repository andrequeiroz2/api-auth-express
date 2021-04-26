from flask import Blueprint, render_template, request, flash, redirect, url_for
from express.host.form import HostForm
from express.host.controller import create_host, num_host, update_host


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/host', methods=['GET', 'POST'])
def host():
    form = HostForm()
    if form.validate_on_submit():
        num = num_host()
        if num:
            print('cria um host')
            create_host(hostname=form.hostname.data)
            flash('Host has benn created', 'success')
            return redirect(url_for("main.host"))
        else:
            print('faz update')
            update_host(hostname=form.hostname.data)
            flash('Host has benn updated', 'success')
            return redirect(url_for("main.host"))

    return render_template('host.html', form=form)
