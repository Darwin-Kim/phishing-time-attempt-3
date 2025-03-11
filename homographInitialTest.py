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

iterations=0
NumChangeLetter=1
Base="classroom.google.com"
input="classroom.google.com"

TrustedLinks=pd.read_csv('TrustedLinks.csv')
SusLinks=pd.read_csv('SusLinks.csv')


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

# function for 1st homograph test (whether the link contains nonlatin characters)
def HomographTest1(input):
    AcceptedCharacters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\',';',"'",',','.','/'
                    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}', '|',':','"','<','>','?']
    bad=False
    for i in range(len(input)):
        if input[i] not in AcceptedCharacters:
            print('bad',input[i])
            bad=True
        else:
            print('OK',input[i])
    print('Homographic:',bad)
    print(input)
    if bad:
        DfAppend(input,'BadLinks.csv')
    else:
        DfAppend(input,'SusLinks.csv')

def DfAppend(input,csv):
    same=0
    dataframe=pd.read_csv(csv)
    print(pd.read_csv(csv))
    # Checking if the link is equivalent to a link already in the database, and adding it to the database if it isn't
    for i2 in range(len(dataframe)):
        print(input,dataframe.at[i2,'Link'])
        if input==dataframe.at[i2,'Link']:
            same=1
    if same==0:
        print('bad:',input)
        input={'Date':[time.ctime()],'Link':[input]}
        input_df=pd.DataFrame(input)
        input_df.to_csv(csv, mode='a', index=False, header=False)
#---------------------------------------------------------------------------------------------------------------------------------------------------
HomographTest1(input)