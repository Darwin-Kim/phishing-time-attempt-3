import homograph
from contextlib import suppress
import random
iterations=0
NumChangeLetter=1
Base="docs.google.com"
String="docs.google.com"

# Running the code to replace NumChangeLetter letters with similar
# counterparts
for i in range(NumChangeLetter):

    # Telling the code which number to change. May make this number
    # specifiable later.
    changeLetter=random.randint(0, len(String)-1)
    homograph_generator = homograph.generate_similar_chars(String[changeLetter])

    # The StopIteration error is used to stop the iteration of the homograph
    # generator. If not bypassed, the will stop running entirely when it 
    # reaches this line.
    with suppress(StopIteration):

        # TypeError will occur if the given character is not a letter, but 
        # instead a character such as a "." or a "/", which will inevitably
        # happen when links are inserted. The need for this line could be 
        # eliminated if we end up specifying which characters to change.

        try:
            while homograph_generator != String[changeLetter]:
                String=String[0:changeLetter]+next(homograph_generator)+String[changeLetter+1:]
                print(String)
                iterations+=1

        # TypeError will occur if the given character is not a letter, but 
        # instead a character such as a "." or a "/", which will inevitably
        # happen when links are inserted. The need for this line could be 
        # eliminated if we end up specifying which characters to change.

        except TypeError:
            pass

# Ensuring that the final string is not the same as the original string once 
# the code has finished running, and re-randomizing the letters if it is
while String==Base:
    changeLetter=random.randint(0, len(String)-1)
    homograph_generator = homograph.generate_similar_chars(String[changeLetter])
    with suppress(StopIteration):
        try:
            while homograph_generator != String[changeLetter]:
                String=String[0:changeLetter]+next(homograph_generator)+String[changeLetter+1:]
                iterations+=1
        except TypeError:
            pass
# Printing the string to visualize it
print(String)

# Making sure that the final product is still homographic to the original
print("Link 1:",String," Link 2:",Base," similar:",homograph.looks_similar(String,Base))