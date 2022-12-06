from TF_IDF_preprocessing.reduce_text_until_references import reduce_text_until_references
import pandas as pd
import numpy as np

def import_preprocessed_text_file(speicherpfad):
    """ This function imports the textfile from the folder "TF_IDF_preprocessing",
    thereby the textfile can be used here

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        list of lists (string): The list of list contains the string of the pdfs

    """
    #load the text fromt he previous processing step
    list_of_shortend_papers=reduce_text_until_references(speicherpfad)
    return list_of_shortend_papers

if __name__ == "__main__":
    print(import_preprocessed_text_file('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    print(len(import_preprocessed_text_file('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
