from TF_IDF_authornames.reduce_text_to_after_references import reduce_text_to_after_references
import re

def extract_raw_authorcandidates(speicherpfad):
    """this function uses a regex code to searcht the reduced text fromt he previously called function,
    and searches a pattern, that is typicall for how references at the end of a scientific paper are
    modeled after. This however is ofcourse still in a raw version, as sometimes others results are
    also being found, this will be dealt with in future functions.

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

    Returns:
        autorenliste_raw: This is a list of strings, containing the result of the regex search.
    """
    #Definition of the regex string command line
    regex = r"([A-Za-z]* )?[a-zA-Z]*, [a-zA-Z]\.([a-zA-Z]\.)?"

    #set up a new empty list to fillt the found author names into..
    autorenliste_raw=[]

    # call the previous function and call the shortend text to search in
    list_of_texts_short=reduce_text_to_after_references(speicherpfad)

    #loop over the list of pdfs and extract the fields that match the pattern of authors
    # under the references area at the end of the paper.. if you want to tweek that got
    # to regex 101 and start with the code"([A-Za-z]* )?[a-zA-Z]*, [a-zA-Z]\.([a-zA-Z]\.)?
    for text in list_of_texts_short:
        temporary_list=[]
        matches = re.finditer(regex, text, re.MULTILINE)

    #loop over the matches aka the author names (currently in a weird list  or dict type )
    # and append them to the formerly empty list..
        for match in matches:
            temporary_list.append(match.group())
        autorenliste_raw.append(temporary_list)

    return autorenliste_raw
if __name__ =="__main__":
    print(len(extract_raw_authorcandidates('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
