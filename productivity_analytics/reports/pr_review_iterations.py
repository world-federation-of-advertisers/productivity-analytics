import pandas as pd


def pr_review_iterations(month: int, review_df: pd.DataFrame) -> float:

    year, month = map(int, month.split('-'))
    review_data = review_df[(review_df['created_at'].dt.year == year) & (review_df['created_at'].dt.month == month)]

    return round(len(review_data) / len(review_data['number'].unique()), 1)
