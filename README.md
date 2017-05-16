<i>Update to original <a href="https://github.com/ceostroff/florida-death-row">respository</a> that gets info from a python dictionary </i>
<h2> What is this thing?</h2>

Over the course of Advanced Web Apps, a UF course that taught back-end coding , I became something of the Department of Corrections beat reporter. 


For my final project, I was inspired by the Texas Tribune's <a href="https://apps.texastribune.org/death-row/">project</a> to build a filterable Flask App using data I scraped from <a href="http://www.dc.state.fl.us/activeinmates/deathrowroster.asp">the Florida Department of Corrections</a> to write information to a CSV. Using a CSV instead of the original python dictionary, I was able to make this project filterable.

About 20 inmates' are missing from this database as their names are listed as being on deathrow but their pages are broken. I'll be contacting Florida's DOC to get more information on that this week.

In the coming days, I will also change the styles and try to make it look a bit nicer as well as start going through court records to add summaries for each erson about what exactly they did, instead of just that they're on death row for first degree murder.

<h2>How do I run it></h2>

You will need...
<ul>
<li>Python 3.x.</li>
<li>Flask and its dependencies installed</li>
<li>Your virtual env activated (if applicable)</li>
</ul>

To run it, put $ python deathrow.py in Terminal. Go to localhost:5000/ to test it out or see the live version <a href="http://ceostroff.com/florida-death-row/">here</a>. 



