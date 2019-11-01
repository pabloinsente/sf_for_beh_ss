def bar_plot_percent(series: str, kind: str ='barh', title: str = 'Title', order=None, sort=False, size=None, df='df_ds'):
    '''Plot a series as percentage

    Arguments:
    ----------
    series(str)   -- series to be plot (default None)
    kind(str)     -- type of plot (default barh)
    title(str)    -- plot title (defaul 'Title')
    order(list)   -- apply custom order (default None)
    sort(bool)    -- sort in descending order (default False)
    size(tuple)   -- width and hight dimensions (default None)
    df(DataFrame) -- DataFrame to be plot (default df_ds)

    Returns:
    --------
    plot
    '''
    if sort:
        return df[series].value_counts().apply(lambda x:np.round((x/df[series].notna().sum())*100, decimals=2)).reindex(order).sort_values(ascending = sort).plot(kind=kind, figsize=size,title=title);
    else:
        return df[series].value_counts().apply(lambda x: np.round((x/len(df))*100, decimals=2)).reindex(order).plot(kind=kind, figsize=size, title=title);
