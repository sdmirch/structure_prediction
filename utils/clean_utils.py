import pandas as pd
import numpy as np


def reduce_dataframe(df_raw, feature_type="cell_nuc_only"):
    """
    Removes columns from raw dataframe, removal specified by feature_type,
    and returns reduced dataframe.

    Args:
        df_raw (pandas.DataFrame): Dataframe with raw data.
        feature_type (str): String referring to removal specification
            cell_nuc_only: Remove all features without feat_cell and feat_nuc

    Returns:
        df (pandas.DataFrame): Reduced dataframe.
    """
    columns = df_raw.columns

    if feature_type == "cell_nuc_only":
        drop_columns = []
        for name in columns:
            if 'feat_cell' in name or 'feat_nuc' in name or\
            name == 'structureProteinName' or name == 'cellID' or\
            name == 'save_feats_path':
                continue
            else:
                drop_columns.append(name)

    df = df_raw.drop(drop_columns, axis=1)

    return df

def clean_dataframe(df_reduced, feature_type="cell_nuc_only"):
    """
    Removes rows that have NaNs in all columns (based on first column),
    and replaces select columns' NaNs with the mean of the column.
    Hard coded for each scenario.

    Args:
        df (pandas.DataFrame): Dataframe with reduced data.
        feature_type (str): String referring to cleaning specification

    Returns:
        df (pandas.DataFrame): Cleaned dataframe.
    """

    if feature_type == "cell_nuc_only":
        # Remove rows that have NaNs in all columns, using first column as indicator.
        df = df_reduced[np.isfinite(df_reduced['feat_nuc_region_mean_px'])]

        # Replace NaNs in specific columns with the column mean.
        df['feat_nuc_obj_mean_edge_len'].fillna((df['feat_nuc_obj_mean_edge_len'].mean()), inplace=True)
        df['feat_nuc_obj_std_edge_len'].fillna((df['feat_nuc_obj_std_edge_len'].mean()), inplace=True)

    return df


def split_dataframe(df, feature_type="cell_nuc_only"):
        """
        Splits dataframe into features, labels, and identifiers.

        Args:
            df (pandas.DataFrame): Dataframe data.
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
        # features = df_raw.drop(drop_columns, axis=1)
        # labels = df_raw[label_column]
        # identifiers = df_raw[id_columns]
        #
        # return features, labels, identifiers
        pass
