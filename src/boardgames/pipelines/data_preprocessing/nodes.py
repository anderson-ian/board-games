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
    cols_to_keep = [each for each in details.columns.tolist() if 'boardgame' in each]

    details = details.loc[:,cols_to_keep]
    return details
