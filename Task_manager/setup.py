from setuptools import setup

setup(
    name="task_manager",
    version="0.1.0",
    packages=["source"],
    entry_points={"console_scripts": ["tsk = source.cli:main"]},
)
