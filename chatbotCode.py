from typing import List, Tuple, Callable, Any
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
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards
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

def checkLink(input:str) -> List[str]:
    pass

def giveInstructions(dummy: List[str]) -> List[str]:
    return ["I can understand the following query patterns:","Does this link contain homographic characters: [Paste the link here]","What can I ask you to do?","Bye"]

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
# Entries in the PA list are written in the form (str.split("Query"), responseFunction),
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("does this link contain homographic characters: %"), checkLink),
    (str.split("what can i ask you to do"), giveInstructions),
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