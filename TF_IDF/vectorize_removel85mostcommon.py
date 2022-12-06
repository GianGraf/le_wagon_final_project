from TF_IDF.import_preprocessed_text_file import import_preprocessed_text_file
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
import re

def vectorize_removel85mostcommon(speicherpfad):
    """ This function removes the standard nltk stopwords from our in the meantime generally
    preprocessed text. The 85 percent mark is absolutely crucial, as this decides on a threshold of which words are being kicked.
    Hence to optimize, this can and should be looked at.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        list of lists (string): The list of list contains the string of the pdfs
    """
    # import the file fromt he previous step
    listof_secondarily_preprocessed_text=import_preprocessed_text_file(speicherpfad)
    #load a set of stop words
    stopwords2=stopwords.words('english')

    #create a vocabulary of words,
    #ignore words that appear in 85% of documents,
    #eliminate stop words
    cv=CountVectorizer(max_df=0.85)

    return cv.fit_transform(listof_secondarily_preprocessed_text)

if __name__ == "__main__":
    print(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    print(len(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
