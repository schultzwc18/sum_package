import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    fh.close()

setuptools.setup(
    name="sum-package",
    version="0.1.0",
    author="Will Schultz",
    author_email="schultzwc18@gmail.com",
    description="sum two numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schultzwc18/sum_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
