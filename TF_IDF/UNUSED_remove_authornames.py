from TF_IDF.UNUSED_remove_stopwords import remove_stopwords
from TF_IDF_authornames.globalize_authornamelist import globalize_authornamelist
from nltk.tokenize import word_tokenize

def remove_authornames(speicherpfad):
    """This function does the exact same as the remove_stopwords one, but uses removes the authors names
    instead of the nltk stopwords. The process however is the exact same. in order to so it initially loads
    the list of author names from the "TF_IDF_authornames" folder.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        paper_list_nostopwords_noauthornames (string): The list of list caontaining the string of the pdfs, with removed stopwords

    """
    # load the list that already doesn't include the nltk stopwords
    paper_list_nostopwords=remove_stopwords(speicherpfad)

    # load the authornames list
    global_authorlist=globalize_authornamelist(speicherpfad)

    #initiate the output contianer
    paper_list_nostopwords_noauthornames=[]

    #itterate over the papers
    for paper in paper_list_nostopwords:
        #initiate a temporarylist that's being cleared for every paper over again
        temp_list=[]
        #tokenize the paper that is currently being looped over
        #word_tokens = word_tokenize(paper)
        for w in paper:
            if w not in global_authorlist:
                temp_list.append(w)
        paper_list_nostopwords_noauthornames.append(temp_list)
    return paper_list_nostopwords_noauthornames

if __name__ == "__main__":
    print(remove_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
    print('----------------------------------')
    print(len(remove_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
