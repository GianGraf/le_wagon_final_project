from TF_IDF.remove_authornames import remove_authornames
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re

def vectorize_removel85mostcommon(speicherpfad):
    """ This function takes the list of words that have the stopwwords and authornames already removed. it then vectorizes the remaining
    text and removes the 85% of words that are common in 85% of all papers

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        cv.fit_transform(paper_list_nostopwords_noauthornames): This function retunrs the count vector, meaning the fitted and
        transformed vector.
    """
    # import the file fromt he previous step
    paper_list_nostopwords_noauthornames=remove_authornames(speicherpfad)


    #create a vocabulary of words,
    #ignore words that appear in 85% of documents,
    #eliminate stop words
    cv=CountVectorizer(max_df=0.85)
    word_count_vector=cv.fit_transform(paper_list_nostopwords_noauthornames)
    return word_count_vector

if __name__ == "__main__":
    print(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    #print(len(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
