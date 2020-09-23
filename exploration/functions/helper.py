import pandas as pd
import numpy as np

def read_in_data(df_names, directory = './'):
    '''Read in data into seperate dataframes'''
    
    # change directory to data storage location
    os.chdir(directory)
    
    # list of filenames
    extension = 'csv'
    filenames = [i for i in glob.glob('*.{}'.format(extension))]
    
    # create global dfs within function
    for name, file in zip(df_names, filenames):
        globals()[name] = pd.read_csv(file)
        

def replace_na_with_text(df, column, new_text):
    '''replace missing text with preferred description'''
    
    # change missing data to appropriate label
    df[column] = df[column].replace(np.nan, new_text)

    
def timestamp_to_datetime(df, columns):
    '''convert multiple timestamp columns to datetime'''
    
    for col in columns:
        df[col] = pd.to_datetime(df[col])

def lowercase(df, columns):
    '''change all text to lowercase'''
    
    for col in columns:
        df[col] = df[col].str.lower()
        
        
def translate_column_with_df(df_original, df_translation, column_original, column_translation): 
    '''Translate column, given df with translation'''
    
    # convert translation to dictionary to extract key, value pairs
    df_translation = df_translation.set_index(column_original)
    df_translation = df_translation.to_dict('dict')
    
    # map translations
    df_original[column_original] = df_original[column_original]\
                                               .replace(df_translation[column_translation])

    
def merge_multiple_df_on_key(dfs, key):
    '''create dataframe with customer info including their location, order details and review'''
    
    from functools import reduce
    
    # stolen from https://stackoverflow.com/questions/23668427/pandas-three-way-joining-multiple-dataframes-on-columns)
    new_df = reduce(lambda left,right: pd.merge(left,right, how = 'inner', on=key), dfs)
    
    return new_df

def drop_duplicates_ignore_cols(df, cols_to_ignore, keep = 'first'):
    '''drop duplicates but ignore certain columns'''
    
    df.drop_duplicates(keep = keep, \
                       subset=df.columns.difference(cols_to_ignore), \
                       inplace=True)
        