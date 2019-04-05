import setuptools

setuptools.setup(
    name="prjxray",
    version="0.0.1",
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="Project X-Ray tools",
    url="https://github.com/SymbiFlow/prjxray/prjxray",
    packages=setuptools.find_packages(include=['prjxray*']),
    install_requires=['simplejson', 'fasm', 'progressbar2', 'pyjson5', 'intervaltree'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
