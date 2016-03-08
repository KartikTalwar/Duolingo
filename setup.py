from setuptools import setup
import duolingo

with open('README.md') as fd:
    long_description = fd.read()

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
    install_requires=("Werkzeug", "requests"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=long_description
)
