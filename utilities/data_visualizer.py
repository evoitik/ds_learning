import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from typing import DataFrame


def plot_heatmap(df, title, figsize=None, **kwargs):
    try:
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        plt.figure(figsize=figsize)
        sns.heatmap(df, **kwargs)
        plt.title(title, fontsize=kwargs.get('fontsize', 16))
        plt.show()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting the heatmap: {e}")


def plot_barplot(df, x, y, title=None, x_label=None, y_label=None, legend=None, **kwargs):
    try:
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        if x not in df.columns or y not in df.columns:
            raise ValueError(f"Columns '{x}' or '{y}' not found in the DataFrame.")
        
        plot = kwargs.get('ax', plt)
        sns.barplot(data=df, x=x, y=y, **kwargs)
        plot.set_title(title)
        plot.set_xlabel(x_label)
        plot.set_ylabel(y_label)
        plot.legend(title=legend)
        plt.show()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting the bar plot: {e}")


def plot_histogram(df: pd.DataFrame, x: str, hue: str = None, **kwargs) -> None:
    try:
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        if x not in df.columns:
            raise ValueError(f"Column '{x}' not found in the DataFrame.")
        
        sns.histplot(data=df, x=x, hue=hue, **kwargs)
        plt.show()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting the histogram: {e}")


def plot_scatter(df, x, y, title=None, x_label=None, y_label=None, **kwargs):
    try:
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        if x not in df.columns or y not in df.columns:
            raise ValueError(f"Columns '{x}' or '{y}' not found in the DataFrame.")
        
        plot = kwargs.get('ax', plt)
        sns.scatterplot(x=x, y=y, data=df, **kwargs)
        plot.set_title(title)
        plot.set_xlabel(x_label)
        plot.set_ylabel(y_label)
        plt.show()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting the scatter plot: {e}")


def plot_count(df, x, title=None, x_label=None, y_label=None, **kwargs):
    try:
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        if x not in df.columns:
            raise ValueError(f"Column '{x}' not found in the DataFrame.")
        
        plot = kwargs.get('ax', plt)
        sns.countplot(x=x, data=df, **kwargs)
        plot.set_title(title)
        plot.set_ylabel(y_label)
        plot.set_xlabel(x_label)
        plt.show()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while plotting the count plot: {e}")