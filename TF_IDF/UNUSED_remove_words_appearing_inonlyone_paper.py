from TF_IDF.UNUSED_countvectorizer_removalofstopwords import countvectorizer_removalofstopwords
import numpy as np

def remove_words_appearing_inonlyone_paper(speicherpfad):
    """ This function uses the vectorized words and figures out which words are only used in one paper. it achieves this by
    checking whether a word represented by a column only has a single one in it, it does so by summing up the amount of non
    zero values in the column, if this process ends up with a one, the whole columns gets dropped. this is done under the
    assumption, that there is no single word that is only being used one paper, this assumption becomes the more relieable
    the more paper are beind read in at once..

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        word_count_vector: the vectori of
    """
    #read in the input from the previous function
    word_count_vector=countvectorizer_removalofstopwords(speicherpfad)

    #fill a list with the ids of the words, that fullwil the criteria
    #ids_selected_words = np.where(word_count_vector.sum(axis=0) != 1)[1]

    #then select only the words, that have differnet ids
    #word_count_vector_reduced=word_count_vector[:,ids_selected_words]

    return word_count_vector
#word_count_vector_reduced

if __name__ == "__main__":
    print(remove_words_appearing_inonlyone_paper('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
