from import_pdfs import import_pdfs

def multiple_pdfs_to_list(speicherpfad, file_name_list):
    """
    This function calls the previous function "import_pdfs" and does this in a
    itterable manner, it then returns a list of strings, the latet being the pdf's texts.

    Args:
        speicherpfad (str): savingspath, where the pdfs are saved under

        file_name_list (list of strings): Here a list strings is requiered, this list has to
        contain all the names of the pds that are in the folder in the correct order of how they
        will then be read by the code

        Returns:
        pdf_text_list: it returns a list of strings, the latter being the texts from the pdfs
    """
    # a empty list is being produced, where the pdf texts that are being extracted can be saved in
    pdf_text_list=[]
    # itterate over the files in the folder and extract them one after an other
    for file_name in file_name_list:
    # call the predifed function that extracts the text from the pdfs
        pdf_text_as_string=import_pdfs(speicherpfad, file_name)
        #append the strign to the predefined output list
        pdf_text_list.append(pdf_text_as_string)
    return pdf_text_list

if __name__ == "__main__":
    print(multiple_pdfs_to_list('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', ['asset_prcing_1.pdf','asset_prcing_2.pdf', 'asset_prcing_3.pdf']))
