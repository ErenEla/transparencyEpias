from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transparencyEPIAS", # Replace with your own username
    version="0.0.1",
    author="Eren Ela",
    author_email="ela.eren1@gmail.com",
    description="ackage for EPIAS (Turkish Electricity Market Operating Company) Transparency API Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErenEla/transparencyEpias",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.2',
)

#source packing.python