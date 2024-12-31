import astetik
import pandas as pd

import matplotlib.pyplot as plt


def pr_request_per_contributor(review_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Plot the total number of Pull Request (PR) change requests per author

    # Parameters

    review_df (pd.DataFrame): PR review data

    # Returns

    pd.DataFrame: The relative share of PR change requests by each contributor

    # Example

    ```python
    import pandas as pd
    from productivity_analytics.plots import pr_request_per_contributor

    pr_request_per_contributor(pr_df)

    '''

    # The section for rendering the plot with absolute values
    abs_data = review_df.loc[review_df['state'] == 'CHANGES_REQUESTED']
    abs_data = pd.DataFrame(abs_data['user_login'].value_counts())

    # Initialize the plot
    astetik.hist(data=abs_data,
                 x='count',
                 bins=len(abs_data),
                 palette='Reds',
                 x_label='Total Number of PR Change Requests',
                 y_label='Number of Observations',
                 title='How Many PR Change Requests Are Each Contributor Making?',
                 sub_title='[ Absolute Values ]')

    # Show the plot if not in a notebook
    plt.show()

    # The section for rendering the table with relative values
    rel_data = review_df.loc[review_df['state'] == 'CHANGES_REQUESTED']
    rel_data = rel_data['user_login'].value_counts() / len(rel_data) * 100
    rel_data = pd.DataFrame(rel_data).round(2)
    rel_data.columns = ['Percentage of All Change Requests']

    return rel_data
