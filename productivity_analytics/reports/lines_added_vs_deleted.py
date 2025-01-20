import pandas as pd


def lines_added_vs_deleted(pr_df: pd.DataFrame) -> pd.DataFrame:

    '''Display lines added vs deleted per author.

    # Parameters

    pr_df (pd.DataFrame): PR data

    # Returns

    pd.DataFrame: Lines added vs deleted per author

    # Example

    ```python
    import pandas as pd

    from productivity_analytics import get_pr_numbers
    from productivity_analytics import build_pr_dataframe
    from productivity_analytics import lines_added_vs_deleted

    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    pr_numbers = get_pr_numbers(repo_owner, repo_name, token)

    pr_df = build_pr_dataframe(pr_numbers, repo_owner, repo_name, token)

    lines_added_vs_deleted(pr_df)
    '''
    
    # Count the number of PRs per author
    total_prs = pr_df.groupby('user_login')['user_login'].size()

    # Count the number of total additions per author
    total_lines_added = pr_df.groupby('user_login')['additions'].sum()

    # Count the number of total deletions per author
    total_lines_deleted = pr_df.groupby('user_login')['deletions'].sum()

    # Combine the three above created tables into one
    lines_by_author = pd.concat([total_prs, total_lines_added, total_lines_deleted], axis=1)

    # Rename the columns
    lines_by_author.columns = ['total_prs', 'total_lines_added', 'total_lines_deleted']

    # Create a new column for additions MINUS deletions delta
    lines_by_author['total_delta'] = lines_by_author['total_lines_added'] - lines_by_author['total_lines_deleted']

    # Sort to highest delta on top
    lines_by_author = lines_by_author.sort_values(by='total_delta', ascending=False)

    return lines_by_author
