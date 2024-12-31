import astetik
import matplotlib.pyplot as plt
import pandas as pd

from ..features import pr_days_to_close


def pr_open_to_resolve(pr_df: pd.DataFrame,
                       review_df: pd.DataFrame) -> None:

    '''
    Plot the mean days from Pull Request (PR) open to merge or close.

    # Parameters

    pr_df (pd.DataFrame): PR data
    review_df (pd.DataFrame): PR review data

    # Returns

    None

    # Example

    ```python
    import pandas as pd
    from productivity_analytics.plots import pr_open_to_resolve

    pr_open_to_resolve(pr_df, review_df)

    '''

    # Prepare the data specific to this plot
    data = pr_days_to_close(pr_df, review_df)
    bucket_data = data.groupby(pd.Grouper(key="created_at", freq="M")).mean()
    bucket_data = bucket_data.reset_index()

    # Mean days from PR open to merge or close
    astetik.line(bucket_data,
                 'days',
                 'created_at',
                 palette='Reds',
                 x_label='PR Creation Date',
                 y_label='Mean Hours',
                 alpha=1,
                 markersize=0,
                 median_line=True,
                 title='Average Days from PR Open to Merge or Close',
                 sub_title='[ Each Observation is a Monthly Bucket ]')

    plt.show()
