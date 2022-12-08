from TF_IDF.secondary_preprocessing import secondary_preprocessing

import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(speicherpfad):
    """This function is first downloading a set of stop words from nltk.
    It subsequently then tokenizes the input text before removing those tokens
    that do matcht the stopword list.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        paper_list_nostopwords (string): The list of list caontaining the string of the pdfs, with removed stopwords

    """
    # load the list of twice preprocssed textfiles
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)

    #initiate the output contianer
    paper_list_nostopwords=[]

    #initiate the stopwords list
    stop_words = set(stopwords.words('english'))

    #itterate over the papers
    for paper in listof_secondarily_preprocessed_text:
        #initiate a temporarylist that's being cleared for every paper over again
        temp_list=[]
        #tokenize the paper that is currently being looped over
        word_tokens = word_tokenize(paper)
        for w in word_tokens:
            if w not in stop_words:
                temp_list.append(w)
        paper_list_nostopwords.append(temp_list)
    return paper_list_nostopwords, stopwords

if __name__ == "__main__":
    print(remove_stopwords('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    print(len(remove_stopwords('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
