import json
from townsquare.repos.pull_request_repo import PullRequestRepo
from townsquare.models.user import User
from townsquare.models.first_pull_request import FirstPullRequest

class Scoreboard:

    def parse_file(self):
        with open('townsquare/data.json') as f:
            data = json.load(f)
            return data

    def create_user(self, record):
        username = record['username']
        full_name = record['fullName']
        team = record['team']
        department = record['department']
        start_date = record['startDate']
        return User(username,full_name,team,department,start_date)

    def query_first_pr(self, user):
        repo = PullRequestRepo()
        return repo.first_pr(user.username)

    def create_model(self, user, first_pr):
        if (first_pr is None):
            return FirstPullRequest(user.full_name, None, '#', user.start_date, None)
        else:
            return FirstPullRequest(user.full_name, first_pr.title, first_pr.url, user.start_date, first_pr.pr_date)

    def generate(self):
        data = self.parse_file()
        model = []

        for record in data:
            user = self.create_user(record)
            first_pr = self.query_first_pr(user)
            first_pr_model = self.create_model(user, first_pr)
            model.append(first_pr_model)

        return model