from setuptools import setup, find_packages

setup(
    name="autopyperf",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="Lightweight automatic profiler and optimizer suggestion tool for Python code.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/autopyperf",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
