import random
import names
import itertools
from flask import Flask, request, session, render_template, redirect, url_for
from logging import DEBUG

app = Flask(__name__)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.logger.setLevel(DEBUG)
app.secret_key = 'some_secret'

# session['logged_in'] = False


print (names.get_first_name())

def expandeddata(rawdata):
  data = []

  for dept in rawdata:
    data.append(dept)

  data = dict([('marketing',[5, 3]),('sales',[5, 3]), ('accounting', [5, 3]), ('technology', [5, 3]), ('management', [5, 3])])
  glimit = len(data)

  expandeddata = {}

  for k, v in data.items():
    # print (k, v)
    expandeddata[k] = {'data': {}, 'limit': v[1]}
    for number in range(v[0]):
      expandeddata[k]['data'][names.get_first_name()] = random.randrange(100, 1000, 100)
  return expandeddata


def findsubsets(id, iterable, limit):
  sets = itertools.combinations(iterable, limit)
  tup = []
  for item in sets:
    tup.append([id, item])
  return tup

def possibilities(expandeddata):
  possibilities = []
  for dept, deptdata in expandeddata.items():
    possibilities.append((findsubsets(dept, deptdata['data'], deptdata['limit'])))
  return [users for dept in possibilities for users in dept]

def merged_possibilities(possibilities):
  limit = glimit
  possibilities = itertools.chain(possibilities)
  return (findsubsets('GROUP', possibilities, limit ))

def startapp(budget, usabledata):
  expandeddata = expandeddata(usabledata)
  result = []
  groups = merged_possibilities(possibiflities(expandeddata))
  count = 0
  for group in groups:
    if count == 20:
      break
    if sum([expandeddata[grp[0]]['data'][name] for grp in group[1] for name in grp[1]]) <=4000:
      result.append(group)
      count += 1
  return result

@app.route("/")
def index():
  return render_template("index.pug")

@app.route("/selector1", methods=['GET', 'POST'])
def selector1():
  if request.method == 'POST':
    print (request.form)
    session['noofrows'] = request.form['noofrows']
    return redirect(url_for('selector2'))

  return render_template('noofrows.pug')

@app.route("/selector2", methods=['GET', 'POST'])
def selector2():
  if request.method == 'POST':
    print (request.form)
    dept = []
    limit = []
    noofproj =[]
    for item in request.form:
      print (int(item[-1:]))
      if item.startswith('action'):
        continue
      elif item.startswith('limit'):
        limit[int(item[-1:])] = item
      elif item.startswith('dept_name'):
        dept[int(item[-1:])] = item
      elif item.startswith('no_of_projects'):
        noofproj[int(item[-1:])] = item
      else:
        continue
    data = []
    for group in range(1, len(dept)+1):
      data.append([dept[group],(noofproj[group], limit[group])])
    print(data)



  return render_template('baseform.pug', noofrows=int(session['noofrows']))

@app.route("/selector3", methods=['GET', 'POST'])
def selector3():
  if request.method == 'POST':
    print (request.form)
  return render_template('detailsform.pug')

@app.route("/result")
def result():
  pass



if __name__ == "__main__":
  app.run(debug=True)
