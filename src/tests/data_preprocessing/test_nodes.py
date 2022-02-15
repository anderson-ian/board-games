import pytest
import pandas as pd

from src.boardgames.pipelines.data_preprocessing.nodes import (
    preprocess_ratings
)

class TestPrimaryNodes:
    def test_preprocess_ratings(self):
        """
        Confirm that columns are dropped.
        """
        test_df = pd.DataFrame(
                                {
                                'url' : [],
                                'thumbnail' : [],
                                'test_col_1' : [],
                                'test_col_2' : []
                                }
                              )

        expected_df = pd.DataFrame(
                      {
                       'test_col_1' : [],
                       'test_col_2' : []}
                       )
        
        actual_df = preprocess_ratings(test_df)
        assert actual_df.equals(expected_df)
        