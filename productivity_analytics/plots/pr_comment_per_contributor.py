import astetik
import pandas as pd

import matplotlib.pyplot as plt


def pr_comment_per_contributor(review_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Plot the total number of Pull Request (PR) reviews or comments per author

    # Parameters

    review_df (pd.DataFrame): PR review data

    # Returns

    pd.DataFrame: The relative share of PR comments by each contributor

    # Example

    ```python
    import pandas as pd
    from productivity_analytics.plots import pr_comment_per_contributor

    pr_comment_per_contributor(pr_df)

    '''

    # Number of PR reviews or comments per contributor
    review_absolute_data = pd.DataFrame(review_df['user_login'].value_counts())

    astetik.hist(data=review_absolute_data,
                 x='count',
                 bins=len(review_absolute_data),
                 palette='Reds',
                 x_label='Total number of PR reviews',
                 y_label='Number of Observations',
                 title='How many PR reviews or comments are each contributor making?',
                 sub_title='[ Absolute Values ]')
    
    plt.show()

    # Relative share of PR comments by each contributor
    comments_df = pd.DataFrame((review_df['user_login'].value_counts() / len(review_df) * 100).round(2))
    comments_df.columns = ['Percentage of All Reviews']
    
    return comments_df
