from spliting_first_cleaned_candidates import spliting_first_cleaned_candidates

def remove_2lettershort_candidates(speicherpfad, file_name_list):
    """After having splitted the candidates, many new very short strigns were produced, especially
    the first name abbreviations e.g. Muster, M. was processed to Muster M, and in the last step
    to Muster, M now we need to remove all the "M"s

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

    Returns:
        initially_cleaned_andspererates_candidates_shortend: list of list, the elements of the sublist are strings and
        they are now split along the spaces, to provide individual words, all too short elements were deleted
                        first level of the list = papers
                        second level of the list = candidated per paper
    """
    #produce the output container
    initially_cleaned_andspererates_candidates_shortend=[]
    #call the results from the previous function
    initially_cleaned_andspererates_candidates=spliting_first_cleaned_candidates(speicherpfad, file_name_list)
    #itterate over the papers
    for i in initially_cleaned_andspererates_candidates:
        #initiate a temporary list
        subliste3=[]
        #itterate over the candidates
        for j in i:
            #check length, must be longer then two letters
            if len(j)>2:
                subliste3.append(j)
        initially_cleaned_andspererates_candidates_shortend.append(subliste3)
    return initially_cleaned_andspererates_candidates_shortend
if __name__ =="__main__":
    print(remove_2lettershort_candidates('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', ['asset_prcing_1.pdf','asset_prcing_2.pdf', 'asset_prcing_3.pdf']))
