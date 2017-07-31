import os
import sys
import config
import elasticemail
from utils import logger_setup

logger = logger_setup(__file__)

try:
    logger.info("Reading pid of supervisord...")
    with open(config.SUPERVISOR_PID_FILE) as f:
        pid = int(f.readline().strip())
except FileNotFoundError as err:
    logger.error("Supervisord PID file not found!")
    sys.exit(-1)

try:
    logger.info("Checking if pid {} is running...".format(pid))
    os.kill(pid, 0)
except ProcessLookupError as err:
    logger.info("Sending email...")
    elasticemail.send(
        to=config.TO_EMAIL_ADDRESS,
        subject="Supervisord is not running!",
        body="Check supervisord! 👀"
    )
else:
    logger.info("Supervisord running normally!")
