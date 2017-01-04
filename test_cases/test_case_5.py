from main import *


def run_5():
    touch_file('file_8')
    x = ssh_command()
    x.communicate('cp ' + CLIENT_MOUNTED_DIR + '/file_8 /\nls -l / | grep file_8')   # cp /mnt/file_8 / and ls -l / |grep file_8
    if x.returncode != 0:
        logger.info(MESSAGE_FAILED)
        logger.debug(MESSAGE_NO_COPY)
        check_bug()
    else:
        logger.info(MESSAGE_PASSED)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)
