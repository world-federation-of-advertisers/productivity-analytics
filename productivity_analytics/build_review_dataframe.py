from typing import List, Optional

import pandas as pd

from tqdm import tqdm

from .get_review_data import get_review_data


def build_review_dataframe(pr_numbers: List[int],
                           repo_owner: str,
                           repo_name: str,
                           token: str,
                           save_to_file: Optional[str] = None) -> pd.DataFrame:

    '''
    Build a DataFrame containing selected review data
    for a list of pull requests.

    # Parameters

    pr_numbers (list): A list of pull request numbers.
    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.
    save_to_file (str): File path to save the DataFrame as a CSV file (or None).

    # Returns

    DataFrame: A DataFrame containing selected review data for the
    specified pull requests.

    # Example

    ```python
    pr_numbers = [1, 2, 3]
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    build_pr_reviews(pr_numbers, repo_owner, repo_name, token, save_to_file="pr_data.csv")

    '''

    all_prs_data = []

    for pr_number in tqdm(pr_numbers):

        # Get all the reviews for the PR
        single_pr_data = get_review_data(pr_number,
                                         repo_owner,
                                         repo_name,
                                         token)

        # Extract the relevant data points for each individual review
        for review in single_pr_data:

            all_prs_data.append([pr_number,
                                 review['user']['login'],
                                 review['submitted_at'],
                                 review['state']])
    
    review_df = pd.DataFrame(all_prs_data)
    review_df.columns = ['number',
                         'user_login',
                         'created_at',
                         'state']

    # Save the DataFrame to a CSV file if save_to_file is not None
    if save_to_file is not None:
        review_df.to_csv(save_to_file, index=False)

    return review_df
