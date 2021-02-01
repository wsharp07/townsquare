from datetime import datetime
from sgqlc.endpoint.http import HTTPEndpoint
from townsquare.models.pull_request import PullRequest
import os

class PullRequestRepo:
    url = 'https://api.github.com/graphql'
    token = os.getenv('townsquare_github_token')
    headers = {'Authorization': f'bearer {token}'}

    def first_pr(self, username):
        data = self.query(username)

        user = data['data']['user']

        if (user is None):
            return None

        pr_node = user['pullRequests']['nodes'][0]
        pr = PullRequest(username, pr_node['title'], pr_node['url'], pr_node['createdAt'])
        
        return pr

    def query(self, username):
        endpoint = HTTPEndpoint(self.url, self.headers)
        
        query = '''
            query ($username:String!) { 
                user(login:$username) { 
                    pullRequests(first:1){
                        nodes{
                            title,
                            url,
                            createdAt
                        }
                    }
                    createdAt
                }
            }
            '''

        variables = {'username': username}
        return endpoint(query, variables)
