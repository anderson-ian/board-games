from kedro.pipeline import Pipeline, node

from .nodes import preprocess_ratings

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_ratings,
                inputs="ratings",
                outputs="prepro_ratings",
                name="preprocess_ratings_node",
            ),
        ]
    )