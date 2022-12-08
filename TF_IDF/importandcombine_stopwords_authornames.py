import nltk
from nltk.corpus import stopwords

from TF_IDF_authornames.globalize_authornamelist import globalize_authornamelist

def importandcombine_stopwords_authornames(speicherpfad):
    """This function imports the stopwords from nltk and combines them with the authornames from
    the TF_IDF_authornames folder.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        stopwords_list (list of string): This list is a comprahensive list of all the words that
        need to be removed from the nltk approach.

    """
    #define variable and add the nltk stopwords to it
    stopwords_list=stopwords.words('english')
    #download the authornames list
    global_authorlist=globalize_authornamelist(speicherpfad)
    #append the authornameslist to the stopwordslist
    stopwords_list.append(global_authorlist)

    return stopwords_list

if __name__ =="__main__":
    print(importandcombine_stopwords_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print("_____________________________________________________")
    print(len(importandcombine_stopwords_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
