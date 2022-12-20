from TF_IDF_authornames.import_pdfs import import_pdfs

def import_pdf_text(speicherpfad):
    list_of_papers=import_pdfs(speicherpfad)
    return list_of_papers

if __name__ == "__main__":
    print(import_pdf_text('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')[0])
    print(len(import_pdf_text('/Users/giangraf/code/GianGraf/le_wagon_final_project/data/data')))
