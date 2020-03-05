import pandas as pd

def prepare_missing_summary(some_df):
    count_of_null = some_df.isnull().sum().sort_values(ascending=False)
    percentage_of_null = (some_df.isnull().sum()/some_df.isnull().count()).sort_values(ascending=False)
    return pd.concat([count_of_null,percentage_of_null],axis=1,keys=['Total','Percentage'])