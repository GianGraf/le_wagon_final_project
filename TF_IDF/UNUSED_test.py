
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from TF_IDF.secondary_preprocessing import secondary_preprocessing

def vectorize_removel85mostcommon(speicherpfad):
    """ This function takes the list of words that have the stopwwords and
    authornames already removed. it then vectorizes the remaining text and
    removes the 85% of words that are common in 85% of all papers

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your
        computer, from there on everything is automated. it is Requiered to
        read in the pdf and this is saved in the py file "import_pdfs" in the
        folder "TF_IDF_authornames"

    Returns:
        cv.fit_transform(paper_list_nostopwords_noauthornames): This function
        retunrs the count vector, meaning the fitted and transformed vector.
    """
    from TF_IDF.remove_authornames import remove_authornames
    paper_list_nostopwords_noauthornames=remove_authornames(speicherpfad)

    # import the file fromt he previous step
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)
    #create a vocabulary of words,
    #ignore words that appear in 85% of documents,
    #eliminate stop words

    int_paper=[]
    cv_input=[]
    #,stop_words=stopwords
    #for paper in paper_list_nostopwords_noauthornames:
    #    int_paper=list(filter(None, paper))
    #    cv_input.append(int_paper)
    cv=CountVectorizer(max_df=0.85)
    word_count_vector=cv.fit_transform(listof_secondarily_preprocessed_text)
    return word_count_vector
    #return cv

if __name__ == "__main__":
    print(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    #print(type(listof_secondarily_preprocessed_text))
    #print(len(vectorize_removel85mostcommon('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
