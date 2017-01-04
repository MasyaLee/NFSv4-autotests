from main import *


def run_2():
    rm_file('file_1')
    x = ssh_command()
    x.communicate('ls ' + CLIENT_MOUNTED_DIR + ' | grep -x file_1')
    if x.returncode == 0:
        logger.info(MESSAGE_FAILED)
        logger.debug(MESSAGE_ISNOT_DELETED)
        check_bug()
    else:
        logger.info(MESSAGE_PASSED)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)
