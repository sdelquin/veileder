import os
import sys

import config
from utils import logger_setup
from sgw.core import SendGrid

logger = logger_setup(__file__)


def notify():
    email = SendGrid(
        config.SENDGRID_APIKEY,
        config.SENDGRID_FROM_EMAIL,
        config.SENDGRID_FROM_NAME
    )
    email.send(
        to=config.TO_EMAIL_ADDRESS,
        subject='Supervisord is not running!',
        msg='Check supervisord! 💪🏻'
    )


try:
    logger.info("Reading pid of supervisord...")
    with open(config.SUPERVISOR_PID_FILE) as f:
        pid = int(f.readline().strip())
except FileNotFoundError as err:
    logger.error("Supervisord PID file not found!")
    logger.info("Sending email...")
    notify()
    sys.exit(-1)

try:
    logger.info("Checking if pid {} is running...".format(pid))
    os.kill(pid, 0)
except ProcessLookupError as err:
    logger.error("Supervisord PID not found!")
    logger.info("Sending email...")
    notify()
else:
    logger.info("Supervisord running normally!")
