from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from operator import itemgetter
import csv




app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


def get_data():
    # open data file, filter for in_office,
    # add fullname field
    # then return list of dicts
    with open('./static/data/deathrow.csv', 'r') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['sentence'] == 'Death Sentence':
                newrows.append(row)
        return newrows
    
def inmate_data():
    rows = [d for d in get_data()]
    return (rows)
    
    
    
def filter_data(name='', sortby=None):
    # first, select only peeps that match by a name, then sort them
    rows = [d for d in get_data()]
    if sortby == 'oldest':
        return sorted(rows, key=itemgetter('age'), reverse=True)
    elif sortby == 'youngest':
        return sorted(rows, key=itemgetter('age'))
    else:
        # i.e. 'alpha' or any value...just sort by last name, first name
        return sorted(rows, key=itemgetter('name'))

def get_inmates():
    with open('./static/data/deathrow.csv', 'r') as f:
        names = []
        for row in csv.DictReader(f):
            row['id'] = id
            row['name'] = name
            row['photo'] = photo
        names.append(row)
        return names

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results.html")
def results():
    _sortby =  request.args.get('sortby')
    _lastname =  request.args.get('name')
    peeps = filter_data(name=_lastname, sortby=_sortby)
    html = render_template('results.html', name=_lastname,
                           deathrow=peeps, sortby=_sortby)
    return html

@app.route("/inmate/<id>.html")
def inmate(id):
    peep = get_data()
    html = render_template('inmate.html')
    return html



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)