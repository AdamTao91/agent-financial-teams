"""Financial Teams CLI Tool Setup Configuration."""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="financial-teams",
    version="1.0.0",
    description="Financial Teams CLI - 专业金融AI分析工具",
    author="Financial Teams",
    author_email="contact@financial-teams.ai",
    url="https://github.com/financial-teams/cli",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ft=cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
