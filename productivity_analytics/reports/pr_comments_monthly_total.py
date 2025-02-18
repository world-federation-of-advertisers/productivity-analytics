import pandas as pd


def pr_comments_monthly_total(review_df: pd.DataFrame,
                              month) -> int:

    review_df['created_at'] = pd.to_datetime(review_df['created_at'])

    data = review_df[review_df['state'] == 'CHANGES_REQUESTED']
    
    return data.groupby(review_df['created_at'].dt.to_period('M')).size()[month]