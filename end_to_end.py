import requests
import json
import sys
import os
import optparse

usage = 'usage: %prog default_branch repository_name:branch_name'
parser = optparse.OptionParser(usage=usage)
parser.add_option('-a', '--all', action='store_true', dest='output_all',
                  help='output the entire response from Integration')
(options, args) = parser.parse_args()

def get_build_params(params):
    """Return a JSON object for the request data or exit the program if invalid
    arguments are given.

    Keyword arguments:
    params -- the parameters to run the Integration build.
    """
    data = {
        'build_parameters': {
            'DEFAULT_BRANCH': params[0]
        }
    }
    for param in params[1:]:
        arr = param.split(':')
        data['build_parameters']['SCALITY_' + arr[0].upper() + \
            '_BRANCH'] = arr[1]
        return json.dumps(data)

def get_response_output(res, output_all):
    """Return the message for a failed or successful request.

    Keyword arguments:
    res -- the response object
    output_all -- option to show entire response from Ultron.
    """
    data = res.text[res.text.find('{'):]
    json_res = json.loads(data)
    if 'message' in json_res:
        return json_res['message']
    if output_all:
        return res
    else:
        return json_res['build_url']

try:
    data = get_build_params(args)
except IndexError:
    sys.exit('Please use the format repository_name:branch_name')

try:
    ci_token = os.environ['CI_TOKEN']
except KeyError:
    sys.exit('Environment variable CI_TOKEN not found.')

# Use the ultron branch, with the default specified by the user.
url = 'http://ci.ironmann.io/api/v1/project/scality/Integration/tree/' + \
    'ultron/' + args[0] + '?circle-token=' + ci_token
headers = {'Content-Type': 'application/json'}
res = requests.post(url, data=data, headers=headers)

sys.exit(get_response_output(res, options.output_all))
