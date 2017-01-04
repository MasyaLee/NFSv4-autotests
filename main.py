from subprocess import *
import os
from constant_for_test import *
from test_cases import *
import logging

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
filehandler = logging.FileHandler(SERVER_SHARED_DIR + '/logger.log')
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)


def change_precondition():
    _ = open('/etc/exports', 'w')
    call(['echo', '/share', '*(rw,sync)'], stdout=_)


def touch_file(path):
    command = call(['touch ' + path], shell=True)
    return command


def rm_file(path):
    command = call(['rm -f ' + path], shell=True)
    return command


def cat_file(path):
    command = ('cat ' + CLIENT_MOUNTED_DIR + path)
    return command


def ssh_command():
    command = Popen(['ssh', '-T', CLIENT_WAY], stdin=PIPE, stdout=PIPE)
    return command


def cat_server_file(path):
    command = call(['cat', SERVER_SHARED_DIR + path])
    return command


def touch_server_file(path):
    command = 'touch ' + CLIENT_MOUNTED_DIR + path
    return command


def check_bug():
    _ = open('syslog.log', 'w')
    call(['lsmod'], stdout=_)
    call(['df', '-lh'], stdout=_)
    call(['netstat', '-ln'], stdout=_)


def start_cases():
    test_case_1.run_1()
    test_case_2.run_2()
    test_case_3.run_3()
    test_case_4.run_4()
    test_case_5.run_5()
    # change_precondition()
    test_case_6.run_6()
    test_case_7.run_7()
    test_case_8.run_8()
    test_case_9.run_9()
    test_case_10.run_10()

if __name__ == '__main__':
    os.chdir(SERVER_SHARED_DIR)    # work dir
    call(['touch', 'file_1', 'file_2', 'file_3'])
    start_cases()


