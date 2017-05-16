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
    
def get_inmatedata(id):
    with open('./static/data/deathrow.csv', 'r') as f:
        rows = [d for d in get_data()]
        for row in csv.DictReader(f):
            if id == str( row["id"] ):
            # decode handles accented characters
                name = row["name"] 
                race = row["race"]
                photo = row["photo"] 
                sex = row["sex"]
                age = row["age"]
                years_there = row["years_there"]
                location_held = row["location_held"]
                sentence = row["sentence"]
                crime = row["crime"]
                offense_date = row["offense_date"]
                sentence_date = row["sentence_date"]
                county = row["county"]
                resentence= row["resentence"]
        return id, name, race, photo, sex, age, years_there, location_held, sentence, crime, offense_date, sentence_date, county, resentence
    
    
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
    id, name, race, photo, sex, age, years_there, location_held, sentence, crime, offense_date, sentence_date, county, resentence = get_inmatedata(id)
    return render_template('inmate.html', pairs=name, name=name, race=race, photo=photo, sex=sex, age=age, years_there=years_there, location_held=location_held, sentence=sentence, crime=crime, offense_date=offense_date, sentence_date=sentence_date, county=county, resentence=resentence)

# get the information for each ID


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)