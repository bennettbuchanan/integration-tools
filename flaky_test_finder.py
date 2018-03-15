import sys
import requests
from util import *

default_branch = 'master'
data = get_build_params([default_branch, 'integration:master'])
ci_token = get_ci_token();

# Use the ultron branch, with the default specified by the user.
url = 'http://ci.ironmann.io/api/v1/project/scality/Integration/tree/' + \
    'ultron/' + default_branch + '?circle-token=' + ci_token
headers = {'Content-Type': 'application/json'}
res = requests.post(url, data=data, headers=headers)

file = open('flaky_test_finder_builds', 'a')
file.write(get_response_output(res) + '\n')
file.close()

sys.exit()