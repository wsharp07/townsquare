import os
import tempfile
import pytest
from datetime import datetime

from townsquare.models.user import User
from townsquare.models.pull_request import PullRequest
from townsquare.services.scoreboard import Scoreboard

def test_create_user():
    username = "jdoe"
    full_name = "John Doe"
    team = "Ace of Spades"
    department = "Marketing"

    record = {
        "username": username,
        "fullName": full_name,
        "team": team,
        "department": department,
        "startDate": "2021-01-21"
    }
    user = Scoreboard().create_user(record)
    assert user.full_name is full_name
    assert user.department is department
    assert user.username is username
    assert user.team is team

def test_create_model_user_exists():
    username = 'jdoe'
    full_name = 'John Doe'
    url = 'https://github.com/jdoe/pulls/1'
    user = User(username, full_name, 'Ace of Spades', 'Marketing', '2021-01-01')
    pr = PullRequest(username, 'Pull Request', url, '2021-01-29T01:34:09Z')
    model = Scoreboard().create_model(user, pr)
    assert model.full_name is full_name
    assert model.title is 'Pull Request'
    assert model.url is url

def test_create_model_no_user():
    username = 'jdoe'
    full_name = 'John Doe'
    user = User(username, full_name, 'Ace of Spades', 'Marketing', '2021-01-01')
    model = Scoreboard().create_model(user, None)
    assert model is not None
    assert model.pr_date is None
    assert model.days > 0