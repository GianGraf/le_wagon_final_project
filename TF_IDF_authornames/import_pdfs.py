#installing required packages
import fitz
import os
import numpy as np

def read_file(speicherpfad, filename):
    """here the filename is automatically being generated.

    Args:
        speicherpfad (_type_): _description_
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with fitz.open(f"{speicherpfad}/{filename}") as doc:
        text1 = ""
        for page in doc:
            text1 += page.get_text()
    return text1

def import_pdfs(speicherpfad):
    """This function calls on a folder of pdfs files and convertes them to a string, in order for it
        to do so all the must be in the same folder so the code can itterate over the folder entries one after
        another.

    Args:
        speicherpfad (str): This variable contains the savingpath to the file
        filename (list(str)): _description_

    Returns:
        list_of_papers: list of strings, the strings being the read in papers.
    """
    filenames=np.array(os.listdir(speicherpfad))
    filenames=filenames[["pdf" in item for item in filenames]]
    list_of_papers=[]
    for file in filenames:
        list_of_papers.append(read_file(speicherpfad, file))
    return list_of_papers, filenames

if __name__ =="__main__":
    print((import_pdfs('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[-1]))
