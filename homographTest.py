# CHECKING IF THE GIVEN LINK IS HOMOGRAPHIC (going to be put into a different code file at some point)
#TODO:
#  - DARWIN -  start testing in this section (finish testing in previous section first)

SusLinks=pd.read_csv('SusLinks.csv')
TrustedLinks=pd.read_csv('TrustedLinks.csv')
for i in range(len(SusLinks)):
    # Printing linkToCheck and row i of column Link of the TrustedLinks database and the output of the function homograph.looks_similar
    # with the two links inputted, while i is in the range of the length of the TrustedLinks database
    linkToCheck=SusLinks['Link'][i]
    for i2 in range(len(TrustedLinks)):
        print("Input:",linkToCheck," Trusted Link [i2]:",TrustedLinks['Link'][i2]," similar:",homograph.looks_similar(input,TrustedLinks['Link'][i]))
    
    # Adding the possibly suspiscious link to the database if it is similar to the link in row i of the TrustedLinks database
    if homograph.looks_similar(linkToCheck, TrustedLinks['Link'][i2]):
        print(input, time.ctime())
        links=links.append({'Link':linkToCheck, 'Date':time.ctime()},ignore_index=True)
links.to_csv('BadLinks.csv', mode='a', index=False, header=False)   