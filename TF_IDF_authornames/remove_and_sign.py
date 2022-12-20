from TF_IDF_authornames.import_pdfs import import_pdfs

def remove_and_sign(speicherpfad):
    """the regex functon in the following step can not handle the "&" sign, hence
        we remove it here.

        Args: (same as before)
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

        Returns:
        list_of_texts: it returns the same variable as it calls from the function multiple_pdfs_to_list,
        however withpout the &-signs.
    """
    list_of_texts, filenames =import_pdfs(speicherpfad)
    for papers in list_of_texts:
        papers=papers.replace('&', '')
    return list_of_texts

if __name__ =="__main__":
    print(len(remove_and_sign('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
