from typing import List, Optional

import pandas as pd

from tqdm import tqdm

from .get_pr_data import get_pr_data


def build_pr_dataframe(pr_numbers: List[int],
                       repo_owner: str,
                       repo_name: str,
                       token: str,
                       save_to_file: Optional[str] = None) -> pd.DataFrame:

    '''
    Build a DataFrame containing selected data for a list of pull requests.

    # Parameters

    pr_numbers (list): A list of pull request numbers.
    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.
    save_to_file (str): File path to save the DataFrame as a CSV file (or None).

    # Returns

    DataFrame: A DataFrame containing selected data for the specified pull requests.

    # Example

    ```python
    pr_numbers = [1, 2, 3]
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    build_pr_dataframe(pr_numbers, repo_owner, repo_name, token, save_to_file="pr_data.csv")

    '''

    all_prs_data = []

    for pr_number in tqdm(pr_numbers):

        # Get the JSON data for the PR
        single_pr_data = get_pr_data(pr_number, repo_owner, repo_name, token)

        # Extract the relevant data points for each PR
        pr_meta = [single_pr_data['id'],
                   single_pr_data['number'],
                   single_pr_data['html_url'],
                   single_pr_data['state'],
                   single_pr_data['merged'],
                   single_pr_data['title'],
                   single_pr_data['user']['login'],
                   single_pr_data['user']['id'],
                   single_pr_data['body'],
                   single_pr_data['created_at'],
                   single_pr_data['closed_at'],
                   single_pr_data['merged_at'],
                   single_pr_data['comments'],
                   single_pr_data['review_comments'],
                   single_pr_data['base']['repo']['name'],
                   single_pr_data['commits'],
                   single_pr_data['additions'],
                   single_pr_data['deletions'],
                   single_pr_data['changed_files']]

        all_prs_data.append(pr_meta)

    # Convert the list of lists into a DataFrame
    pr_df = pd.DataFrame(all_prs_data)

    # Make sure these columns exactly match of pr_meta above
    pr_df.columns = ['id',
                     'number',
                     'html_url',
                     'state',
                     'merged',
                     'title',
                     'user_login',
                     'user_id',
                     'body',
                     'created_at',
                     'closed_at',
                     'merged_at',
                     'comments',
                     'review_comments',
                     'base_repo_name',
                     'commits',
                     'additions',
                     'deletions',
                     'changed_files']

    # Convert the created_at, closed_at, and merged_at columns to datetime
    pr_df['created_at'] = pd.to_datetime(pr_df['created_at'])
    pr_df['closed_at'] = pd.to_datetime(pr_df['closed_at'])
    pr_df['merged_at'] = pd.to_datetime(pr_df['merged_at'])

    # Save the DataFrame to a CSV file
    if save_to_file is not None:
        pr_df.to_csv(save_to_file, index=False)

    return pr_df
