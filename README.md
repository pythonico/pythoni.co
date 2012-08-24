pythoni.co
==========

Website for pythoni.co

Up and Running
==============

Make sure you have postgresql properly installed and you have
a database and user called pythonico and you have rights to
work with your pythonico user.

In a python interpreter::

  >> from pythonico import db
  >> db.create_all()

