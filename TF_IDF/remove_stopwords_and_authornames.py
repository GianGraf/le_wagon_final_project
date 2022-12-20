from TF_IDF.importandcombine_stopwords_authornames import importandcombine_stopwords_authornames
from TF_IDF.secondary_preprocessing import secondary_preprocessing

def remove_stopwords_and_authornames(speicherpfad):
    """This function takes care of the follwoign three things:
    1. it splits the papers from the previous steps into individual words, ergo we now are working witg
    a list of lists

    2. it removes all the stopwords and authornames within that list of lists

    3. it removes all the words within that list of list that is only one letter long


    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        paper_list_nostopwords_noauthornames (string): The list of list caontaining the string of the pdfs, with removed stopwords

    """
    # load the list of words that are to be removed
    stopwords_list=importandcombine_stopwords_authornames(speicherpfad)
    # load the preprocessed text
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)
    #initiate the output contianer
    paper_list_nostopwords_noauthornames=[]
    # outputlist
    outputlist=[]

# split the Strings that are part of the list into lists themselves, in order to exclude the stopwords and authornames
    for paper in listof_secondarily_preprocessed_text:
        temporary_list=[]
        temporary_list=paper.split()
        outputlist.append(temporary_list)

    #itterate over the papers
    for paper in outputlist:
        #initiate a temporarylist that's being cleared for every paper over again
        temp_list=[]
        #tokenize the paper that is currently being looped over
        #word_tokens = word_tokenize(paper)
        for w in paper:
            if w not in stopwords_list:
                temp_list.append(w)
        paper_list_nostopwords_noauthornames.append(temp_list)


#itterate over individual words and remove the ones, that are only one letter long
    output_list2=[]
    for paper in paper_list_nostopwords_noauthornames:
        temporary_list_2=[]
        for word in paper:
            if len(word) > 1:
                temporary_list_2.append(word)
        output_list2.append(temporary_list_2)
    paper_list_nostopwords_noauthornames=[]
    paper_list_nostopwords_noauthornames=output_list2

    return paper_list_nostopwords_noauthornames

if __name__ == "__main__":
    print(remove_stopwords_and_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[0])
    print('----------------------------------')
    print(len(remove_stopwords_and_authornames('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
