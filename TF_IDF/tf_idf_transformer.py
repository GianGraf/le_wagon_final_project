from TF_IDF.stemming import stemming
from TF_IDF.secondary_preprocessing import secondary_preprocessing
from  sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def tf_idf_transformer(speicherpfad):
    """ This function imports the list of lists and is here initally being joined back together
        into a coherent text. Secondly it is now being transformed into the TF IDF algorithm.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns: X: the fit_transformed TF_IDF Vectorizer
    """
    #load the text fromt he previous step
    paper_list_nostopwords_noauthornames=stemming(speicherpfad)

    intermediary_list=[]
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)

#Joine the words backtogether into one ling string
    for paper in paper_list_nostopwords_noauthornames:
        intermediary_list.append(" ".join(paper))

    paper_list_nostopwords_noauthornames=[]
    paper_list_nostopwords_noauthornames=intermediary_list
#Use the tf idf own vectorizer, as the transformer requieres a vectorizes input
    vectorizer = TfidfVectorizer(stop_words= 'english')
    #, use_idf=True
    X = vectorizer.fit_transform(paper_list_nostopwords_noauthornames)
    vocab=vectorizer.vocabulary_
    vocab_2={y: x for x, y in vocab.items()}
    #tfidf_vector_array=tfidf_vector.toarray()
#use the tf idf transformer
    #tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    #tfidf_transformer.fit_transform(paper_list_nostopwords_noauthornames)

    return X, vocab_2 #, vectorizer.get_feature_names_out(), vocab

if __name__ == "__main__":
    print(len(tf_idf_transformer('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[0]))
