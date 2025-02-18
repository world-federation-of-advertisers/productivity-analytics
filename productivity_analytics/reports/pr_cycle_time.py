import pandas as pd


def pr_cycle_time(month: int, pr_df: pd.DataFrame) -> int:

    year, month = map(int, month.split('-'))
    pr_data = pr_df[(pr_df['merged_at'].dt.year == year) & (pr_df['merged_at'].dt.month == month)]

    return (pr_data['merged_at'] - pr_data['created_at']).mean().days
