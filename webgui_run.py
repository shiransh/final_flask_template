#!/usr/bin/env python3
from webserver.models import User
from webserver import app, db, views
from flask.cli import AppGroup

cli_group_db = AppGroup('db')


@cli_group_db.command('init')
def init_db():
    db.create_all()
    # TODO: configure default user here
    db.session.add(User(username="admin", password="123456"))
    db.session.add(User(username="admin1", password="123456"))
    db.session.add(User(username="admin2", password="123456"))
    db.session.commit()


@cli_group_db.command('drop')
def drop_db():
    db.drop_all()


app.cli.add_command(cli_group_db)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
