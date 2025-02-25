import pandas as pd
from logging import Logger as logger


def get_missing_count(df: pd.DataFrame, column: str) -> int:
    """
        Function for printing missing value is a particular column
    """
    return df[column].isnull().sum()

def print_missing_counts(df: pd.DataFrame) -> None:
    """
        Function for printing count of missing values per DataFrame column
    """
    missing_counts = {col: get_missing_count(df, col) for col in df.columns}

    for col, missing_count in missing_counts.items():
        logger.info(f'Number of missing values in "{col}" column: {missing_count}.')
    return missing_counts

#TODO: to realise logic while working on na-present values datasets.
def fill_na_values():
    pass


