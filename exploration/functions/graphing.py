import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def filter_by_count(df, column, count):
    '''filter column in dataframe by number of times an item appears'''
    
    new_df = df.groupby(column).filter(lambda x: len(x) > count)
    
    return new_df


def plot_filtered_groupby(df, groupby_col, sort_col, count, agg_func):
    '''using the filter_by_count function, graph horizontal bar chart of grouped column'''
    
    df_filtered = filter_by_count(df, groupby_col, count)\
                         [[groupby_col, sort_col]]\
    
    df_agg = df_filtered.groupby([groupby_col])[sort_col]\
                        .apply(agg_func)\
                        .reset_index()\
                        .sort_values([sort_col], ascending = False)
    
    fig, ax = plt.subplots(figsize=(8, 12))
    
    ax = sns.barplot(data=df_agg, x=sort_col, y=groupby_col, color = 'cyan')
    plt.show()
    
    
def timeseries_plot(df, timeseries_col, y_col, agg_func, dStart, dEnd, sample_by = 'D'):
    
    timeseries_vs_y = df[[timeseries_col, y_col]]
    plot_df = timeseries_vs_y.set_index(timeseries_col).resample(sample_by)[y_col].apply(agg_func)
    df = plot_df[(dStart <= plot_df.index) & (plot_df.index <= dEnd)]

    ax = plt.figure(figsize=(12, 6)).add_subplot(111)   
    xticks = pd.date_range(start=dStart, end=dEnd, freq='M')

    df.plot(ax = ax, xticks = xticks)

    ax.set_xticklabels([x.strftime('%h\n%Y') for x in xticks])
    plt.setp(ax.xaxis.get_majorticklabels(), ha='right')
 
    plt.show()
    
    
