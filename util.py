import sys
import os
import json

def get_ci_token():
    """Return the CI token from the envinment variable CI_TOKEN."""
    try:
        ci_token = os.environ['CI_TOKEN']
    except KeyError:
        sys.exit('Environment variable CI_TOKEN not found.')
    return ci_token

def get_build_params(params):
    """Return a JSON object for the request data or exit the program if invalid
    arguments are given.

    Keyword arguments:
    params -- the parameters to run the Integration build.
    """
    try:
        data = {
            'build_parameters': {
                'DEFAULT_BRANCH': params[0]
            }
        }
        for param in params[1:]:
            arr = param.split(':')
            data['build_parameters']['SCALITY_' + arr[0].upper() + \
                '_BRANCH'] = arr[1]
    except IndexError:
        sys.exit('Please use the format repository_name:branch_name')
    return json.dumps(data)
        

def get_response_output(res, output_all=None):
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