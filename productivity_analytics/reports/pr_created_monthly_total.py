import pandas as pd


def pr_created_monthly_total(pr_df: pd.DataFrame,
                             review_df: pd.DataFrame,
                             month) -> int:

    pr_df['created_at'] = pd.to_datetime(pr_df['created_at'])
    review_df['created_at'] = pd.to_datetime(review_df['created_at'])

    return pr_df.groupby(pr_df['created_at'].dt.to_period('M'))['number'].nunique()[month]
