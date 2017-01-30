# Integration tools

Run an end-to-end test from the command line with Scality's Integration.

`python end_to_end.py default_branch repository_name:branch_name`

You may specify as many `repository_name:branch_name` positional arguments as
you need.

Set your CI token (found [here](http://ci.ironmann.io/account/api)): `export CI_TOKEN=your_token`

Dependencies: `pip install requests`
