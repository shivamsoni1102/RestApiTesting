import requests
from Utilities.Configurations import *

baseUrl = get_config()["API"]["endpoint"]
s = requests.Session()
s.headers = {'Content-Type': 'application/json'}


def make_request(method, resource, query_params=None, headers=None, cookies=None):
    full_url = baseUrl + resource
    if query_params is None:
        response = s.request(method=method, url=full_url, headers=headers, cookies=cookies, verify=False)
    else:
        response = s.request(method=method, url=full_url, json=query_params.__dict__, headers=headers,
                             cookies=cookies, verify=False)
    return response
