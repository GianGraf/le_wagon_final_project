from TF_IDF_authornames.first_cleaning_raw_authors import first_cleaning_raw_authors

def spliting_first_cleaned_candidates(speicherpfad):
    """the first cleaned candidates are often still strings in the form of sentences,
    this functions seperates those sentences into individual words, that are then
    being furtherly preprocessed.

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

    Returns:
        initially_cleaned_andspererates_candidates: list of list, the elements of the sublist are strings and
        they are now split along the spaces, to provide individual words
                        first level of the list = papers
                        second level of the list = candidated per paper
    """
    #initiate the empty output container
    initially_cleaned_andspererates_candidates=[]
    #call the results from the importet and preceeding function
    initially_cleaned_candidates=first_cleaning_raw_authors(speicherpfad)
    #loop over the papers
    for i in initially_cleaned_candidates:
        #initiate a temporay list
        sublist=[]
        #iterate over the individual candidates
        for j in i:
            #split the individual candidates and flatted the thereby produced 3rd level lists immediately again
            sublist.extend(j.split())
        #append the temporary list to the initiated output container
        initially_cleaned_andspererates_candidates.append(sublist)

    return initially_cleaned_andspererates_candidates

if __name__ =="__main__":
    print(len(spliting_first_cleaned_candidates('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
