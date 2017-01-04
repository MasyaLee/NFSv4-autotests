from main import *


def run_1():
    touch_file('file_4')
    x = ssh_command()
    x.communicate(cat_file('/file_4'))      # x.communicate('cat ' + CLIENT_MOUNTED_DIR + '/file_4\n')
    if x.returncode != 0:
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


