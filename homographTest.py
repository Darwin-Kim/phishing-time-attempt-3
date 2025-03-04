import homograph
from csv import writer
from contextlib import suppress
import random
import pandas as pd
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------
# INPUTTING A SUSPISCIOUS LINK
# TODO:
#   - Add an API/chatbot into this section of the code (Basically start from scratch, this is just a placeholder for the final product)
#   - Have the code put the suspiscious link into the SusLinks.csv file so this section of code can be seperate from the section below
iterations=0
NumChangeLetter=1
Base="classroom.google.com"
input="classroom.google.com"

links=pd.DataFrame(columns=['Date','Link'])
TrustedLinks=pd.read_csv('TrustedLinks.csv')
SusLinks=pd.read_csv('SusLinks.csv')
print(TrustedLinks)

# Running the code to replace NumChangeLetter letters with similar
# counterparts
for i in range(NumChangeLetter):

    # Randomizing which characters to change. May make this specifiable 
    # later.
    changeLetter=random.randint(0, len(input)-1)
    homograph_generator = homograph.generate_similar_chars(input[changeLetter])

    # The StopIteration error is used to stop the iteration of the homograph
    # generator. If not bypassed, the will stop running entirely when it 
    # reaches this line.
    with suppress(StopIteration):

        # TypeError will occur if the given character is not a letter, but 
        # instead a character such as a "." or a "/", which will inevitably
        # happen when links are inserted. The need for this line could be 
        # eliminated if we end up specifying which characters to change.

        try:
            while homograph_generator != input[changeLetter]:
                input=input[0:changeLetter]+next(homograph_generator)+input[changeLetter+1:]
                #print(input)
                iterations+=1

        # TypeError will occur if the given character is not a letter, but 
        # instead a character such as a "." or a "/", which will inevitably
        # happen when links are inserted. The need for this line could be 
        # eliminated if we end up specifying which characters to change.

        except TypeError:
            pass
# Printing the possibly suspiscious link to visualize it
print(input)
links=links.append({'Link':input,'Date':time.ctime()},ignore_index=True)
print(links)
bad=0

# Checking if the link contains a character that is not a latin/special character
for i in range(len(input)):
    if input[i]!="a"or'b'or'c'or'd'or'e'or'f'or'g'or'h'or'i'or'j'or'k'or'l'or'm'or'n'or'o'or'p'or'q'or'r'or's'or't'or'u'or'v'or'w'or'x'or'y'or'z'or'A'or'B'or'C'or'D'or'E'or'F'or'G'or'H'or'I'or'J'or'K'or'L'or'M'or'N'or'O'or'P'or'Q'or'R'or'S'or'T'or'U'or'V'or'W'or'X'or'Y'or'Z'or'!'or"@"or'#'or'$'or'%'or'^'or'&'or'*'or'('or')'or'-'or'_'or'+'or'='or'{'or'['or']'or'}'or'`'or'~'or'\\'or'/'or'|'or','or'.':
        bad=1

# Running the code below if the link contains one of these characters
if bad==1:
    same=0
    BadLinks=pd.read_csv('BadLinks.csv')

    # Checking if the link is equivalent to a link already in the database, and adding it to the database if it isn't
    for i2 in range(len(BadLinks)) and range(len(links)):
        if not links.at[i2,'Link']==BadLinks.at[i2,'Link']:
            links.to_csv('BadLinks.csv', mode='a', index=False, header=False)
            
# Adding the code to database of suspiscious links to be passed on to the second block if it is not immediately flagged as bad
else:
    links.to_csv('SusLinks.csv', mode='a', index=False, header=False)


#---------------------------------------------------------------------------------------------------------------------------------------------------
# CHECKING IF THE GIVEN LINK IS HOMOGRAPHIC (going to be put into a different code file at some point)
#TODO:
#  - Rewrite code so it takes links from SusLinks.csv and removes them from SusLinks.csv once it has run them through the system 
#    so this section of code can be seperate from the section above
#
#  - Rewrite code so it does not delete the links in BadLinks.csv every time it runs

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