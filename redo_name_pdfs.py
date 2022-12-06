# creating list with all pdf file names
def name_pdfs():
    """_summary_: eturns a list of pdf names, that can later be added to the dataframe as a column themselves.
    This is to be done, in order to abel to identify the papers later on.

    !! this function needs to be altered to be able to produce a list of pdf names that are equal to
    the names of the actual files and it is requiered for it to be able to handle unequal numbers of
    papers per category!!
    Args:
        categories (list of strings): a list of strings has to be entered, the strings are the names of the categories
        no_of_papers_per_categorie (_type_): This function only works for

    Returns:
        _type_: _description_
    """

    pdf_names = []
    for x in range(0,7):
        cat = ['asset_prcing_', 'banking_', 'corporate_finance_', 'corporate_governance_', 'insurance_', 'investment_and_portfolio_management_', 'market_microstructure_']
        for i in range(0, 5):
            name = f'{cat[x]}{i+1}.pdf'
            pdf_names.append(name)

    return pdf_names

if __name__ == "__main__":
    print(name_pdfs())
  """
    r

    !! However, this is a hardcoded version sofar, aka it needs to be either modifed to automatically achieve it,
    or it has to be manually adapted every time.!!

    Input= manually
    Putput= list containing strings, pdf names

    """
