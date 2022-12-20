from TF_IDF.tf_idf_transformer import tf_idf_transformer
import pandas as pd
import numpy as np

def spares_to_df(speicherpfad):
    """ This function applies a secondary layer of preprocessing to the text, this is
    being done seperatlely, as this allows to reuse as many previous steps as possible
    for several different use cases. e.g. the gpt3 summarizes requieres as unprocessed
    as possible

    Args: (as before)
        speicherpfad (str): This variable defines the savin location on your computer,
        from there on everything is automated. it is Requiered to read in the pdf and
        this is saved in the py file "import_pdfs" in the folder "TF_IDF_authornames"

    Returns:
        list of lists (string): The list of list contains the string of the pdfs
    """
    X, vocab=tf_idf_transformer(speicherpfad)
    #, feature_names, vocab
    df=pd.DataFrame.sparse.from_spmatrix(X)
    #xxx=np.where(matrix.sum(axis=0) !=1)[1]
    liste=[]
        #remove the "_" in front of the keys
    temp_dict={}
    for i in vocab:
        x=vocab[i]
        temp_dict[i]=x.replace('_','')

    #rename the columns
    #df.set_axis(liste, axis=1,inplace=True)
    df = df.rename(columns= temp_dict)

    #feature_names, matrix, xxx
    return df
if __name__ == "__main__":
    print((spares_to_df('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data').keys()))
