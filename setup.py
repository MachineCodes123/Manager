
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Manager",
    version="0.0.2",
    author="MachineCodes",
    author_email="machinecodespython@gmail.com",
    description="Un programa simple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MachineCodes/Manager",
    packages=["Manager"],
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.6',
)
