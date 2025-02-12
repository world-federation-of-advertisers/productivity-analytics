import pandas as pd


def pr_merged_monthly_total(pr_df: pd.DataFrame,
                            month) -> int:

    pr_df['merged_at'] = pd.to_datetime(pr_df['merged_at'])

    return pr_df.groupby(pr_df['merged_at'].dt.to_period('M'))['number'].nunique()[month]
