from TF_IDF_preprocessing.import_pdf_text import import_pdf_text
import re

def reduce_text_until_references(speicherpfad):
    """This function takes a list of list containing strings and reduces those to the part until
    the first mentioning of the word "references" this is being done in order to reduce the
    exposure to faulty text, as no import information aka keyword is under the references.

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        list of lists (string): The list of list contains the string of the pdf, however reduced
        to the part until the last mention of the word (References)
    """
    #import the output from the previous py file
    input, filenames =import_pdf_text(speicherpfad)
    #initiate the output container
    list_of_shortend_papers=[]
    #itterate over the individual pdfs
    for papers in input:
        #remove braces, make lowercase, strip whitespace, replace
        #define the various types of openeing brackets
        opening_braces = '\(\['
        closing_braces = '\)\]'
        #define the non greedy wildcard, so regex minimizes it
        non_greedy_wildcard = '.*?'
        #regex applicatioj
        papers = re.sub(f'[{opening_braces}]{non_greedy_wildcard}[{closing_braces}]', ' ', papers)
        #make the text lowercase only
        papers = papers.lower()
        #define the word until which it will search
        sub_str = "references"
        res = papers.split(sub_str)#[:-1]
        fin_text = ' '
        for i in res:
            fin_text = fin_text+ ' '+ i
            #print(f"----------------------ARTICLE {x}-----------------", res[0])
            fin_text = fin_text.strip()
            fin_text = fin_text.replace('\n', ' ')
            fin_text = fin_text.replace('  ', ' ')
        list_of_shortend_papers.append(fin_text)
    return list_of_shortend_papers

if __name__ == "__main__":
    print(reduce_text_until_references('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[0])
    print('----------------------------------')
    print(len(reduce_text_until_references('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
