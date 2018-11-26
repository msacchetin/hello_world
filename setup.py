""" This is the setuptools building module """

import os
from setuptools import setup
from setuptools import find_packages


def _path(filename):  # noqa: N802
    return os.path.join(os.path.dirname(__file__), filename)


DEFAULT_NAME = "grubseccode"
DEFAULT_REQS = [
    "paramiko"
]

if os.path.exists(_path("pip-requirements.txt")):
    with open(_path("pip-requirements.txt")) as fp:
        reqs = fp.read().strip()
else:
    reqs = DEFAULT_REQS


setup(
    name=DEFAULT_NAME,
    version="1.0.1b0",
    module_name=DEFAULT_NAME,
    author="Grubhub",
    author_email="infosec@grubhub.com",
    description="InfoSec Automation",
    url="https://github.com/securitytechnology/hello_world",
    package_dir={"": "."},
    packages=find_packages("."),
    license="Proprietary",
    install_requires=reqs,
    include_package_data=True
)