import pandas as pd


def merged_vs_not(pr_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Display the rate of PRs that were merged and not merged.

    # Parameters

    pr_df (pd.DataFrame): PR data

    # Returns

    pd.DataFrame: The rate of PRs that were merged and not merged

    # Example

    ```python
    import pandas as pd
    from productivity_analytics import merged_vs_not

    merged_vs_not(pr_df)

    '''

    # Create a temp dataframe where merged PRs are counted per author
    merged_data = pd.DataFrame(pr_df[~pd.isna(pr_df['merged_at'])]['user_login'].value_counts())

    # Create a temp dataframe where not yet merged (or closed without merging) PRs are counted per author
    not_merged_data = pd.DataFrame(pr_df[pd.isna(pr_df['merged_at'])]['user_login'].value_counts())

    # Combine the two into a temp dataframe and adjust column names
    merged_vs_not_data = pd.concat([merged_data, not_merged_data], axis=1)
    merged_vs_not_data.columns = ['merged_count', 'not_merged_count']

    # Drop rows with NaN values and convert remaining values into integers
    merged_vs_not_data = merged_vs_not_data.dropna().astype(int)

    # Create new columns
    total_prs = merged_vs_not_data['not_merged_count'] + merged_vs_not_data['merged_count']
    merged_vs_not_data['total_prs'] = total_prs
    merge_rate = merged_vs_not_data['merged_count'] / merged_vs_not_data['total_prs'] * 100
    merged_vs_not_data['merge_rate'] = merge_rate
    merged_vs_not_data['merge_rate'] = merged_vs_not_data['merge_rate'].round(2)

    # Display the results
    return merged_vs_not_data.sort_values('merge_rate', ascending=False)
