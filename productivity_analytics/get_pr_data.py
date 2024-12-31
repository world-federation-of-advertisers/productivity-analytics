import requests


def get_pr_data(pr_number: int,
                repo_owner: str,
                repo_name: str,
                token: str) -> dict:

    '''
    Fetch detailed data for a specific pull request based on a PR number.

    # Parameters

    pr_number (int): Pull request number.
    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.

    # Returns

    dict: Detailed data for the specified pull request.

    # Example

    ```python
    pr_number = 1
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    pr_data = get_pr_data(pr_number, repo_owner, repo_name, token)

    '''

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        print(f"Failed to fetch PR data (Status Code: {response.status_code})")
        return None
