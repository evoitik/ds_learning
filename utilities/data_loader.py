import pandas as pd


def load_csv(filepath) -> pd.DataFrame:
    """
        Function for loading csv-format files
    """
    try:
        # Attempt to read the CSV file
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError(f"The file '{filepath}' is empty.")
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Error parsing the file '{filepath}': {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading '{filepath}': {e}")
