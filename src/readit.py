import pandas as pd

def csv(url = "https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv"):
    
    print(f"reading data from {url}")
    
    return pd.read_csv(url)