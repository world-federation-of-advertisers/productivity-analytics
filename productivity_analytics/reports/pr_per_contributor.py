import astetik
import pandas as pd

import matplotlib.pyplot as plt


def pr_per_contributor(pr_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Plot the total number of Pull Requests (PRs) opened by each contributor.

    # Parameters

    pr_df (pd.DataFrame): PR data

    # Returns

    pd.DataFrame: The relative share of PRs opened by each contributor

    # Example

    ```python
    import pandas as pd
    from productivity_analytics.plots import pr_per_contributor

    pr_iterations_per_author(pr_df)

    '''

    # A distribution of the total number of PRs opened by each contributor
    pr_open_data = pd.DataFrame(pr_df['user_login'].value_counts())
    astetik.hist(data=pr_open_data,
                 x='count',
                 bins=len(pr_open_data),
                 palette='Reds',
                 x_label='Number of Opened PRs',
                 y_label='Number of Contributors',
                 title='How Many PRs are Each Contributor Opening?',
                 sub_title='[ Absolute Values ]')
    
    plt.show()

    # Relative share of PRs opened by each contributor
    opening_relative_data = pd.DataFrame((pr_df['user_login'].value_counts() / len(pr_df) * 100).round(2))
    opening_relative_data.columns = ['Percentage of All PRs']
    
    return opening_relative_data
