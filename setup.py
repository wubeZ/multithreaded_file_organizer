from setuptools import setup, find_packages

setup(
    name="multithreaded_file_organizer",
    version="1.0.0",
    author="Wubshet Zeleke",
    author_email="wubezeleke@gmail.com",
    description="A multithreaded CLI tool to organize files by type, date, or size",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'organize=organizer.cli:main',
        ],
    },
    install_requires=['tqdm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)