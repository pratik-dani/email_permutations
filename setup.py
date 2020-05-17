import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='email_permutations',
    version="0.6.0",
    author="Pratik Dani",
    author_email="danipratik91@gmail.com",
    description="To Find All Possible Permtations & Combinations for a given first name and last name",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devildani/email_permutations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)