# Standard
from os import environ
from dotenv import load_dotenv

# Celery
from celery import Celery

# Load environment variables
load_dotenv()
REDIS = environ.get('REDIS_URL')

# Celery instance
app = Celery(
    'project', 
    broker=REDIS,
    backend=REDIS,
    include=['project.tasks']
)


if __name__ == '__main__':

    app.start()