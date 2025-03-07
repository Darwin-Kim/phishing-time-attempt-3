import homograph
from csv import writer
from contextlib import suppress
import random
import pandas as pd
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TODO:
#  DARWIN
#-----------------------------------------------------------------------------------------------------------------------------------------------

links=pd.DataFrame(columns=['Date','Link'])
SusLinks=pd.read_csv('SusLinks.csv')
TrustedLinks=pd.read_csv('TrustedLinks.csv')

#Running the 1st in a series of extended tests
def HomographExtendedTest1(SusLink,TrustedLink):
    print(TrustedLink)
    print("Link to check: ",SusLink," Trusted Link: ", TrustedLink)
    print("Input:",SusLink," Trusted Link [i2]:",TrustedLink," similar:",homograph.looks_similar(SusLink,TrustedLink))

    # Adding the possibly suspiscious link to the database if it is similar to the link in row i of the TrustedLinks database
    if homograph.looks_similar(SusLink, TrustedLink):
        print(input, time.ctime())
        links=links.append({'Link':SusLink, 'Date':time.ctime()},ignore_index=True)

# Appending all bad links to BadLinks.csv
def BadLinksAppend(input):
    same=0
    BadLinks=pd.read_csv('BadLinks.csv')
    # Checking if the link is equivalent to a link already in the database, and adding it to the database if it isn't
    for i2 in range(len(BadLinks)):
        if input['Link'][i2]==BadLinks.at[i2,'Link']:
            same=1
        if same==0:
            print('bad:',input[:][i2])
            input[:][i2].to_csv('BadLinks.csv', mode='a', index=False, header=False)

for i in range(len(SusLinks)):
    SusLink=SusLinks['Link'][i]
    for i2 in range(len(TrustedLinks)):
        TrustedLink=TrustedLinks['Link'][i2]
        HomographExtendedTest1(SusLink, TrustedLink)

# Clearing the SusLinks.csv file once every link in the file has ran through all tests
file=open('SusLinks.csv','w')
file.truncate()
file.close()

# Adding all flagged links to BadLinks.csv
BadLinksAppend(links)