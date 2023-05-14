import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="restdantic",
    version="0.0.0",
    description="",
    keywords=[],
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Bartłomiej Nowak and Michał Pleszczyński",
    author_email="n.bartek3762@gmail.com, TODO: michal_email",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["pydantic"],
    entry_points={},
)
