import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moneyFlowIndicator",
    version="0.0.2",
    author="Example Author",
    author_email="author@example.com",
    description="Institutional money flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pstrito/InstitutionalPip.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
