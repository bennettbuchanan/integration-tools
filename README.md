# Integration tools

## Using

Set your CI token (found [here](http://ci.ironmann.io/account/api)): `export CI_TOKEN=your_token`

Dependencies:
* `pip install requests`
* `pip install python-crontab`

Run an end-to-end test from the command line with Scality's Integration:

### Cron job for finding flaky tests

Set a cron job to run integration tasks (by default, every hour and 45 minutes):

`python scheduler.py`

This will output a list of builds to a file `flaky_test_finder_builds` in the
same directory as `flaky_test_finder.py`.

### Simple script for running an end-to-end build from the command line

`python end_to_end.py default_branch repository_name:branch_name`

You may specify as many `repository_name:branch_name` positional arguments as
you need. The end-to-end test will use what you set as your `default_branch`,
for the Ultron branch (e.g., ultron/default_branch).