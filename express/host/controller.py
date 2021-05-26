from express.host.model import Host
from express.database import db


def create_host(hostname):
    host = Host(name=hostname)
    db.session.add(host)
    db.session.commit()


def num_host():
    host = Host.query.all()
    num = len(host)
    if num == 1:
        
        return False
    
    return True


def update_host(hostname):
    Host.query.filter_by(id=1).update(dict(name=hostname))
    db.session.commit()


def get_host():
    host = Host.query.all()
    if not host:
        return True
    else:
        return False


def host():
    host = Host.query.filter_by(id=1).first()
    print(host)
    return host