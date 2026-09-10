#importing libraries
from pathlib import Path
import pandas as pd

def load_data(file_path):
    
    path = Path(file_path).suffix.lower()

    if path == '.csv':
        df = pd.read_csv(file_path)
        return df
    
    elif path == '.xlsx':
        df = pd.read_excel(file_path)
        return df
    
    else:
        raise ValueError(f'Unsupported format: {path}')
    