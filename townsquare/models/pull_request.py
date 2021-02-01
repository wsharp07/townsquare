from datetime import datetime

class PullRequest:

    def __init__(self, username, title, url, pr_date):
        self.username = username
        self.title = title
        self.url = url
        self.pr_date = self.parse_date(pr_date)

    def parse_date(self, pr_date):
        date_format = '%Y-%m-%dT%H:%M:%SZ'
        return datetime.strptime(pr_date, date_format)