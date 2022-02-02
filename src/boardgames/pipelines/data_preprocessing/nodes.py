import pandas as pd 

def preprocess_ratings(ratings: pd.DataFrame) -> pd.DataFrame:
    """Removes two url columns

    Args:
        ratings (pd.DataFrame): Straight csv downloaded from internet

    Returns:
        pd.DataFrame: Defaults in the csv downloaded from internet, less two columns
    """
    cols_to_drop = ['url','thumbnail']
    ratings.drop(cols_to_drop, axis=1, inplace=True)
    return ratings

def preprocess_details(details: pd.DataFrame) -> pd.DataFrame:
    """Removes text-based columns from the numerical variables

    Args:
        details (pd.DataFrame): Dataframe containing mutliple columns with 
        boardgame name prefix.

    Returns:
        pd.DataFrame: Data without board games included
    """
    
    # list of columns without boardgame
    cols_to_keep = [each for each in details.columns.tolist() if 'boardgame' not in each]
    
    # remove description from list of columns
    cols_to_keep = [each for each in cols_to_keep if 'description' not in each]

    details = details.loc[:,cols_to_keep]
    return details

def merge_ratings_details(prepro_ratings: pd.DataFrame,
                          prepro_details: pd.DataFrame) -> pd.DataFrame:
    """Combines preprocessed dataframes into single set.

    Args:
        prepro_ratings (pd.DataFrame): ratings table without urls
        prepro_details (pd.DataFrame): details table without narrative strings

    Returns:
        pd.DataFrame: Merged dataframe with column overlaps cleaned
    """

    # merge on id and clean up column overlaps
    ratings_details = \
    prepro_ratings.merge(prepro_details, 
                         left_on='id',
                         right_on='id',
                         how='inner') \
                   .drop('num_y',axis=1).rename({'num_x':'num'},axis=1)
    
    return ratings_details