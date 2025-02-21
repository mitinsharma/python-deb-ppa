from setuptools import setup, find_packages

setup(
    name="hello-ppa",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "hello-ppa=hello_ppa.main:greet"
        ]
    }
)