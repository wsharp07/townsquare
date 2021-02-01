from datetime import datetime

class FirstPullRequest:
    def __init__(self, full_name, title, url, start_date, pr_date):
        self.full_name = full_name
        self.title = title
        self.url = url
        self.start_date = start_date
        self.pr_date = pr_date
        self.days = self.days_to_pr(start_date, pr_date)

    def days_to_pr(self, start_date, pr_date):
        if (pr_date is None):
            pr_date = datetime.now()
            
        days_since_join = (datetime.now() - start_date).days
        days_since_pr = (datetime.now() - pr_date).days
        days_first_pr = days_since_join - days_since_pr
        return days_first_pr

    