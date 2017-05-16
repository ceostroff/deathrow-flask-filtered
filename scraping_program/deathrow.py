from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import csv



def openLinks(pageVals):
    html = urlopen("http://www.dc.state.fl.us/activeinmates/deathrowroster.asp")
    bsObj = BeautifulSoup(html, "html5lib")
# final regex string returns all links that start with /wiki/ and after that do not contain any colons 
    for link in bsObj.find("div", {"class":"dcCSScontent"}).findAll( "a", href=re.compile("^(../ActiveInmates/)(.)*$") ):
        if 'href' in link.attrs: 
            partial = str(link.attrs['href'])
            new_url = partial.replace("..", "http://www.dc.state.fl.us")
        pageVals.append(new_url) 
        print(new_url)
#function to get the demographic information for each inmate    
def getDetails(pageVals):
    global driver
    global inmate_details
    #for each link in the list you have stored in pageVals
    for value in pageVals:
        #open each link
        try:
            html = urlopen(value)
            time.sleep(3)
            bsObj = BeautifulSoup(html, "html5lib")
            td_list = bsObj.findAll("td", {"align":"LEFT"})
            time.sleep(1)
            inmate = {
                'id': td_list[0].get_text().strip(),
                'name': td_list[1].get_text().strip(),
                'race': td_list[2].get_text().strip(),
                'sex': td_list[3].get_text().strip(),
                'dob': td_list[8].get_text().strip(),
                'entry': td_list[9].get_text().strip(),
                'facility': td_list[10].get_text().strip(),
                'custody': td_list[11].get_text().strip(),
                }
            print(inmate)
            inmate_details.append(inmate)

        except IndexError:
            return
        
#function to save all of your hard work to a CSV        
def saveToCSV(inmate_details):
    #give the csv file you want to export it to a name
    filename = 'deathrowredo.csv' 
    #open your new csv file with a 'w' so you can write to it
    with open(filename, 'w') as output_file:
        #make headers for you columns. these must match up with the keys you set in your python dictionary, inamte
        fieldnames = [	'id',
                      'name',
                      'race',
                      'sex',
                      'dob',
                      'entry',
                      'facility',
                      'custody',
                     ]
        #write these into a csv, the headers being fieldnames and the rows your list of inmates
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inmate_details)
#you prefered driver has to open the original page to do all this. I use Firefox here but Chrome is also an option        
#your lists where info will be stored
pageVals = []
inmate_details = []

#run the functions, using the values (links) of the lists we created        
openLinks(pageVals)
print("Links Opened")
getDetails(pageVals)
print("Got details")
saveToCSV(inmate_details)
print("All done!")


#Ta-Da!    

