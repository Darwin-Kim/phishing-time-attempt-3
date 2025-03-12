from typing import List, Tuple, Callable, Any
import pandas as pd
from homographTests import DfAppend
links=pd.DataFrame(columns=['Date','Link'])
SusLinks=pd.read_csv('SusLinks.csv')
TrustedLinks=pd.read_csv('TrustedLinks.csv')

# from homographTest import whateverDarwinEndsUpNamingTheirFunctions
def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)
    while sind < len(source) or pind < len(pattern):

        # 1) if we reached the end of the pattern but not source
        if  sind < len(source) and pind == len(pattern):
            return None
        # 2) if the current thing in the pattern is a %
        elif pattern[pind] == "%":
            percentString = ""
            if pind + 1 == len(pattern):
                while(sind != len(source)):
                    if(percentString != ""):
                        percentString += " " 
                    percentString += source[sind]
                    sind += 1
            else:
                while source[sind] != pattern[pind+1]:
                    if sind < len(source):
                        if(percentString != ""):
                            percentString += " " 
                        percentString += source[sind]
                        sind += 1
                    else: return None
            result.append(percentString)
            pind += 1

        # 3) if we reached the end of the source but not the pattern
        elif sind == len(source) and pind < len(pattern):
            return None
        # 4) if the current thing in the pattern is an _
        elif pattern[pind] == "_":
            result.append(source[sind])
            sind += 1
            pind += 1
        # 5) if the current thing in the pattern is the same as the current thing in the
        # source
        elif pattern[pind] == source[sind]:
            sind += 1
            pind += 1
        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source
        else: 
            return None

    return result

def isHomographic(input:str) -> bool:
    AcceptedCharacters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\',';',"'",',','.','/'
                    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}', '|',':','"','<','>','?']
    for i in range(len(input)):
        if input[i] not in AcceptedCharacters:
            print('Homographic',input[i])
            return True
    return False


def checkLink(input:str) -> List[str]:
    pass
    if not isHomographic(input):
        DfAppend(input,'SusLinks.csv')
        return ["The link you have entered does not contain any homographs!", "However, you should still proceed with caution and make sure it is a trusted website."]
    elif isHomographic(input):
        DfAppend(input,'BadLinks.csv')
        return ["The link you have entered contains either homographic characters or characters I do not recognize.","It is likely dangerous, so please do not click it."]
def generateSimilarLink(input:str) -> List[str]:
    pass

def phishingBlurb(dummy: List[str]) -> List[str]:
    return ["A phishing attack is a cyberattack in which the attacker impersonates a legitimate institution in an attempt to steal the victim’s personal information. Phishing is the most important form of cybercrime, so it is important to know how to avoid it.","Phishing attacks often take the form of emails, but can also be phone calls, text messages, or even malicious QR codes pasted over legitimate ones.","Attackers will often use your information to steal your money, but another common way they will use your information is to inform ‘spear phishing’ attacks on others. Spear phishing attacks are targeted to specific people, often executives or people with access to important information. These attacks use personal information to make themselves seem more legitimate in order to convince their targets into giving away valuable information."]

def homographBlurb(dummy: List[str]) -> List[str]:
    return ["A homographic character is a non-Latin character that looks extremely similar or visually identical to a Latin character. These characters can be used in phishing attacks to create fake links that are visually identical to trusted links but actually lead to the attacker’s website, which they will use to take a victim’s personal information or install malware on their device. Can you tell these two links apart?","googlе.com","google.com"]

def giveInstructions(dummy: List[str]) -> List[str]:
    return ["I can understand the following query patterns:","Does this link contain homographic characters: [Paste the link here]","What can I ask you to do?","What is a homograph?","What is a phishing attack?","Bye [Closes program]"]

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

# A list of query patterns and their corresponding response functions
# It must be declared here, after all of the function definitions
# Entries in the PA list are written in the form (str.split("query"), responseFunction),
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("does this link contain homographic characters: %"), checkLink),
    (str.split("what can i ask you to do"), giveInstructions),
    (str.split("what is a homograph"), homographBlurb),
    (str.split("tell me about homographs"), homographBlurb),
    (str.split("what is a phishing attack"), phishingBlurb),
    (str.split("what is phishing"),phishingBlurb),
    (str.split("tell me about phishing"),phishingBlurb),
    (str.split("tell me about phishing attacks"),phishingBlurb),
    #(str.split("generate a homographic string for this link: %"), generateSimilarLink),
    (["bye"],bye_action)
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pa in pa_list:
        if match(pa[0],src) != None:
            answer = pa[1](match(pa[0],src))
            if answer == []:
                return ["No answers"]
            else: return answer
    return ["I don't understand. Please type 'What can I ask you to do?' for information on what queries I can accept"] 


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome! I am a chatbot designed to keep you safe from phishing attacks! \n For a list of available commands, please ask: 'What can I ask you to do?'")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()