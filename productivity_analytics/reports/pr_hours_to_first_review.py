import pandas as pd
import productivity_analytics as pa


def pr_hours_to_first_review(month: str,
                             pr_df: pd.DataFrame,
                             review_df: pd.DataFrame) -> int:

    year, month = map(int, month.split('-'))

    month_prs_created = pr_df[(pr_df['created_at'].dt.year == year) & (pr_df['created_at'].dt.month == month)]
    month_pr_numbers = month_prs_created['number'].unique()

    result = 0
    counter = 0

    for number in month_pr_numbers:

        review_created_at_data = pa.create_comment_timeline(number,
                                                            pr_df,
                                                            review_df).sort_values('created_at')['created_at']

        if len(review_created_at_data) > 1:

            td = review_created_at_data.iloc[1] - review_created_at_data.iloc[0]
            result += td.total_seconds() / 3600
            counter += 1

    # Avoid division by zero
    average_time_to_first_review = result / counter if counter > 0 else 0

    return int(average_time_to_first_review)
