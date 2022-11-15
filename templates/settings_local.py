# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{django_secret_key}}'

ALLOWED_HOSTS = [ '{{domain}}', '{{download_domain}}' ]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# BuildingTimeout in seconds, will stop the build if no output from build script arrives within that time
BUILDING_TIMEOUT = 600

SHOW_NUMBER_OF_FINISHED_JOBS = 50

EMAIL_FROM_ADDRESS = "build.robot@{{domain}}"
EMAIL_SERVER = "{{pac}}.hostsharing.net"
EMAIL_PORT = 587
EMAIL_USER = "{{pac}}-{{user}}"
EMAIL_PASSWORD = "{{password}}"

SEND_EMAIL_ON_SUCCESS = False
DELETE_LOG_AFTER_DAYS = 20
KEEP_MINIMUM_LOGS = 5
DISPLAY_MAX_BUILDS_PER_PACKAGE = 15
MAX_DEBUG_LEVEL = 1

DELETE_PACKAGES_AFTER_DAYS = 4
KEEP_MINIMUM_PACKAGES = 4

GIT_SRC_PATH = "/home/pacs/{{pac}}/users/{{user}}/var/src"
LOGS_PATH = "/home/pacs/{{pac}}/users/{{user}}/var/logs"
REPOS_PATH = "/home/pacs/{{pac}}/users/{{user}}/var/repos"
TARBALLS_PATH = "/home/pacs/{{pac}}/users/{{user}}/var/tarballs"
SSH_TMP_PATH = "/home/pacs/{{pac}}/users/{{user}}/var/ssh"

STATIC_ROOT="/home/pacs/{{pac}}/users/{{user}}/static"

PUBLIC_KEY_SERVER = "keyserver.ubuntu.com"

LBS_URL = "https://{{domain}}"
DOWNLOAD_URL = "https://{{download_domain}}"

TIME_ZONE = 'Europe/Amsterdam'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{pac}}_{{user}}',
        'USER': '{{pac}}_{{user}}',
        'PASSWORD': '{{password}}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
