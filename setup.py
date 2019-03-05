import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name='json_viewer',
        version='0.1.1',
        scripts=['json_viewer'],
        author="arfan",
        author_email="abdul.arfan@gmail.com",
        description="A Python GUI json viewer",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/arfan/json-viewer",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
    )
