import astetik
import pandas as pd

import matplotlib.pyplot as plt


def pr_iterations_per_author(pr_df: pd.DataFrame,
                             review_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Plot the mean number of back and forths with the PR author
    required to merge a PR.

    # Parameters

    pr_df (pd.DataFrame): PR data
    review_df (pd.DataFrame): PR review data

    # Returns

    None

    # Example

    ```python
    import pandas as pd
    from productivity_analytics.plots import pr_iterations_per_author

    pr_iterations_per_author(pr_df, review_df)

    '''

    # Prepare the data specific to this plot
    out = []

    for number in pr_df['number']:

        if pr_df.loc[pr_df['number'] == number]['state'].values != 'open':

            pr_reviews = review_df.loc[review_df['number'] == number]
            pr_author = pr_df.loc[pr_df['number'] == number]['user_login'].iloc[0]
            back_and_forths = len(pr_reviews.loc[pr_reviews['user_login'] == pr_author])

            out.append([pr_author, back_and_forths])

    author_iterations_data = pd.DataFrame(out)
    author_iterations_data.columns = ['user_login', 'count']

    # Number of back and forths with the PR author required to merge a PR
    astetik.hist(data=author_iterations_data,
                 x='count',
                 bins=30,
                 palette='Reds',
                 x_label='Number of Back and Forths',
                 y_label='Number of Contributors',
                 title='How many back and forths with the PR author does it require to merge a PR?',
                 sub_title='[ Absolute Values ]')

    plt.show()

    # Average number of back and forths with the PR author required to merge a PR
    author_iterations_data = author_iterations_data.groupby('user_login').mean()
    return author_iterations_data.sort_values('count', ascending=False)
