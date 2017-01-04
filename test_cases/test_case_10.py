from main import *


def run_10():
    touch_file('file_14')
    x = ssh_command()
    x.communicate('rm -rf ' + CLIENT_MOUNTED_DIR + '/file_14\nls -l ' + CLIENT_MOUNTED_DIR + \
                            ' | grep -x file_14')  # rm -rf /mnt/file_14 and ls -l /mnt | grep -x file_14
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
