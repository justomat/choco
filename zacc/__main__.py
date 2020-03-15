import sys

from zacc import app

if __name__ == "__main__":
    if len(sys.argv) < 2:
        app.run(".")
    else:
        app.run(sys.argv[1])
