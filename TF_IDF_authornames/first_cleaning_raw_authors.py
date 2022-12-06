from TF_IDF_authornames.extract_raw_authorcandidates import extract_raw_authorcandidates

def first_cleaning_raw_authors(speicherpfad):
    """This fucntion does a initial cleaning of the authorcandidates:
        1. it removes ".", "," and white space to the left and right of the strings
        2. it removes all list entries who are only 1 character long, as they must be noise, no
        author name is only one character long.

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

    Returns:
        initially_cleaned_candidates: a initially cleaned list of lists of author candidates..
                        first level of the list = papers
                        second level of the list = candidated per paper
    """

    #create an empty list that can be returned to carry the results
    initially_cleaned_candidates=[]
      #call the result from the called function
    input=extract_raw_authorcandidates(speicherpfad)

    #itterate over the papers (first level of list in list)
    for papers in input:
        #create a temporary list, that will later be appended again
        subliste4=[]
        #itterate over the second level, aka over the sublists
        for candidate in papers:
            #remove dots, commas, whitespace to the left and to the right of the individual substrings
            subliste4.append(candidate.replace(".","").replace(",", "").rstrip().lstrip())
        #append the cleaned strings back into the output list list of lists
        initially_cleaned_candidates.append(subliste4)

        # this second part, does the second task of this function

        #itterate over the papers
        for i in initially_cleaned_candidates:
            #itterate over the candidates per paper
            for j in i:
                if len(j)==1:
                    i.remove(j)
    return initially_cleaned_candidates

if __name__ =="__main__":
    print(len(first_cleaning_raw_authors('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
