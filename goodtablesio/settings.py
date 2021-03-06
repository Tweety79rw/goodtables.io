import os
import logging
from logging.handlers import SysLogHandler
from dotenv import load_dotenv
load_dotenv('.env')


# Logging

logging.basicConfig(level=logging.DEBUG)
if os.environ.get('LOGGING_URL', None):
    root_logger = logging.getLogger()
    host, port = os.environ['LOGGING_URL'].split(':')
    syslog_handler = SysLogHandler(address=(host, int(port)))
    syslog_handler.setLevel(logging.INFO)
    root_logger.addHandler(syslog_handler)
log = logging.getLogger(__name__)

# General

BASE_URL = os.environ['BASE_URL']
DEBUG = os.environ.get('FLASK_DEBUG', False)
GTIO_SECRET_KEY = os.environ['GTIO_SECRET_KEY']
GLOB_EXCLUDED_FORMATS = ['json', 'sql']
GOOGLE_ANALYTICS_CODE = os.environ.get('GOOGLE_ANALYTICS_CODE')
MAX_TABLES_PER_SOURCE = 100

# Flask

FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

# Database

JOBS_LIMIT_FOR_FIND_QUERY = 100
if not os.environ.get('TESTING'):
    log.debug('Not testing mode')
    DATABASE_URL = os.environ['DATABASE_URL']
else:
    log.debug('Testing mode')
    DATABASE_URL = os.environ['TEST_DATABASE_URL']

# Celery

broker_url = os.environ['BROKER_URL']
result_backend = os.environ['RESULT_BACKEND']
task_default_queue = 'default'
task_serializer = 'json'
result_serializer = 'json'
timezone = 'Europe/London'
enable_utc = True

# GitHub

GITHUB_API_BASE = 'https://api.github.com'
GITHUB_API_TOKEN = os.environ['GITHUB_API_TOKEN']
GITHUB_HOOK_SECRET = os.environ['GITHUB_HOOK_SECRET']

# S3

S3_GT_ACCESS_KEY_ID = os.environ['S3_GT_ACCESS_KEY_ID']
S3_GT_SECRET_ACCESS_KEY = os.environ['S3_GT_SECRET_ACCESS_KEY']
S3_GT_AWS_REGION = os.environ['S3_GT_AWS_REGION']
S3_GT_ACCOUNT_ID = os.environ['S3_GT_ACCOUNT_ID']
S3_LAMBDA_ARN = os.environ['S3_LAMBDA_ARN']
S3_LAMBDA_HOOK_SECRET = os.environ['S3_LAMBDA_HOOK_SECRET']

# OAuth

GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
GITHUB_OAUTH_SCOPES = [
    # See Travis scopes:
    # https://github.com/travis-ci/travis-web/blob/master/mirage/api-spec.js
    # Changes compared to Travis:
    # - `repo_deployment` is removed
    # - `write:repo_hook` changes to `admin:repo_hook` (TODO: sync with Travis here?)
    'read:org',
    'user:email',
    'repo:status',
    'admin:repo_hook',
]

# Sentry

SENTRY_DSN = os.environ.get('SENTRY_DSN')

# Plans
MAX_S3_BUCKETS_ON_FREE_PLAN = 2
