import pytest
import pandas as pd

from src.boardgames.pipelines.data_preprocessing.nodes import (
    preprocess_ratings,
    preprocess_details
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

    def test_preprocess_details(self):
        """
        Confirm that column names are dropped.
        """
        test_df = pd.DataFrame({
                                'boardgame' : [],
                                'description' : [],
                                'col_A' : [],
                                'col_B' : []
                                 })

        expected_df = pd.DataFrame({
                                'col_A' : [],
                                'col_B' : []
                                 })

        actual_df = preprocess_details(test_df)

        if 'boardgame' not in actual_df.columns.to_list() and \
           'description' not in actual_df.columns.to_list():
            output = True
        else:
            output = False

        assert output
        assert actual_df.equals(expected_df)