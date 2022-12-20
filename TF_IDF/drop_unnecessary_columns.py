from TF_IDF.spare_to_df import spares_to_df
import numpy as np

def drop_unnecessary_columns(speicherpfad):
    """ This function takes the dataframe and defines a list of shitty column names, it excludes the following:
        - column names that are only a single special character
        - column names that include a special character are being dropped
        - column names that consist of repetions of a single character like aaa
        - column names that are a digit


    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer, from
        there on everything is automated. it is Requiered to read in the pdf and this is saved
        in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        df: the matrix, that includes the tf idf frequencies and distributions

    """
    #load the text fromt he previous processing step
    df=spares_to_df(speicherpfad)

    #produce a list of all column headbnames
    liste = list(df.columns.values)
    #initaite a container of the columns that are to be dropped
    remove_liste=[]
    #define the symbols that can not be included in the columns
    symbols = ['~','@','#','$','%','^','&','*','(',')','+','=','{','[','}','}','<','>'
               'Α',
               'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π',
               'Ρ', 'Σ','Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η',
               'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

    #remove the ones that are a digit and the ones that are a symbol
    for i in liste:
            if i.isdigit():
                remove_liste.append(i)
            if i in symbols:
                remove_liste.append(i)
    #check wether the list entries consits out of only one letter like aaa or fffff
    for word in liste:
        liist=[]
        for i in word:
            if i not in liist:
                liist.append(i)
        if len(liist)==1:
            remove_liste.append(word)
    #check wether the word is rubbish, as it includes a special character
    for word in liste:
        liist=[]
        for i in word:
            if i in symbols:
                remove_liste.append(word)
    #some of these fucntions detect the same values over agaon, hence they then should be droped from the list
    remove_liste = list(dict.fromkeys(remove_liste))

    #produce a new data frame that doesn't anymore include those columns

    df2=df.drop(remove_liste, axis = 1)
    no_of_columns_appearin_inonlyonepaper= np.count_nonzero(df2, axis=1)

    #ids_selected_words = np.where(df2.sum(axis=1) != 1)[1]
    return df2

    ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ
    αβγδεζηθικλμνξοπρστυφχψω

if __name__ == "__main__":
    print(drop_unnecessary_columns('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
