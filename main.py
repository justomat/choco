import subprocess
import re


def main():
    todos = git_grep("TODO")
    for todo in todos.splitlines():
        file, line = todo.split(":")[:2]
        out = git_blame(file, line)

        matches = re.match(
            r"^(?P<hash>[0-9a-f]{10}) (?P<filepath>.+?) \((?P<author>.+?) (?P<timestamp>.+?) \d+\)(?P<snippet>.+$)",
            out,
        )

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
    main()
