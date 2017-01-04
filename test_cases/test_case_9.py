from main import *


def run_9():
    x = ssh_command()
    x.communicate('echo "echo "Hi again"" > ' + CLIENT_MOUNTED_DIR + '/file_13')    # echo "echo \"Hi again\"" > /mnt/file_13
    _ = call(['sh', SERVER_SHARED_DIR + '/file_13'], stdout=PIPE, stderr=PIPE)
    if _ != 0:
        logger.info(MESSAGE_FAILED)
        logger.debug(MESSAGE_NO_FILE + MESSAGE_CANT_EXECUTE)
        check_bug()
    else:
        logger.info(MESSAGE_PASSED)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)
