#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from flask_script import Manager, Shell

from example.app import app

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app}


manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
