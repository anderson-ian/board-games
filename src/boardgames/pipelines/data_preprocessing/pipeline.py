from kedro.pipeline import Pipeline, node

from .nodes import preprocess_ratings, preprocess_details

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_ratings,
                inputs="ratings",
                outputs="prepro_ratings",
                name="preprocess_ratings_node",
            ),
            node(
                func=preprocess_details,
                inputs="details",
                outputs="prepro_details",
                name="preprocess_details_node",
            ),

        ]
    )