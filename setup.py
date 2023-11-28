from setuptools import setup, find_packages

setup(
    name="blinky_mcblinkster",
    version="0.1.0",  # Update the version number for new releases
    description="A Python project for LED animations",  # A short description
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    url="https://github.com/yourusername/blinky_mcblinkster",  # Replace with your project's URL
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=[
        # Add your project dependencies here
        "pygame",  # Example dependency, replace with your actual dependencies
        # 'another-package==version',
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",  # Change as appropriate
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Choose an appropriate license
        "Programming Language :: Python :: 3",  # Specify your Py version
        "Programming Language :: Python :: 3.9",  # Specify the exact Python version if needed
    ],
    python_requires=">=3.6",  # Minimum version requirement of the package
    entry_points={  # Optional
        "console_scripts": [
            # Entry points for automatic script creation
        ],
    },
)
