from typing import List, Tuple, Callable, Any
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

# def query_loop() -> None:
#     """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
#     characters and exit gracefully.
#     """
#     print("Welcome to the movie database!\n")
#     while True:
#         try:
#             print()

#         except (KeyboardInterrupt, EOFError):
#             break

#     print("\nSo long!\n")

