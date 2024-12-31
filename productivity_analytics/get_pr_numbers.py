import requests


def get_pr_numbers(repo_owner: str,
                   repo_name: str,
                   token: str) -> list:

    '''
    Get all PR numbers for a repository.

    # Parameters

    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.

    # Returns

    list: A list of all PR numbers.

    # Example

    ```python
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    pr_numbers = get_pr_numbers(repo_owner, repo_name, token)

    '''

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    pr_numbers = []
    page = 1

    while True:

        response = requests.get(url,
                                headers=headers,
                                params={"state": "all",
                                        "page": page,
                                        "per_page": 100})

        if response.status_code == 200:
            prs = response.json()

            if not prs:
                break

            pr_numbers.extend(pr['number'] for pr in prs)
            page += 1

        else:
            print(f"Failed to fetch PRs (Status Code: {response.status_code})")
            break

    return pr_numbers
