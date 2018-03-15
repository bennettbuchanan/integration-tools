import requests
import sys
import optparse
from util import *

usage = 'usage: %prog default_branch repository_name:branch_name'
parser = optparse.OptionParser(usage=usage)
parser.add_option('-a', '--all', action='store_true', dest='output_all',
                  help='output the entire response from Integration')
(options, args) = parser.parse_args()

data = get_build_params(args)
ci_token = get_ci_token();

# Use the ultron branch, with the default specified by the user.
url = 'http://ci.ironmann.io/api/v1/project/scality/Integration/tree/' + \
    'ultron/' + args[0] + '?circle-token=' + ci_token
headers = {'Content-Type': 'application/json'}
res = requests.post(url, data=data, headers=headers)

sys.exit(get_response_output(res, options.output_all))
