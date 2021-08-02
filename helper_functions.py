def null_count(df):
    return df.isnull().sum()


def Ran(df,seed):
    return df.sample(frac=1, random_state=seed)