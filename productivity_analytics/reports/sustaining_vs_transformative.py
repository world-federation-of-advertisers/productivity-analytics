import pandas as pd


def sustaining_vs_transformative(merged_per_tag_data: pd.DataFrame) -> pd.DataFrame:

    '''
    Display a comparison between sustainining and transformative PRs.

    # Parameters

    merged_per_tag_data (pd.DataFrame): Data resulting from merged_per_tag function

    # Returns

    pd.DataFrame: A DataFrame with the count of each type of PR and its relative share

    # Example

    ```python
    import pandas as pd
    from productivity_analytics import sustaining_vs_transformative

    sustaining_vs_transformative(merged_per_tag_data)

    '''

    data = pd.DataFrame(merged_per_tag_data['type_of_work'].value_counts())
    data['relative_share'] = (data['count'] / data['count'].sum() * 100).round(2)

    return data
