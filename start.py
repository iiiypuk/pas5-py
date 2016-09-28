#!/usr/bin/env python3

from deps.bottle import TEMPLATE_PATH, static_file, get, route, template, run
import sqlite3

TEMPLATE_PATH.insert(0, './static/tpl/')

@get('/static/<filename:re:.*\.js>')
def javascripts(filename):
  return static_file(filename, root='./static/js')

@get('/static/<filename:re:.*\.(css|less)>')
def stylesheets(filename):
  return static_file(filename, root='./static/css')

# @get('/<filename:re:.*\.(jpg|png|gif|ico)>')
# def images(filename):
#     return static_file(filename, root='static/img')

@get('/static/<filename:re:.*\.ttf>')
def fonts(filename):
    return static_file(filename, root='./static/fonts')

@route('/')
def hello():
  return template('index.tpl')

@get('/pwd/get/<url>')
def get_pwd(url):
  con = sqlite3.connect('./pwd.db')
  con.row_factory = sqlite3.Row
  cur = con.cursor()    
  cur.execute('SELECT url,email,login,pass FROM passwords WHERE url LIKE "%%%s%%"' % url)
  data = cur.fetchall()
  return_data = dict()
  count = 0
  for pass_item in data:
    return_data[count] = {
      'url'   : pass_item['url'],
      'email' : pass_item['email'],
      'login' : pass_item['login'],
      'pass'  : pass_item['pass'],
      # 'desc'  : pass_item['desc']
    }

    count += 1

  con.close()

  return return_data

run(host='localhost', port=5153, debug=True)
