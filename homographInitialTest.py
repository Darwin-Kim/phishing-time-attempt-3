import homograph
from csv import writer
from contextlib import suppress
import random
import pandas as pd
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------
# INPUTTING A SUSPISCIOUS LINK
# TODO:
#   ISABEL 
# - Add an API/chatbot into this section of the code
#
#   DARWIN 
# - Finish making functions
# - fix link printing twice into csv and delete temporary(probably) workaround

AcceptedCharacters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\',';',"'",',','.','/'
                    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}', '|',':','"','<','>','?']
iterations=0
NumChangeLetter=1
Base="classroom.google.com"
input="classroom.google.com"

TrustedLinks=pd.read_csv('TrustedLinks.csv')
SusLinks=pd.read_csv('SusLinks.csv')
print(TrustedLinks)

def HasNonLatinCharacters(latinCharacters,link):
    for i in range(len(link)):
        if link[i] not in latinCharacters:
            return True
        else:
            return False

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

# -------------------------------------------------- HERE ON OUT IS NOT TEMPORARY ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Printing the possibly suspiscious link to visualize it
print('input: ',input)

# function for 1st homograph test (whether the link contains nonlatin characters)
def HomographTest1(link):
    AcceptedCharacters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\',';',"'",',','.','/'
                    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}', '|',':','"','<','>','?']
    for i in range(len(link)):
        if link[i] not in AcceptedCharacters:
            BadLinksAppend(link)

def BadLinksAppend(input):
    same=0
    BadLinks=pd.read_csv('BadLinks.csv')
    # Checking if the link is equivalent to a link already in the database, and adding it to the database if it isn't
    for i2 in range(len(BadLinks)):
        if input==BadLinks.at[i2,'Link']:
            same=1
        if same==0:
            print('bad:',input)
            input.to_csv('BadLinks.csv', mode='a', index=False, header=False)

# Adding the code to database of suspiscious links to be passed on to the second block if it is not immediately flagged as bad
#---------------------------------------------------------------------------------------------------------------------------------------------------
HomographTest1(input)