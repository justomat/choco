from concurrent.futures import ThreadPoolExecutor

from zacc.git import git_grep, git_blame
from zacc.util import pushd


def blame_todos():
    with git_grep("TODO") as grep_fork:
        for line in grep_fork.stdout:
            print(blame(line))


def blame_todos_parallel():
    with ThreadPoolExecutor() as executor:
        with git_grep("TODO") as grep_fork:
            executor.map(lambda line: print(blame(line)), grep_fork.stdout)


def blame(grep_output):
    file, linenumber, *_ = grep_output.rstrip().split(":")
    with git_blame(file, linenumber) as blame_fork:
        stdout, _ = blame_fork.communicate()
        return stdout


def run(path):
    with pushd(path):
        # blame_todos()
        blame_todos_parallel()
