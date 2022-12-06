#installing required packages
import fitz

def import_pdfs(speicherpfad, filename):
    """This function calls on a folder of pdfs files and convertes them to a string, in order for it
        to do so all the must be in the same folder so the code can itterate over the folder entries one after
        another.

    Args:
        speicherpfad (str): This variable contains the savingpath to the file
        filename (list(str)): _description_

    Returns:
        list: _description_
    """
    with fitz.open(f"{speicherpfad}/{filename}") as doc:
        text1 = ""
        for page in doc:
            text1 += page.get_text()
        return text1

if __name__ == "__main__":
    print(import_pdfs('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', 'asset_prcing_1.pdf'))
