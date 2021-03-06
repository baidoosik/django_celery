from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_sched.settings')

app = Celery('movie_sched')

# using a string here means the worker don't have to serialize
# the configuration object to child process.
app.config_from_object('django.conf:settings', namespace='CELERY')

#load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ['REDIS_URL'])

app.conf.beat_schedule ={
    'get_ocn_schedule': {
        'task': 'scheduler_core.tasks.startup_news_crawling',
        'schedule': crontab(minute='5,10,15,20'),
        # 'args': ("OCN", "http://ocn.tving.com/ocn/schedule?startDate="),
    }

}

#set timezone for kst
app.conf.timezone ='Asia/Seoul'

