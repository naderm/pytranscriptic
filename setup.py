from setuptools import setup, find_packages

setup(
    name="pyscriptic",
    version="0.0.1",
    author="Nader Morshed",
    url="https://github.com/naderm/pytranscriptic",
    author_email="morshed.nader@gmail.com",
    packages=find_packages("pyscriptic"),
    package_dir={"": "pyscriptic"},
    description="Python wrapper around transcriptic API",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering",
    ],
    test_suite="tests",
)
