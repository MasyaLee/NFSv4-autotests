from main import *


def run_4():
    _ = open('file_7', 'w')
    call(['echo', 'echo', '\"Hi', 'there\"'], stdout=_)
    x = ssh_command()
    x.communicate('sh ' + CLIENT_MOUNTED_DIR + '/file_7')
    if x.returncode != 0:
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


