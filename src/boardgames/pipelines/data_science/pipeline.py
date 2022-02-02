from kedro.pipeline import Pipeline, node

from .nodes import make_primary_bins

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=make_primary_bins,
                inputs="merged_ratings",
                outputs="primary_model_input",
                name="feature_engineering_node",
            ),
        ]
    )