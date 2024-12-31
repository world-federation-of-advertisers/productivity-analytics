import requests


def get_review_data(pr_number: int,
                    repo_owner: str,
                    repo_name: str,
                    token: str) -> dict:
    
    '''
    Fetch review metadata for a pull request with pagination.

    # Parameters:

    pr_number (int): Pull request number.
    repo_owner (str): The organization or user that owns the repository.
    repo_name (str): Name of the repository.
    token (str): GitHub access token.

    # Returns

    list: A list of review metadata.

    # Example

    ```python
    pr_number = 1
    repo_owner = "octocat"
    repo_name = "Hello-World"
    token = "YOUR_GITHUB_TOKEN"

    '''

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/reviews"
    headers = {"Authorization": f"Bearer {token}"}

    reviews = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code == 200:
            data = response.json()
            if not data:  # Exit if no more data
                break
            reviews.extend(data)
            page += 1
        else:
            print(f"Failed to fetch review metadata (Status Code: {response.status_code})")
            break

    return reviews
