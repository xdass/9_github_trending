import requests
import datetime


def get_trending_repositories(repos, top_size=20):
    return repos[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    link = "https://api.github.com/repos/{}/{}/issues".format(repo_owner, repo_name)
    response = requests.get(link)
    all_issues = response.json()
    return len([issue for issue in all_issues if issue['state'] == 'open'])


def print_repository_info(repositories):
    for repo in repositories:
        repo_issues = get_open_issues_amount(repo['owner']['login'], repo['name'])
        print("""Название: {}\nСсылка: {}\nIssues: {}\n""".format(repo['name'], repo['html_url'], repo_issues))


def get_repositories():
    week_delta = datetime.timedelta(days=7)
    week_ago = datetime.date.today() - week_delta
    params = {'q': 'created:>={}'.format(week_ago), 'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    return response.json()['items']

if __name__ == '__main__':
    repositories_list = get_repositories()
    top_repositories = get_trending_repositories(repositories_list)
    print_repository_info(top_repositories)
