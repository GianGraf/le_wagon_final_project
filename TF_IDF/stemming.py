from TF_IDF.remove_stopwords_and_authornames import remove_stopwords_and_authornames
from nltk.stem import PorterStemmer

def stemming(speicherpfad):
    """ this function turns every word in the list of lists into its original base word
    e.g. funny -> fun, horses -> horse.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        paper_list_nostopwords_noauthornames (list of list of stringd): The list of list contains the string of the pdfs

    """
    #load the data
    paper_list_nostopwords_noauthornames=remove_stopwords_and_authornames(speicherpfad)

    #initiate the stemmer
    ps = PorterStemmer()

    temp_container=[]
    #loop over the paper
    for paper in paper_list_nostopwords_noauthornames:
        sublist=[]
        for word in paper:
            sublist.append(ps.stem(word))
        temp_container.append(sublist)

    #overwrtie the initial value
    paper_list_nostopwords_noauthornames=[]
    paper_list_nostopwords_noauthornames=temp_container

    return paper_list_nostopwords_noauthornames

if __name__ == "__main__":
    print((stemming('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[0]))
