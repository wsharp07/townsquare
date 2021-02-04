from datetime import datetime
from sgqlc.endpoint.http import HTTPEndpoint
from townsquare.models.pull_request import PullRequest
import os

class PullRequestRepo:
    url = os.getenv('townsquare_github_url')
    token = os.getenv('townsquare_github_token')
    headers = {'Authorization': f'bearer {token}'}

    def first_pr(self, username, start_date):
        response = self.__deep_query(username, 3, None, start_date)

        if (response['user'] is None):
            return None

        pr = self.__parse_pull_request(response['pull_request'], username)
        
        return pr

    def __parse_user(self, response):
        return response['data']['user']

    def __parse_pull_request(self, pr_node, username):
        return PullRequest(username, pr_node['title'], pr_node['url'], pr_node['createdAt'])

    def __deep_query(self, username, page_size, cursor, after_date):
        endpoint = HTTPEndpoint(self.url, self.headers)

        query = '''
            query($username:String!, $pageSize:Int!, $cursor:String){
                user(login: $username) {
                    pullRequests(first: $pageSize, after:$cursor) {
                        edges {
                            cursor
                            node {
                                title
                                url
                                createdAt
                            }
                        }
                    }
                    createdAt
                }
            }
        '''

        variables = {
            'username': username,
            'pageSize': page_size
        }

        if cursor != None:
            variables['cursor'] = cursor

        response = endpoint(query, variables)

        user = response['data']['user']

        if (user == None):
            return {
                'user': None,
                'pull_request': None
            }

        edges = response['data']['user']['pullRequests']['edges']

        for node in edges:
            date_format = '%Y-%m-%dT%H:%M:%SZ'
            created_at = node['node']['createdAt']
            created_at = datetime.strptime(created_at, date_format)
            if created_at >= after_date:
                return {
                    'user': response['data']['user'],
                    'pull_request': node['node']
                }

        cursor = edges[-1]['cursor']
        return self.__deep_query(username, page_size, cursor, after_date)
        


    def __query(self, username):
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
