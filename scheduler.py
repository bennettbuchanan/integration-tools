import os
from crontab import CronTab

cron = CronTab(user='bennettbuchanan')
job = cron.new(command='python ' + os.getcwd() + '/flaky_test_finder.py')
job.minute.every(105)
cron.write()