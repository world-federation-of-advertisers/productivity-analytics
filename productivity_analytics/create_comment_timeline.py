import pandas as pd


def create_comment_timeline(number: int,
                            pr_df: pd.DataFrame,
                            review_df: pd.DataFrame) -> pd.DataFrame:
    
    '''
    Combines pr data with pr review data, to create a single timeline of all
    activity in the a single PR.

    # Parameters

    number (int): A pull request number.
    pr_df (DataFrame): A DataFrame containing pull request data.
    review_df (DataFrame): A DataFrame containing pull request review data.

    # Returns

    DataFrame: A DataFrame containing a complete timeline of all
    activity in a single PR.

    # Example

    ```python

    create_comment_timeline(123, pr_df, review_df)

    '''

    pr_data = pr_df[pr_df['number'] == number].squeeze()
    review_data = review_df[review_df['number'] == number]
    
    creation_data = pd.Series({'number': pr_data['number'],
                               'user_login': pr_data['user_login'],
                               'created_at': pr_data['created_at'],
                               'state': 'CREATED',
                               'type': 'create'})
    
    return pd.concat([creation_data.to_frame().T, review_data],
                     ignore_index=True)
