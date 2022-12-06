from remove_and_sign import remove_and_sign

def reduce_text_to_after_references(speicherpfad, file_name_list):
    """This code searches for the index of the last occurence of the word 'references',
    this is being done in order for us to start the search only aftet this occurance and to
    therefor reduce the number of wrong matches


   Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

    Returns:
        list_of_texts_short: it returns the same variable as it calls from the function "remove_and_sign",
        however it cuts it down to only the part after the last occurence of the word "references"
    """
    #This code searches for the index of the last occurence of the word 'references', this is being done in order fot us to start the search only aftet this occurance
    list_of_texts_short=remove_and_sign(speicherpfad, file_name_list)
    for i in range(len(list_of_texts_short)):
        ref_index=list_of_texts_short[i].lower().rfind('references')
        list_of_texts_short.append(list_of_texts_short[i][ref_index:])

    return list_of_texts_short

if __name__ =="__main__":
    print(reduce_text_to_after_references('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', ['asset_prcing_1.pdf','asset_prcing_2.pdf', 'asset_prcing_3.pdf']))
