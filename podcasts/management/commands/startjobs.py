#standard library
import logging

#Django
from django.conf import settings
from django.core.management.base import BaseCommand

#Third Party
import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

# Models
from podcasts.models import Episode, Content


logger = logging.getLogger(__name__)
def save_new_episodes(theme,feed, filled):
    for item in feed.entries:
        if not theme.objects.filter(guid=item.guid).exists():
            filled = theme(
                title=item.title,
                pub_date=parser.parse(item.published),
                link=item.link,
                guid=item.guid,
            )
            filled.save()

def fetch_content(theme,info,filled):
    feed = feedparser.parse(info)
    save_new_episodes(theme,feed,filled)


def fetch_nairaland_content():
    fetch_content(Content,"https://www.nairaland.com/feed","content")


    
def fetch_vanguard_contents():
    fetch_content(Episode,"https://www.vanguardngr.com/feed","episode")
    
def delete_old_job_executions(max_age = 604_800):
    """Deletes all apscheduler job execution logs older than `max_age`."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)  

class Command(BaseCommand):
    help = "Runs Apscheduler."

    def handle(self,*args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_vanguard_contents,
            trigger="interval",
            minutes=0.5,
            id="Vanguard",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Vanguard Headlines.")

        scheduler.add_job(
            fetch_nairaland_content,
            trigger="interval",
            minutes=0.5,
            id="Nairaland",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: Nairaland Headlines.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete Old Job Executions.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")


 
