from datetime import datetime

class FirstPullRequest:
    def __init__(self, user, title, url, start_date, pr_date):
        self.user = user
        self.title = title
        self.url = url
        self.start_date = start_date
        self.pr_date = pr_date
        self.has_pr = True if self.pr_date != None else False
        self.days = self.days_to_pr(start_date, pr_date, self.has_pr)

    def days_to_pr(self, start_date, pr_date, has_pr):
        if (has_pr == False):
            pr_date = datetime.now()
            
        days_since_join = (datetime.now() - start_date).days
        days_since_pr = (datetime.now() - pr_date).days
        days_first_pr = days_since_join - days_since_pr

        return days_first_pr * -1 if has_pr == False else days_first_pr

    