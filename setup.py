from setuptools import setup
from whitewall.setup_info import SETUP_INFO

fn = "whitewall/setup_info.py"
with open(fn, "rb") as fd:
    exec(compile(fd.read(), fn, "exec"))

if __name__ == "__main__":
    setup(**SETUP_INFO)
