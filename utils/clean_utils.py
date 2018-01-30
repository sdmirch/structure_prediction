import pandas as pd
import numpy as np


def clean_dataframe(df_raw, feature_type="cell_nuc_only"):
    """
    Removes columns from raw dataframe, removal specified by feature_type,
    and returns features, labels, and identifiers.

    Args:
        df_raw (pandas.DataFrame): Dataframe with raw data.
        feature_type (str): String referring to removal specification
            cell_nuc_only: Remove all features without feat_cell and feat_nuc

    Returns:
        features (pandas.DataFrame): features for analysis, dependent on feature_type.
        labels (pandas.DataFrame): targets (structureProteinName').
        identifiers (pandas.DataFrame): unique identifiers for cells ('cellID', 'save_feats_path').
    """
    columns = df_raw.columns
    
    label_column = ['structureProteinName']
    id_columns = ['cellID', 'save_feats_path']

    if feature_type == "cell_nuc_only":
        drop_columns = []
        for name in columns:
            if 'feat_cell' in name:
                continue
            elif 'feat_nuc' in name:
                continue
            else:
                drop_columns.append(name)

    features = df_raw.drop(drop_columns, axis=1)
    labels = df_raw[label_column]
    identifiers = df_raw[id_columns]

    return features, labels, identifiers
