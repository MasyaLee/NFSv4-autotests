from main import *


def run_8():
    x = ssh_command()
    x.communicate('touch /file_12\ncp /file_12 ' + CLIENT_MOUNTED_DIR)  # touch /file_12 and mv /file_12 /mnt
    _ = cat_server_file('/file_12')     # _ = call(['cat', SERVER_SHARED_DIR + '/file_12'])
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
