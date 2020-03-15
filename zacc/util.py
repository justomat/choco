import os
import subprocess
import contextlib


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


def shell(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
