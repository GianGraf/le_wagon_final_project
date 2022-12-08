from TF_IDF.importandcombine_stopwords_authornames import importandcombine_stopwords_authornames
from TF_IDF.secondary_preprocessing import secondary_preprocessing
from sklearn.feature_extraction.text import CountVectorizer

def countvectorizer_removalofstopwords(speicherpfad):
    """ this function vectorizes the pdfs and simultaneously removes the authornames
    and stopwords.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        word_count_vector: the vectorized version of the texts

    """
#IMPORT THE DATA FROM PREVIOUS STEPS
    #load the stopwords and authornames lsit
    stopwords_list=importandcombine_stopwords_authornames(speicherpfad)
    #load the secondarily preporcessed text
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)

    corpus = ['This is the first document.','This document is the second document.','And this is the third one.','Is this the first document?']


#VECTORIZE THE PREPROCESSED TEXT
    #define the Countvectorizer to a variable
    vectorizer = CountVectorizer(max_df=0.8, stop_words=stopwords_list)
    #
    #fit and transform the vectorizer to the existing data
    #listof_secondarily_preprocessed_text=[listof_secondarily_preprocessed_text]
    word_count_vector=vectorizer.fit_transform(corpus)

    return word_count_vector

if __name__ == "__main__":
    print(countvectorizer_removalofstopwords('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
