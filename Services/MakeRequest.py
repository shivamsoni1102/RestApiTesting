import requests
from Utilities.Configurations import *

baseUrl = get_config()["API"]["endpoint"]
s = requests.Session()
s.headers = {'Content-Type': 'application/json'}


def make_request(method, resource, query_params, headers=None, path_variable=None):
    full_url = baseUrl + resource
    if path_variable is not None:
        full_url = full_url + "/" + path_variable

    response = s.request(method=method, url=full_url, json=query_params.__dict__, headers=headers, verify=False)
    return response