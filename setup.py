from setuptools import setup
import duolingo


def read_file(name):
    with open(name) as fd:
        return fd.read()

setup(
    name="duolingo-api",
    version=duolingo.__version__,
    author=duolingo.__author__,
    author_email=duolingo.__email__,
    description=duolingo.__doc__,
    url=duolingo.__url__,
    keywords="duolingo, duolingo api, language",
    license='MIT',
    py_modules=['duolingo'],
    install_requires=read_file('requirements.txt').splitlines(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=read_file('README.md')
)
