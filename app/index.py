#!/usr/bin/python
#!coding:utf-8
from flask import Flask,render_template,url_for,request,redirect,make_response,session
import os
from redis_db import *
import commands
app = Flask(__name__)
app.secret_key='passwd'
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('user')
	pawd = request.form.get('pawd')
        r.set(username,pawd)
        return render_template('hi.html',name=username)
    else:
	return render_template('reg.html')
@app.route('/shell',methods=['GET','POST'])
def sysshell():
    if request.method == 'POST':
        shell = request.form.get('shell')
	(statu,output) = commands.getstatusoutput(shell)
	if statu == '0':
            statu = 'NO'
	else:
	    statu = 'YES'
        return render_template('rec.html',statu=statu,output=output)
    else:
	return render_template('shell.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=88)
