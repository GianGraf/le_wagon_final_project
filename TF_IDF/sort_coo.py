from TF_IDF.tf_idf_transformer import tf_idf_transformer
from sklearn.feature_extraction.text import TfidfVectorizer
from TF_IDF.secondary_preprocessing import secondary_preprocessing
import pandas as pd
from sympy import *
from scipy.sparse import csc_matrix

def sort_coo(speicherpfad):
    """This is a sub function for the TF_IDF vectorizer, and is being fed
    by another function from within the TF_IDF folder"

    Args:
        coo_matrix (sparse matrix): This fucntion required the fit_transformed sparse matrix


    Returns: X: the fit_transformed TF_IDF Vectorizer
    """
    X=tf_idf_transformer(speicherpfad)
    X_2=csc_matrix.tocoo(X)
    listof_secondarily_preprocessed_text=secondary_preprocessing(speicherpfad)
    tuples = zip(X_2.col, X_2.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

if __name__ == "__main__":
    print(sort_coo('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data'))
