import homograph
from csv import writer
from contextlib import suppress
import random
import pandas as pd
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TODO:
#  DARWIN
#  - Change code to allow for a queue in SusLinks.csv
#  - Add a check to ensure that the same link is not appended to BadLinks.csv twice (copy from initial test)
#-----------------------------------------------------------------------------------------------------------------------------------------------

links=pd.DataFrame(columns=['Date','Link'])
SusLinks=pd.read_csv('SusLinks.csv')
TrustedLinks=pd.read_csv('TrustedLinks.csv')
for i in range(len(SusLinks)):
    print(SusLinks)

    # Printing linkToCheck and row i of column Link of the TrustedLinks database and the output of the function homograph.looks_similar
    # with the two links inputted, while i is in the range of the length of the TrustedLinks database
    linkToCheck=SusLinks['Link'][i]
    for i2 in range(len(TrustedLinks)):
        print("Link to check: ",linkToCheck," Trusted Link: ", TrustedLinks['Link'][i2])
        print("Input:",linkToCheck," Trusted Link [i2]:",TrustedLinks['Link'][i2]," similar:",homograph.looks_similar(linkToCheck,TrustedLinks['Link'][i]))
    
    # Adding the possibly suspiscious link to the database if it is similar to the link in row i of the TrustedLinks database
        if homograph.looks_similar(linkToCheck, TrustedLinks['Link'][i2]):
            print(input, time.ctime())
            links=links.append({'Link':linkToCheck, 'Date':time.ctime()},ignore_index=True)
links.to_csv('BadLinks.csv', mode='a', index=False, header=False)
