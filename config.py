from prettyconf import config

# absolute path to the supervisord pid file
SUPERVISOR_PID_FILE = config(
    'SUPERVISOR_PID_FILE',
    default='/var/run/supervisord.pid'
)

SENDGRID_APIKEY = config('SENDGRID_APIKEY')
SENDGRID_FROM_EMAIL = config('SENDGRID_FROM_EMAIL')
SENDGRID_FROM_NAME = config('SENDGRID_FROM_NAME')

TO_EMAIL_ADDRESS = config('TO_EMAIL_ADDRESS')
