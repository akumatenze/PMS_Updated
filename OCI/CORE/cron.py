# myapp/cron.py

from django_cron import CronJobBase, Schedule # type: ignore
from datetime import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # run every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.my_cron_job'    # a unique code

    def do(self):
        # Your task logic here
        print("Cron job executed at", datetime.now())


