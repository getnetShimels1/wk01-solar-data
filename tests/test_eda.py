import pytest
import pandas as pd
from src.eda_analysis import df  # Import your dataframe

def test_data_loading():
    assert df is not None, "Data not loaded"
    assert df.shape[0] > 0, "Dataset is empty"
    assert df.shape[1] > 0, "Dataset has no columns"

def test_summary_stats():
    assert df['GHI'].mean() > 0, "GHI column has no meaningful data"