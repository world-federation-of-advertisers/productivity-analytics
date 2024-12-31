import pandas as pd

from .get_pr_numbers import get_pr_numbers
from .build_pr_dataframe import build_pr_dataframe


def update_pr_data(repo_owner: str,
                   repo_name: str,
                   token: str,
                   path_to_data: str = '../data/pr_data.csv',
                   save_to_file: bool = True) -> pd.DataFrame:
    
    '''
    Update the saved PR data for a repository.
    
    # Parameters
    
    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.
    path_to_data (str): File path to the saved review data.
    save_to_file (bool): Save the updated data to the file.

    NOTE: If save_to_file is set to True, the data will be saved
    based on the path_to_data parameter.

    # Returns

    DataFrame: A DataFrame containing the updated PR data.

    # Example

    ```python
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    update_review_data(repo_owner, repo_name, token, save_to_file=True)
    
    '''

    # Load the current data
    pr_df = pd.read_csv(path_to_data)

    # Compare the PR numbers already in data with the new
    new_pr_numbers = get_pr_numbers(repo_owner, repo_name, token)
    old_pr_numbers = pr_df['number'].tolist()
    pr_numbers = list(set(new_pr_numbers).difference(old_pr_numbers))

    if len(pr_numbers) > 0:

        # Build the new data frame
        new_pr_df = build_pr_dataframe(pr_numbers, repo_owner, repo_name, token)
    
        pr_df = pd.concat([new_pr_df, pr_df], ignore_index=True)
    
        if save_to_file is True:
            pr_df.to_csv(path_to_data, index=False)

    return pr_df
