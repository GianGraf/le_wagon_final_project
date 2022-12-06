from TF_IDF_authornames.remove_2lettershort_candidates import remove_2lettershort_candidates

def keep_only_correct_namingconvention(speicherpfad):
    """Here the candidates are furtherly filteres based on how they are written, only the ones
    with a fist Capital letter and then non-capital letters are furtherly considered as candidates.

    hence the goal is to furtherly increase the qulity of the candidates

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

    Returns:
        cleaned_separated_longerthan2letters_namingconvention_candidates: list of list, the elements
        of the sublist are strings, however we furhterly filter the the candidates, based on how
        they are written.
                first level of the list = papers
                second level of the list = candidated per paper
    """
    #initiate the output container
    cleaned_separated_longerthan2letters_namingconvention_candidates=[]
    #call the previous results
    input=remove_2lettershort_candidates(speicherpfad)
    #iterate over the papers
    for i in input:
    #initiate a temporary list
        subliste=[]
        #iterate over the candidates
        for j in i:
            #check the writting convention
            if j[0].isupper() and j[1:].islower():
                subliste.append(j)
        cleaned_separated_longerthan2letters_namingconvention_candidates.append(subliste)
    return cleaned_separated_longerthan2letters_namingconvention_candidates

if __name__ =="__main__":
    print(len(keep_only_correct_namingconvention('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
