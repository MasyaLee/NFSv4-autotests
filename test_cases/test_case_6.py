from main import *


def run_6():
    x = ssh_command()
    x.communicate(touch_server_file('/file_9'))
    _ = cat_server_file('/file_9')  # _ = call(['cat', SERVER_SHARED_DIR + '/file_9'])
    if _ != 0:
        logger.info(MESSAGE_FAILED)
        logger.debug(MESSAGE_NO_FILE)
        check_bug()
    else:
        logger.info(MESSAGE_PASSED)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)

