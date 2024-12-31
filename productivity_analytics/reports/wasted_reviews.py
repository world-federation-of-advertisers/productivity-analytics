import pandas as pd


def wasted_reviews(pr_df: pd.DataFrame,
                   review_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Displays a table with reviews per author for PRs that never got merged.

    # Parameters

    pr_df (pd.DataFrame): PR data
    review_df (pd.DataFrame): PR review data

    # Returns

    pd.DataFrame: A table with reviews per author for PRs that never got merged.

    # Example

    ```python
    import pandas as pd
    from productivity_analytics import wasted_reviews

    wasted_reviews(pr_df, review_df)

    '''

    # add boolean column (True if not merged)
    pr_df['not_merged'] = pr_df['merged_at'].isna()

    # add float column for number of review comments for a given PR number
    review_count_data = pd.DataFrame(review_df['number'].value_counts()).reset_index()
    review_count_data = review_count_data.rename(columns={'count': 'review_comment_count'})
    pr_df = pr_df.merge(review_count_data, on='number')

    # create a temp dataframe to count number of authored PRs
    total_prs_authored = pr_df[['user_login']]
    total_prs_authored['pr_count'] = 1
    total_prs_authored = total_prs_authored.groupby('user_login').sum().reset_index()

    # create a temp dataframe to count number of reviews received 
    wasted_pr_reviews = pr_df[pr_df['not_merged'] == True]
    wasted_pr_reviews = wasted_pr_reviews.groupby('user_login', as_index=False)
    wasted_pr_reviews = wasted_pr_reviews['review_comment_count'].sum()

    wasted_pr_reviews = wasted_pr_reviews.merge(total_prs_authored, on='user_login')

    comments = wasted_pr_reviews['review_comment_count']
    prs = wasted_pr_reviews['pr_count']

    wasted_pr_reviews['review_waste_ratio'] = (comments / prs).round(2)

    return wasted_pr_reviews.sort_values(['review_waste_ratio', 'pr_count'])
