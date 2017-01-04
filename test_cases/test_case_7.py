from main import *


def run_7():
    x = ssh_command()
    x.communicate(touch_server_file('/file_10') + '\nmv ' + CLIENT_MOUNTED_DIR + '/file_10 '\
                + CLIENT_MOUNTED_DIR + '/file_11')  # touch /mnt/file_10 and mv /mnt/file_10 /mnt/file_11
    _ = cat_server_file('/file_11')     # _ = call(['cat', SERVER_SHARED_DIR + '/file_11'])
    if _ != 0:
        logger.info(MESSAGE_FAILED)
        logger.debug(MESSAGE_NO_FILE + MESSAGE_CANT_RENAME)
        check_bug()
    else:
        logger.info(MESSAGE_PASSED)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)

