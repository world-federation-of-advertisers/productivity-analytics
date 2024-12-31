import pandas as pd


def pr_per_tag(merged_per_tag_data: pd.DataFrame) -> pd.DataFrame:

    '''
    Display the number of PRs per tag and their relative share.

    # Parameters

    merged_per_tag_data (pd.DataFrame): Data resulting from merged_per_tag function

    # Returns

    pd.DataFrame: A DataFrame with the count of PRs per tag and their relative share

    # Example

    ```python
    import pandas as pd
    from productivity_analytics import pr_per_tag

    pr_per_tag(merged_per_tag_data)

    '''

    data = pd.DataFrame(merged_per_tag_data['tag'].value_counts())
    data['relative_share'] = (data['count'] / data['count'].sum() * 100).round(2)

    return data
