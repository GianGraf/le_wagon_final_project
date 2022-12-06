from keep_only_correct_namingconvention import keep_only_correct_namingconvention

def globalize_authornamelist(speicherpfad, file_name_list):
    """this function produces one global list of author names that can latter be removed
    from text in the same manner stopwords are being removed.

    Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

    Returns:
        global_authorlist: list of strings
        this list contains all the authornames that could be extracted from the
        papers. They than had to survived the selection and preprocessing and can
        now be used globally over all the papers.
    """

    #call the output from the previous function
    cleaned_separated_longerthan2letters_namingconvention_candidates=keep_only_correct_namingconvention(speicherpfad, file_name_list)
    #initiate the output container
    global_authorlist=[]
    #initiate a temporary variante for the second task as well, will lateet be deleted
    global_authorlist_temp=[]
    #itterate over the papers
    for i in cleaned_separated_longerthan2letters_namingconvention_candidates:
        #iterate over the authornames
        for j in i:
            global_authorlist_temp.append(j)
    #secondly we have to drop all duplicates
    #itterate over the authornames
    for i in global_authorlist_temp:
        if i not in global_authorlist:
            global_authorlist.append(i)
    return global_authorlist

if __name__ =="__main__":
    print(globalize_authornamelist('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', ['asset_prcing_1.pdf','asset_prcing_2.pdf', 'asset_prcing_3.pdf']))
