import pandas as pd


def pr_days_to_close(pr_df: pd.DataFrame,
                     review_df: pd.DataFrame) -> pd.DataFrame:
    
    '''
    Creates a DataFrame with the days it took to close a PR which can be
    added as a feature to pr_df.

    # Parameters

    pr_df (pd.DataFrame): PR data
    review_df (pd.DataFrame): PR review data

    # Returns

    None

    # Example

    ```python
    import pandas as pd
    from productivity_analytics import pr_days_to_close

    pr_days_to_close(pr_df, review_df)

    '''

    out = []

    for number in pr_df['number']:

        # Only include PRs that are not open (i.e., closed or merged)
        if pr_df.loc[pr_df['number'] == number]['state'].values != 'open':

            # Convert relevant cols to datetime in case df is loaded from file
            pr_df['created_at'] = pd.to_datetime(pr_df['created_at'])
            pr_df['closed_at'] = pd.to_datetime(pr_df['closed_at'])
            pr_df['merged_at'] = pd.to_datetime(pr_df['merged_at'])
            
            review_df['created_at'] = pd.to_datetime(review_df['created_at'])

            # Initialize temp variables for computing days to close
            pr_created = pr_df.loc[pr_df['number'] == number]['created_at']
            pr_closed = pr_df.loc[pr_df['number'] == number]['closed_at']
            pr_merged = pr_df.loc[pr_df['number'] == number]['merged_at']

            # Create temp DataFrames for computing days to close
            pr_events = pd.concat([pr_created, pr_closed, pr_merged])

            review_events = review_df.loc[review_df['number'] == number]
            
            review_events = review_events.sort_values('created_at')['created_at']

            pr_events = pd.concat([pr_events, review_events])
            pr_events = pr_events.reset_index().drop('index', axis=1)
            
            time_to_close = (pr_events.iloc[-1] - pr_events.iloc[0])[0]
            days_to_close = time_to_close.total_seconds() / 3600 / 24
            out.append([pr_events.iloc[0][0], days_to_close])

    data = pd.DataFrame(out)
    data.columns = ['created_at', 'days']

    return data
