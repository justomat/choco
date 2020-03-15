import subprocess
import re
import sys


def zacc():
    todos = git_grep("TODO")
    for todo in todos.splitlines():
        file, line = todo.split(":")[:2]
        out = git_blame(file, line)

        test = re.compile(
            r"^(?P<hash>[0-9a-f]{10})"
            r" (?P<filepath>.+?)"
            r" \((?P<author>.+?)"
            r" (?P<timestamp>.+?) \d+\)"
            r"(?P<snippet>.+$)"
        )

        matches = re.match(test, out)

        if matches:
            print(matches.groupdict())


def git_grep(string):
    return run(["git", "grep", "--no-color", "-n", string])


def git_blame(file, line):
    return run(["git", "blame", "-L", "{0},{0}".format(line), file])


def run(command):
    with subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    ) as out:
        stdout, stderr = out.communicate()
        return stdout.decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        zacc(".")
    else:
        zacc(sys.argv[1])
