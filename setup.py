import os
import codecs
import re

from setuptools import find_packages, setup

# loosely based on https://github.com/python-attrs/attrs

HERE = os.path.abspath(os.path.dirname(__file__))

NAME = "xfacter"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "xfacter", "__init__.py")
CLASSIFIERS = [
    "Development Status :: 1 - Experimental",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

INSTALL_REQUIRES = []


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


# after pip 10.x, no more pip.req.parse_requirements
def read_requirements():
    """
    Parse requirements.txt file
    """
    with open('requirements.txt') as f:
        for l in f.readlines():
            if not l.startswith('#'):
                INSTALL_REQUIRES.append(l.strip())

META_FILE = read(META_PATH)
VERSION = find_meta("version")
DESCRIPTION = find_meta("description")
TITLE = find_meta("title")
LICENSE = find_meta("license")
AUTHOR = find_meta("author")
URL = find_meta("url")

read_requirements()

if __name__ == "__main__":
    setup(
            name=NAME,
            author=AUTHOR,
            version=VERSION,
            url=URL,
            description=DESCRIPTION,
            license=LICENSE,
            packages=PACKAGES,
            install_requires=INSTALL_REQUIRES,
            package_dir={"": "src"},
            python_requires=">=3.5",
            entry_points={
                'console_scripts': ['xfacter-server=xfacter:serve']
                }
        )
