from zacc.util import shell


def git_grep(string):
    return shell(["git", "grep", "--no-color", "--line-number", string])


def git_blame(file, line):
    return shell(["git", "blame", "-L", f"{line},{line}", file])
