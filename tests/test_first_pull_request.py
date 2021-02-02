import os
import tempfile
import pytest
from datetime import datetime

from townsquare.models.first_pull_request import FirstPullRequest

def test_days_to_pr_user_exists():
    start_date = datetime(2021,1,10)
    pr_date = datetime(2021,1,12)
    fpr = FirstPullRequest('John Doe', 'Pull Request', 'https://test.com', start_date, pr_date)
    assert fpr.days == 2