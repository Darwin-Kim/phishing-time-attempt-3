import homograph
from csv import writer
from contextlib import suppress
import random
import pandas as pd
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TODO:
#  DARWIN
# - FIX THIS!!! (please??)
#-----------------------------------------------------------------------------------------------------------------------------------------------

links=pd.DataFrame(columns=['Date','Link'])
SusLinks=pd.read_csv('SusLinks.csv')
TrustedLinks=pd.read_csv('TrustedLinks.csv')

#Running the 1st in a series of extended tests
def HomographExtendedTest1(SusLink,TrustedLink):
    global links
    print(TrustedLink)
    print("Link to check: ",SusLink," Trusted Link: ", TrustedLink)
    #print("Input:",SusLink," Trusted Link [i2]:",TrustedLink," similar:",homograph.looks_similar(SusLink,TrustedLink))

    # Adding the possibly suspiscious link to the database if it is similar to the link in row i of the TrustedLinks database
    if homograph.looks_similar(SusLink, TrustedLink):
        print(input, time.ctime())
        links=links.append({'Links':SusLink, 'Date':time.ctime()},ignore_index=True)

# Adding all flagged links to BadLinks.csv
def DfAppend(input,csv):
    same=0
    dataframe=pd.read_csv(csv)
    print(pd.read_csv(csv))
    # Checking if the link is equivalent to a link already in the database, and adding it to the database if it isn't
    for i2 in range(len(dataframe)):
        print('input:',input,'dataframe:',dataframe.at[i2,'Link'])
        if input==dataframe.at[i2,'Link']:
            same=1
    if same==0:
        print('bad:',input)
        input={'Date':[time.ctime()],'Link':[input]}
        input_df=pd.DataFrame(input)
        input_df.to_csv(csv, mode='a', index=False, header=False)

for i in range(len(SusLinks)):
    SusLink=SusLinks['Links'][i]
    for i2 in range(len(TrustedLinks)):
        TrustedLink=TrustedLinks['Link'][i2]
        HomographExtendedTest1(SusLink, TrustedLink)

# Clearing the SusLinks.csv file once every link in the file has ran through all tests
file=open('SusLinks.csv','w')
file.truncate()
file.close()

DfAppend(links,'BadLinks.csv')