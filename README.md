<i>This repo is an update to original <a href="https://github.com/ceostroff/florida-death-row">respository</a> that gets inmate information from a python dictionary. It also incorporates data from the original scraper I built, which can be seen <a href="https://github.com/ceostroff/inmates">here</a>. </i>
<h2> What is this thing?</h2>

Over the course of Advanced Web Apps, a UF course that taught back-end coding , I became something of the Department of Corrections beat reporter. 


For my final project, I was inspired by the Texas Tribune's <a href="https://apps.texastribune.org/death-row/">project</a> to build a filterable Flask App using data I scraped from <a href="http://www.dc.state.fl.us/activeinmates/deathrowroster.asp">the Florida Department of Corrections</a> to write information to a CSV. Using a CSV instead of the original python dictionary, I was able to make this project filterable.

About 20 inmates' are missing from this database as their names are listed as being on deathrow but their pages are broken on the FDCO website. 

<i>Note: this app is dynamic but deployed online as a static build <a href="http://www.ceostroff.com/florida-death-row/">here</a>. To view it dynamically, download the repository and run it in Terminal with $python deathrow.py. It is hosted on localhost:5000/. You can also run the original scraper to get the data in the scraping_program folder. Fair warning, this does take upward of an hour to run, and depending on when the website automatically changed the URLs, you may need to run it again. </i>




