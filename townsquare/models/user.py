from datetime import datetime

class User:
    def __init__(self, username, full_name, team, department, start_date):
        self.username = username
        self.full_name = full_name
        self.team = team
        self.department = department
        self.start_date = self.parse_date(start_date)

    def parse_date(self, start_date):
        return datetime.strptime(start_date, '%Y-%m-%d')
    