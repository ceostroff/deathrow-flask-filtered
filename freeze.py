"""
When you run this file in the Terminal, it creates a static version of your Flask app in a folder named 'build.' You can upload this folder to your web server and run it without WSGI. Make sure you installed Frozen-Flask in your virtualenv before trying this. Note that it creates STATIC pages, so some types of Python interaction (such as forms) would not work.
"""

"""
Basic script for freezing a Flask app.
"""

from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR app
from deathrow import app

app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

"""
More details ...
Frozen-Flask can be configured using Flask’s configuration system. The following configuration values are accepted:
FREEZER_RELATIVE_URLS
If set to True, Frozen-Flask will patch the Jinja environment so that url_for() returns relative URLs. Defaults to False. Python code is not affected unless you use relative_url_for() explicitly. This enables the frozen site to be browsed without a web server (opening the files directly in a browser) but appends a visible index.html to URLs that would otherwise end with /.
Docs:
http://pythonhosted.org/Frozen-Flask/
http://pythonhosted.org/Frozen-Flask/#configuration
http://flask.pocoo.org/docs/0.12/config/
"""