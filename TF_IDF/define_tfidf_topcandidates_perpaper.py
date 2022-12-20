from TF_IDF.drop_unnecessary_columns import drop_unnecessary_columns
from TF_IDF_authornames.import_pdfs import import_pdfs
import pandas as pd

def define_tfidf_topcandidates_perpaper(speicherpfad, no_of_output_per_paper):
    #load previous results
    df=drop_unnecessary_columns(speicherpfad)

    #Import the list of names of the papers, in the order inwhich they are read into the document
    list_of_papers, filenames = import_pdfs(speicherpfad)
    #transpose the data frame
    df_t=df.T
    no_of_columns=df_t.shape[1]
    output_df= pd.DataFrame(index=range(no_of_columns),columns=['pdf_name', 'title', 'author', 'uniquieish_words'])
    raw_df = pd.DataFrame(index=range(no_of_columns),columns=['pdf_name', 'title', 'author', 'preprocessed_text'])

    for i in range(no_of_columns):
        sorted_df=df_t.sort_values(i, ascending=False)
        sorted_words=sorted_df.index.values
        uniqueish_words_dict={}
        for j in range(no_of_output_per_paper):
            uniqueish_words_dict[sorted_words[j]]=sorted_df[i][j]
            output_df['uniquieish_words'][i]=uniqueish_words_dict

    #Hier werden die Namen der PDF Dokumente zum Data frame hinzugefügt.
    output_df["pdf_name"]=filenames
    return output_df

if __name__ == "__main__":
    print(define_tfidf_topcandidates_perpaper('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data', 50))
