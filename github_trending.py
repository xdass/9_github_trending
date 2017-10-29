import requests
import datetime


# get template https://api.github.com/search/repositories?q=created:%3E=2017-10-22+language:python&sort=stars&order=desc

def get_trending_repositories(repos, top_size=20):
    return repos[::top_size]


def get_open_issues_amount(repo_owner, repo_name):
    # https://api.github.com/repos/<owner-name>/<repo-name>/issues
    pass


def print_repository_info():
    pass


def get_repositories():
    week_delta = datetime.timedelta(days=7)
    week_ago = datetime.date.today() - week_delta
    params = {'q': 'created:>={}'.format(week_ago), 'sort': 'stars', 'order': 'desc'}
    r = requests.get('https://api.github.com/search/repositories', params=params)
    return r.json()['items']

if __name__ == '__main__':
    repositories_list = get_repositories()
    trending_repos = get_trending_repositories(repositories_list)
    print(repositories_list)
    for repo in repositories_list:
        print(repo['name'])
