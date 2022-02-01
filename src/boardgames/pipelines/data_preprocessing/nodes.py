import pandas as pd 

def preprocess_ratings(ratings: pd.DataFrame) -> pd.DataFrame:
    
    cols_to_drop = ['url','thumbnail']
    ratings.drop(cols_to_drop, axis=1, inplace=True)
    return ratings
