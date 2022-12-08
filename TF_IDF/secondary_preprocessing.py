from TF_IDF.import_preprocessed_text_file import import_preprocessed_text_file
import re

def secondary_preprocessing(speicherpfad):
    """ This function applies a secondary layer of preprocessing to the text, this is
    being done seperatlely, as this allows to reuse as many previous steps as possible
    for several different use cases. e.g. the gpt3 summarizes requieres as unprocessed
    as possible

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        list of lists (string): The list of list contains the string of the pdfs

    """
    #load the text from the previous step
    list_of_shortend_papers=import_preprocessed_text_file(speicherpfad)

    #initiate the output container
    listof_secondarily_preprocessed_text=[]
    #iterate over the papers
    for paper in list_of_shortend_papers:
        # lowercase
        paper=paper.lower()
        #remove tags
        paper=re.sub("","",paper)
        # remove special characters and digits
        paper=re.sub("(\\d|\\W)+"," ",paper)
        listof_secondarily_preprocessed_text.append(paper)
    return listof_secondarily_preprocessed_text


if __name__ == "__main__":
    print(secondary_preprocessing('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    print(type(secondary_preprocessing('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[3]))
