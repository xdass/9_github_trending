import requests
import datetime


def get_open_issues_amount(repo_owner, repo_name):
    link = "https://api.github.com/repos/{}/{}/issues".format(
        repo_owner,
        repo_name)
    response = requests.get(link)
    all_issues = response.json()
    return len([issue for issue in all_issues if issue['state'] == 'open'])


def print_repositories_info(repositories):
    for repo_info in repositories:
        for item_label, item_value in repo_info.items():
            print(item_label, item_value)


def get_repositories_detail_info(repositories):
    detail_info = []
    for repo in repositories:
        issues = get_open_issues_amount(repo['owner']['login'], repo['name'])
        detail_info.append(
            {
                'Название': repo['name'],
                'Ссылка: ': repo['html_url'],
                'Issues: ': issues
            })
    return detail_info


def get_top_repositories(top_size=20):
    week_delta = datetime.timedelta(days=7)
    week_ago = datetime.date.today() - week_delta
    params = {'q': 'created:>={}'.format(
        week_ago),
        'sort': 'stars',
        'order': 'desc'
    }
    response = requests.get('https://api.github.com/search/repositories',
                            params=params)
    return response.json()['items'][:top_size]


if __name__ == '__main__':
    repositories_top_list = get_top_repositories()
    repositories_detail_info = get_repositories_detail_info(repositories_top_list)
    print_repositories_info(repositories_detail_info)
