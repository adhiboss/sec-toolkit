from setuptools import setup, find_packages

setup(
    name="sec-toolkit",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sec-toolkit=cli:main',
        ],
    },
)
